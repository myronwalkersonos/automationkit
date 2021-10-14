"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.aspects import Aspects, DEFAULT_ASPECTS

from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class RemoteUIServer1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'RemoteUIServer1' service.
    """

    SERVICE_MANUFACTURER = 'UPnP'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:RemoteUIServer:1'

    SERVICE_EVENT_VARIABLES = {}

    def action_GetCompatibleUIs(self, InputDeviceProfile, UIFilter, *, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetCompatibleUIs action.

            :returns: "UIListing"
        """
        arguments = {
            "InputDeviceProfile": InputDeviceProfile,
            "UIFilter": UIFilter,
        }

        out_params = self.call_action("GetCompatibleUIs", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("UIListing",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetUILifetime(self, UI, Lifetime, *, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the SetUILifetime action.
        """
        arguments = {
            "UI": UI,
            "Lifetime": Lifetime,
        }

        self.call_action("SetUILifetime", arguments=arguments, aspects=aspects)

        return
