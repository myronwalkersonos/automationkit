"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.aspects import Aspects, DEFAULT_ASPECTS

from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class InboundConnectionConfig1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'InboundConnectionConfig1' service.
    """

    SERVICE_MANUFACTURER = 'UPnP'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:InboundConnectionConfig:1'

    SERVICE_EVENT_VARIABLES = {}

    def action_GetDynamicDNSSupportedProtocols(self, *, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetDynamicDNSSupportedProtocols action.

            :returns: "DynamicDNSSupportedProtocols"
        """
        arguments = { }

        out_params = self.call_action("GetDynamicDNSSupportedProtocols", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("DynamicDNSSupportedProtocols",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetNetworkTopologyInfo(self, *, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetNetworkTopologyInfo action.

            :returns: "CurrentNetworkTopologyInfo"
        """
        arguments = { }

        out_params = self.call_action("GetNetworkTopologyInfo", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentNetworkTopologyInfo",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetDynamicDNSConfigInfo(self, NewDynamicDNSConfigInfo, *, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the SetDynamicDNSConfigInfo action.
        """
        arguments = {
            "NewDynamicDNSConfigInfo": NewDynamicDNSConfigInfo,
        }

        self.call_action("SetDynamicDNSConfigInfo", arguments=arguments, aspects=aspects)

        return

    def action_SetSTUNServerAddress(self, NewSTUNServerAddress, *, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the SetSTUNServerAddress action.
        """
        arguments = {
            "NewSTUNServerAddress": NewSTUNServerAddress,
        }

        self.call_action("SetSTUNServerAddress", arguments=arguments, aspects=aspects)

        return
