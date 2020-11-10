"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class Layer3Forwarding1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'Layer3Forwarding1' service.
    """

    SERVICE_MANUFACTURER = 'UPnP'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:Layer3Forwarding:1'


    def action_GetDefaultConnectionService(self, extract_returns=True):
        """
            Calls the GetDefaultConnectionService action.

            :returns: "NewDefaultConnectionService"
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDefaultConnectionService", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewDefaultConnectionService",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetDefaultConnectionService(self, NewDefaultConnectionService, extract_returns=True):
        """
            Calls the SetDefaultConnectionService action.

            :returns: "result"
        """
        arguments = {
            "NewDefaultConnectionService": NewDefaultConnectionService,
        }

        out_params = self.proxy_call_action("SetDefaultConnectionService", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args
