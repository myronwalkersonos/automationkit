"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.aspects import Aspects, DEFAULT_ASPECTS

from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class ExternalActivity1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'ExternalActivity1' service.
    """

    SERVICE_MANUFACTURER = 'UPnP'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:ExternalActivity:1'

    SERVICE_EVENT_VARIABLES = {
        "Activity": { "data_type": "string", "default": None, "allowed_list": None},
        "AvailableRegistrations": { "data_type": "boolean", "default": "1", "allowed_list": None},
    }

    def action_Register(self, ButtonNameIn, DisplayStringIn, DurationIn, *, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the Register action.

            :returns: "ActualDurationOut", "RegistrationIDOut"
        """
        arguments = {
            "ButtonNameIn": ButtonNameIn,
            "DisplayStringIn": DisplayStringIn,
            "DurationIn": DurationIn,
        }

        out_params = self.call_action("Register", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("ActualDurationOut", "RegistrationIDOut",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args
