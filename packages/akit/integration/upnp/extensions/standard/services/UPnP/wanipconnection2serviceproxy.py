"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.aspects import Aspects, DEFAULT_ASPECTS

from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class WANIPConnection2ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'WANIPConnection2' service.
    """

    SERVICE_MANUFACTURER = 'UPnP'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:WANIPConnection:2'

    SERVICE_EVENT_VARIABLES = {}

    def action_AddAnyPortMapping(self, NewRemoteHost, NewExternalPort, NewProtocol, NewInternalPort, NewInternalClient, NewEnabled, NewPortMappingDescription, NewLeaseDuration, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the AddAnyPortMapping action.

            :returns: "NewReservedPort"
        """
        arguments = {
            "NewRemoteHost": NewRemoteHost,
            "NewExternalPort": NewExternalPort,
            "NewProtocol": NewProtocol,
            "NewInternalPort": NewInternalPort,
            "NewInternalClient": NewInternalClient,
            "NewEnabled": NewEnabled,
            "NewPortMappingDescription": NewPortMappingDescription,
            "NewLeaseDuration": NewLeaseDuration,
        }

        out_params = self._proxy_call_action("AddAnyPortMapping", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewReservedPort",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_AddPortMapping(self, NewRemoteHost, NewExternalPort, NewProtocol, NewInternalPort, NewInternalClient, NewEnabled, NewPortMappingDescription, NewLeaseDuration, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the AddPortMapping action.
        """
        arguments = {
            "NewRemoteHost": NewRemoteHost,
            "NewExternalPort": NewExternalPort,
            "NewProtocol": NewProtocol,
            "NewInternalPort": NewInternalPort,
            "NewInternalClient": NewInternalClient,
            "NewEnabled": NewEnabled,
            "NewPortMappingDescription": NewPortMappingDescription,
            "NewLeaseDuration": NewLeaseDuration,
        }

        self._proxy_call_action("AddPortMapping", arguments=arguments, aspects=aspects)

        return

    def action_DeletePortMapping(self, NewRemoteHost, NewExternalPort, NewProtocol, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the DeletePortMapping action.
        """
        arguments = {
            "NewRemoteHost": NewRemoteHost,
            "NewExternalPort": NewExternalPort,
            "NewProtocol": NewProtocol,
        }

        self._proxy_call_action("DeletePortMapping", arguments=arguments, aspects=aspects)

        return

    def action_DeletePortMappingRange(self, NewStartPort, NewEndPort, NewProtocol, NewManage, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the DeletePortMappingRange action.
        """
        arguments = {
            "NewStartPort": NewStartPort,
            "NewEndPort": NewEndPort,
            "NewProtocol": NewProtocol,
            "NewManage": NewManage,
        }

        self._proxy_call_action("DeletePortMappingRange", arguments=arguments, aspects=aspects)

        return

    def action_ForceTermination(self, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the ForceTermination action.
        """
        arguments = { }

        self._proxy_call_action("ForceTermination", arguments=arguments, aspects=aspects)

        return

    def action_GetAutoDisconnectTime(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetAutoDisconnectTime action.

            :returns: "NewAutoDisconnectTime"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetAutoDisconnectTime", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewAutoDisconnectTime",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetConnectionTypeInfo(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetConnectionTypeInfo action.

            :returns: "NewConnectionType", "NewPossibleConnectionTypes"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetConnectionTypeInfo", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewConnectionType", "NewPossibleConnectionTypes",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetExternalIPAddress(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetExternalIPAddress action.

            :returns: "NewExternalIPAddress"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetExternalIPAddress", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewExternalIPAddress",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetGenericPortMappingEntry(self, NewPortMappingIndex, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetGenericPortMappingEntry action.

            :returns: "NewRemoteHost", "NewExternalPort", "NewProtocol", "NewInternalPort", "NewInternalClient", "NewEnabled", "NewPortMappingDescription", "NewLeaseDuration"
        """
        arguments = {
            "NewPortMappingIndex": NewPortMappingIndex,
        }

        out_params = self._proxy_call_action("GetGenericPortMappingEntry", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewRemoteHost", "NewExternalPort", "NewProtocol", "NewInternalPort", "NewInternalClient", "NewEnabled", "NewPortMappingDescription", "NewLeaseDuration",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetIdleDisconnectTime(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetIdleDisconnectTime action.

            :returns: "NewIdleDisconnectTime"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetIdleDisconnectTime", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewIdleDisconnectTime",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetListOfPortMappings(self, NewStartPort, NewEndPort, NewProtocol, NewManage, NewNumberOfPorts, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetListOfPortMappings action.

            :returns: "NewPortListing"
        """
        arguments = {
            "NewStartPort": NewStartPort,
            "NewEndPort": NewEndPort,
            "NewProtocol": NewProtocol,
            "NewManage": NewManage,
            "NewNumberOfPorts": NewNumberOfPorts,
        }

        out_params = self._proxy_call_action("GetListOfPortMappings", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewPortListing",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetNATRSIPStatus(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetNATRSIPStatus action.

            :returns: "NewRSIPAvailable", "NewNATEnabled"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetNATRSIPStatus", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewRSIPAvailable", "NewNATEnabled",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetSpecificPortMappingEntry(self, NewRemoteHost, NewExternalPort, NewProtocol, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetSpecificPortMappingEntry action.

            :returns: "NewInternalPort", "NewInternalClient", "NewEnabled", "NewPortMappingDescription", "NewLeaseDuration"
        """
        arguments = {
            "NewRemoteHost": NewRemoteHost,
            "NewExternalPort": NewExternalPort,
            "NewProtocol": NewProtocol,
        }

        out_params = self._proxy_call_action("GetSpecificPortMappingEntry", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewInternalPort", "NewInternalClient", "NewEnabled", "NewPortMappingDescription", "NewLeaseDuration",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetStatusInfo(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetStatusInfo action.

            :returns: "NewConnectionStatus", "NewLastConnectionError", "NewUptime"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetStatusInfo", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewConnectionStatus", "NewLastConnectionError", "NewUptime",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetWarnDisconnectDelay(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetWarnDisconnectDelay action.

            :returns: "NewWarnDisconnectDelay"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetWarnDisconnectDelay", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewWarnDisconnectDelay",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_RequestConnection(self, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the RequestConnection action.
        """
        arguments = { }

        self._proxy_call_action("RequestConnection", arguments=arguments, aspects=aspects)

        return

    def action_RequestTermination(self, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the RequestTermination action.
        """
        arguments = { }

        self._proxy_call_action("RequestTermination", arguments=arguments, aspects=aspects)

        return

    def action_SetAutoDisconnectTime(self, NewAutoDisconnectTime, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the SetAutoDisconnectTime action.
        """
        arguments = {
            "NewAutoDisconnectTime": NewAutoDisconnectTime,
        }

        self._proxy_call_action("SetAutoDisconnectTime", arguments=arguments, aspects=aspects)

        return

    def action_SetConnectionType(self, NewConnectionType, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the SetConnectionType action.
        """
        arguments = {
            "NewConnectionType": NewConnectionType,
        }

        self._proxy_call_action("SetConnectionType", arguments=arguments, aspects=aspects)

        return

    def action_SetIdleDisconnectTime(self, NewIdleDisconnectTime, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the SetIdleDisconnectTime action.
        """
        arguments = {
            "NewIdleDisconnectTime": NewIdleDisconnectTime,
        }

        self._proxy_call_action("SetIdleDisconnectTime", arguments=arguments, aspects=aspects)

        return

    def action_SetWarnDisconnectDelay(self, NewWarnDisconnectDelay, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the SetWarnDisconnectDelay action.
        """
        arguments = {
            "NewWarnDisconnectDelay": NewWarnDisconnectDelay,
        }

        self._proxy_call_action("SetWarnDisconnectDelay", arguments=arguments, aspects=aspects)

        return
