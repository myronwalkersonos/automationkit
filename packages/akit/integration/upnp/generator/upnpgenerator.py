
import netifaces
import os
import sys

from argparse import ArgumentParser, ArgumentError

from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import fromstring as xml_fromstring

from akit.integration.coordinators.upnpcoordinator import UpnpCoordinator
from akit.integration.upnp.extensions import services as services_extensions


DIR_UPNP_GENERATOR = os.path.dirname(__file__)

DIR_UPNP_GENERATOR_DYNAMIC = os.path.join(DIR_UPNP_GENERATOR, "dynamic")
DIR_UPNP_GENERATOR_STANDARD = os.path.join(DIR_UPNP_GENERATOR, "standard")

DIR_UPNP_EXTENSIONS = os.path.dirname(services_extensions.__file__)

DIR_UPNP_EXTENSIONS_DYNAMIC = os.path.join(DIR_UPNP_EXTENSIONS, "dynamic")
DIR_UPNP_EXTENSIONS_STANDARD = os.path.join(DIR_UPNP_EXTENSIONS, "standard")

DIR_UPNP_GENERATOR_DYNAMIC_SERVICES = os.path.join(DIR_UPNP_GENERATOR, "dynamic", "services")
DIR_UPNP_GENERATOR_STANDARD_SERVICES = os.path.join(DIR_UPNP_GENERATOR, "standard", "services")

UPNP_SERVICE_NAMESPACE = "urn:schemas-upnp-org:service-1-0"

MANUFACTURER_TO_BASE_CLASSES = {
    'SonosInc': ("akit.integration.upnp.devices.embedded.upnpdevice", "SonosDevice")
}

CONTENT_PROXY_FILE_HEADER = """
    NOTE: This is a code generated file.  This file should not be edited directly.
"""

TEMPLATE_CLASS_PREFIX = """

from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class %(class_name)s(UpnpServiceProxy, LoadableExtension):
    \"""
        This is a code generated proxy class to the '%(class_name_base)s' service.
    \"""

    SERVICE_TYPE = '%(service_type)s'
    SERVICE_ID = '%(service_id)s'

"""

TEMPLATE_GETTER = """
    def get_%(var_name)s(self):
        \"""
            Gets the "%(var_name)s" variable.
        \"""
        rval = self.proxy_get_variable_value("%(var_name)s")
        return rval

"""

TEMPLATE_SETTER = """
    def set_%(var_name)s(self, val):
        \"""
            Sets the "%(var_name)s" variable.
        \"""
        self.proxy_set_variable_value("%(var_name)s", val)
        return

"""

TEMPLATE_ACTION = """
    def action_%(action_name)s(self%(in_params_comma)s%(in_params_list)s):
        \"""
            Calls the %(action_name)s action.
        \"""
        arguments = %(args_dict)s
        out_params = self.proxy_call_action("%(action_name)s", arguments=arguments)

        (%(out_params_list)s,) = out_params

        return %(out_params_list)s

"""

def node_lower_strip_text(txt):
    if txt is not None:
        txt = txt.lower().strip()
    return txt

def node_strip_text(txt):
    if txt is not None:
        txt = txt.strip()
    return txt

def generate_upnp_service_proxy(destinationDir, serviceType, variablesTable, typesTable, eventsTable, actionsTable):

    if not os.path.exists(destinationDir):
        os.makedirs(destinationDir)

    service_type_parts = serviceType.split(":")
    service_id = ":".join(service_type_parts[:-1])

    class_name_base = service_type_parts[3] + service_type_parts[-1]
    class_name = class_name_base + "ServiceProxy"
    file_base = class_name.lower() + ".py"

    class_fill_dict = {
        "class_name": class_name,
        "class_name_base": class_name_base,
        "service_type": serviceType,
        "service_id": service_id
    }

    dest_file_full = os.path.join(destinationDir, file_base)
    with open(dest_file_full, 'w') as spf:
        spf.write('"""\n')
        spf.write(CONTENT_PROXY_FILE_HEADER)
        spf.write('"""\n')
        spf.write('\n')
        spf.write(TEMPLATE_CLASS_PREFIX % class_fill_dict)

        variable_names_sorted = [ k for k in variablesTable.keys() ]
        variable_names_sorted.sort()

        for var_name in variable_names_sorted:
            variable_info = variablesTable[var_name]

            var_name = variable_info["name"]
            var_type = variable_info["dataType"]
            var_send_events = variable_info["sendEvents"]

            var_allowed_list = None
            if "allowedValueList" in variable_info:
                var_allowed_list = variable_info["allowedValueList"]

            var_default_value = None
            if "defaultValue" in variable_info:
                var_default_value = variable_info["defaultValue"]

            var_fill_dict = {
                'var_name': var_name,
                'var_type': var_type,
            }

            # Generate the getter
            spf.write(TEMPLATE_GETTER % var_fill_dict)

            # Generate the setter
            spf.write(TEMPLATE_SETTER % var_fill_dict)

        action_names_sorted = [ k for k in actionsTable.keys() ]
        action_names_sorted.sort()

        for action_name in action_names_sorted:

            action_info = actionsTable[action_name]

            in_params_list = ""
            out_params_list = "result"

            args_dict = "{ }\n"
            args_in_table = action_info["args_in"]
            args_in_keys = action_info["args_in_keys"]
            if len(args_in_keys) > 0:
                in_params_list = ", ".join(args_in_keys)
                args_dict = "{\n"
                for arg_key in args_in_keys:
                    args_dict += '            "%s": %s,\n' % (arg_key, arg_key)
                args_dict += "        }\n"

            in_params_comma = ""
            if len(in_params_list) > 0:
                in_params_comma = ", "

            args_out_table = action_info["args_out"]
            args_out_keys = action_info["args_out_keys"]
            if len(args_out_keys) > 0:
                out_params_list = ", ".join(args_out_keys)

            action_fill = {
                "action_name": action_name,
                "in_params_list": in_params_list,
                "in_params_comma": in_params_comma,
                "out_params_list": out_params_list,
                "args_dict": args_dict
            }
            spf.write(TEMPLATE_ACTION % action_fill)

    return

def process_action_list(svcActionListNode, namespaces=None):

    actionsTable = {}

    actionNodeList = svcActionListNode.findall("action", namespaces=namespaces)
    for actionNode in actionNodeList:
        action_name = node_strip_text(actionNode.find("name", namespaces=namespaces).text)
        args_in_keys = []
        args_in_table = {}
        args_out_keys = []
        args_out_table = {}

        argumentListNode = actionNode.find("argumentList", namespaces=namespaces)
        if argumentListNode is not None:
            argumentNodeList = argumentListNode.findall("argument")
            for argumentNode in argumentNodeList:
                arg_info = {}
                arg_name = node_strip_text(argumentNode.find("name", namespaces=namespaces).text)
                arg_direction = node_lower_strip_text(argumentNode.find("direction", namespaces=namespaces).text)

                arg_related = None
                argRelatedNode = argumentNode.find("relatedStateVariable", namespaces=namespaces)
                if argRelatedNode is not None:
                    arg_related = node_strip_text(argRelatedNode.text)

                arg_info["name"] = arg_name
                arg_info["direction"] = arg_direction
                arg_info["relatedStateVariable"] = arg_related

                if arg_direction == "in":
                    args_in_keys.append(arg_name)
                    args_in_table[arg_name] = arg_info
                elif arg_direction == "out":
                    args_out_keys.append(arg_name)
                    args_out_table[arg_name] = arg_info
                else:
                    raise ValueError("Invalid argument direction %s" % arg_direction)

                action_info = { 
                    "name": action_name, 
                    "args_in": args_in_table,
                    "args_in_keys": args_in_keys,
                    "args_out": args_out_table,
                    "args_out_keys": args_out_keys
                }

        actionsTable[action_name] = action_info

    return actionsTable

def process_service_state_table(svcStateTableNode, namespaces=None):

    variablesTable = {}
    typesTable = {}
    eventsTable = {}

    stateVariableNodeList = svcStateTableNode.findall("stateVariable", namespaces=namespaces)

    for stateVariableNode in stateVariableNodeList:

        variable_info = {}

        var_name = node_strip_text(stateVariableNode.find("name", namespaces=namespaces).text)
        variable_info["name"] = var_name

        send_events = "no"
        if "sendEvents" in stateVariableNode.attrib:
            send_events = node_lower_strip_text(stateVariableNode.attrib["sendEvents"])
        else:
            sendEventsNode = stateVariableNode.find("sendEventsAttribute")
            if sendEventsNode is not None:
                send_events = node_lower_strip_text(sendEventsNode.text)

        variable_info["sendEvents"] = send_events


        var_type = stateVariableNode.find("dataType", namespaces=namespaces).text.strip()
        variable_info["dataType"] = var_type

        allowedValueListNode = stateVariableNode.find("allowedValueList", namespaces=namespaces)
        if allowedValueListNode is not None:
            allowed_value_list = []
            for allowedValueNode in allowedValueListNode.findall("allowedValue", namespaces=namespaces):
                allowed_value = node_strip_text(allowedValueNode.text)
                allowed_value_list.append(allowed_value)
            variable_info["allowedValueList"] = allowed_value_list

        defaultValueNode = stateVariableNode.find("defaultValue", namespaces=namespaces)
        if defaultValueNode is not None:
            default_value = node_strip_text(defaultValueNode.text)
            variable_info["defaultValue"] = default_value

        if var_name.startswith("A_ARG_TYPE_"):
            typesTable[var_name] = variable_info
        else:
            variablesTable[var_name] = variable_info
            if send_events == "yes":
                eventsTable[var_name] = variable_info

    return variablesTable, typesTable, eventsTable


def generate_service_proxies(svc_desc_directory, proxy_dest_directory):

    for dirpath, dirnames, filenames in os.walk(svc_desc_directory, topdown=True):
        for nxtfile in filenames:
            serviceType, nxtfile_ext = os.path.splitext(nxtfile)

            svc_content = None

            fullpath = os.path.join(dirpath, nxtfile)
            with open(fullpath, 'r') as xf:
                svc_content = xf.read()

            docNode = xml_fromstring(svc_content)
            if docNode != None:

                namespaces = None
                doc_node_tag = docNode.tag
                if doc_node_tag.find("}") > 0:
                    default_ns = doc_node_tag[doc_node_tag.find("{"):doc_node_tag.find("}")]
                    namespaces = {"": default_ns}

                variablesTable = {}
                typesTable = {}
                eventsTable = {}

                svcStateTableNode = docNode.find("serviceStateTable", namespaces=namespaces)
                if svcStateTableNode is not None:
                    variablesTable, typesTable, eventsTable = process_service_state_table(svcStateTableNode, namespaces=namespaces)

                actionsTable = {}
                actionListNode = docNode.find("actionList", namespaces=namespaces)
                if actionListNode is not None:
                    actionsTable = process_action_list(actionListNode, namespaces=namespaces)

                generate_upnp_service_proxy(proxy_dest_directory, serviceType, variablesTable, typesTable, eventsTable, actionsTable)
            else:
                errmsg = "WARNING: No serice node found in file:\n    %s\n" % fullpath
                print(errmsg, file=sys.stderr)

    return

def upnpgenerator_main():
    aparser = ArgumentParser()
    aparser.add_argument("--action", dest="action", action="store", choices=["scan", "generate"], default="scan",
                         help="The action to perform.")
    aparser.add_argument("--exclude-iface", dest="interfaces_excluded", action="append", default=["lo"],
                         help="The interfaces to exclude in the scan.")
    aparser.add_argument("--include-iface", dest="interfaces_included", action="append",
                         help="The interfaces to include in the scan.")

    args = aparser.parse_args()

    action = args.action
    excluded_interfaces = [iface for iface in args.interfaces_excluded]

    if action == "scan":
        ucoord = UpnpCoordinator()
        ucoord.startup_scan(None, exclude_interfaces=excluded_interfaces, response_timeout=60)

        for cdev in ucoord.children:
            cdev.record_description(DIR_UPNP_GENERATOR_DYNAMIC)

    elif action == "generate":
        if os.path.exists(DIR_UPNP_GENERATOR_DYNAMIC_SERVICES):
            generate_service_proxies(DIR_UPNP_GENERATOR_DYNAMIC_SERVICES, DIR_UPNP_EXTENSIONS_DYNAMIC)

        if os.path.exists(DIR_UPNP_GENERATOR_STANDARD_SERVICES):
            generate_service_proxies(DIR_UPNP_GENERATOR_STANDARD_SERVICES, DIR_UPNP_EXTENSIONS_STANDARD)
    else:
        raise ArgumentError("action", "The 'action' argument specified (%s) is not valid." % action)


    return

if __name__ == "__main__":
    upnpgenerator_main()