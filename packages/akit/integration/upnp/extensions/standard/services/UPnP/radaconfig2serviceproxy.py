"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.aspects import Aspects, DEFAULT_ASPECTS

from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class RADAConfig2ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'RADAConfig2' service.
    """

    SERVICE_MANUFACTURER = 'UPnP'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:RADAConfig:2'

    SERVICE_EVENT_VARIABLES = {
        "SystemInfoUpdateID": { "data_type": "ui4", "default": None, "allowed_list": None},
    }

    def action_CreateVirtualDevice(self, VirtualDeviceDescr, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the CreateVirtualDevice action.

            :returns: "VirtualDeviceID"
        """
        arguments = {
            "VirtualDeviceDescr": VirtualDeviceDescr,
        }

        out_params = self._proxy_call_action("CreateVirtualDevice", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("VirtualDeviceID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_DestroyVirtualDevice(self, VirtualDeviceID, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the DestroyVirtualDevice action.
        """
        arguments = {
            "VirtualDeviceID": VirtualDeviceID,
        }

        self._proxy_call_action("DestroyVirtualDevice", arguments=arguments, aspects=aspects)

        return

    def action_EditFilter(self, Filter, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the EditFilter action.
        """
        arguments = {
            "Filter": Filter,
        }

        self._proxy_call_action("EditFilter", arguments=arguments, aspects=aspects)

        return

    def action_GetSystemInfo(self, ID, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetSystemInfo action.

            :returns: "SystemInfo"
        """
        arguments = {
            "ID": ID,
        }

        out_params = self._proxy_call_action("GetSystemInfo", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("SystemInfo",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetVirtualDevices(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetVirtualDevices action.

            :returns: "VirtualDeviceList"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetVirtualDevices", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("VirtualDeviceList",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args
