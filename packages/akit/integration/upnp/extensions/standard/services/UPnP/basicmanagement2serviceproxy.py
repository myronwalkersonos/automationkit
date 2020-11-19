"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class BasicManagement2ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'BasicManagement2' service.
    """

    SERVICE_MANUFACTURER = 'UPnP'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:BasicManagement:2'
    
    SERVICE_EVENT_VARIABLES = {}


    def action_BandwidthTest(self, BandwidthTestSpec, TestEndpoint, TestSchedule, TestSessID, extract_returns=True):
        """
            Calls the BandwidthTest action.

            :returns: "TestID"
        """
        arguments = {
            "BandwidthTestSpec": BandwidthTestSpec,
            "TestEndpoint": TestEndpoint,
            "TestSchedule": TestSchedule,
            "TestSessID": TestSessID,
        }

        out_params = self._proxy_call_action("BandwidthTest", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("TestID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_BaselineReset(self, extract_returns=True):
        """
            Calls the BaselineReset action.

            :returns: "result"
        """
        arguments = { }

        out_params = self._proxy_call_action("BaselineReset", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_CancelTest(self, TestID, extract_returns=True):
        """
            Calls the CancelTest action.

            :returns: "result"
        """
        arguments = {
            "TestID": TestID,
        }

        out_params = self._proxy_call_action("CancelTest", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetACLData(self, extract_returns=True):
        """
            Calls the GetACLData action.

            :returns: "ACL"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetACLData", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("ACL",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetActiveTestIDs(self, extract_returns=True):
        """
            Calls the GetActiveTestIDs action.

            :returns: "TestIDs"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetActiveTestIDs", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("TestIDs",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetBandwidthTestInfo(self, extract_returns=True):
        """
            Calls the GetBandwidthTestInfo action.

            :returns: "BandwidthTestInfo"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetBandwidthTestInfo", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("BandwidthTestInfo",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetBandwidthTestResult(self, TestID, extract_returns=True):
        """
            Calls the GetBandwidthTestResult action.

            :returns: "State", "Status", "AdditionalInfo", "Result"
        """
        arguments = {
            "TestID": TestID,
        }

        out_params = self._proxy_call_action("GetBandwidthTestResult", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("State", "Status", "AdditionalInfo", "Result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetDeviceStatus(self, extract_returns=True):
        """
            Calls the GetDeviceStatus action.

            :returns: "DeviceStatus"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetDeviceStatus", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("DeviceStatus",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetInterfaceResetResult(self, TestID, extract_returns=True):
        """
            Calls the GetInterfaceResetResult action.

            :returns: "Status", "AdditionalInfo", "NumberOfSuccesses", "NumberOfFailures"
        """
        arguments = {
            "TestID": TestID,
        }

        out_params = self._proxy_call_action("GetInterfaceResetResult", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("Status", "AdditionalInfo", "NumberOfSuccesses", "NumberOfFailures",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetLogInfo(self, LogURI, extract_returns=True):
        """
            Calls the GetLogInfo action.

            :returns: "Configurable", "Enabled", "LogLevel", "LogURL", "MaxSize", "LastChange"
        """
        arguments = {
            "LogURI": LogURI,
        }

        out_params = self._proxy_call_action("GetLogInfo", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("Configurable", "Enabled", "LogLevel", "LogURL", "MaxSize", "LastChange",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetLogURIs(self, extract_returns=True):
        """
            Calls the GetLogURIs action.

            :returns: "LogURIs"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetLogURIs", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("LogURIs",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetNSLookupResult(self, TestID, extract_returns=True):
        """
            Calls the GetNSLookupResult action.

            :returns: "Status", "AdditionalInfo", "SuccessCount", "Result"
        """
        arguments = {
            "TestID": TestID,
        }

        out_params = self._proxy_call_action("GetNSLookupResult", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("Status", "AdditionalInfo", "SuccessCount", "Result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetPingResult(self, TestID, extract_returns=True):
        """
            Calls the GetPingResult action.

            :returns: "Status", "AdditionalInfo", "SuccessCount", "FailureCount", "AverageResponseTime", "MinimumResponseTime", "MaximumResponseTime"
        """
        arguments = {
            "TestID": TestID,
        }

        out_params = self._proxy_call_action("GetPingResult", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("Status", "AdditionalInfo", "SuccessCount", "FailureCount", "AverageResponseTime", "MinimumResponseTime", "MaximumResponseTime",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetSelfTestResult(self, TestID, extract_returns=True):
        """
            Calls the GetSelfTestResult action.

            :returns: "Status", "AdditionalInfo"
        """
        arguments = {
            "TestID": TestID,
        }

        out_params = self._proxy_call_action("GetSelfTestResult", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("Status", "AdditionalInfo",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetSequenceMode(self, extract_returns=True):
        """
            Calls the GetSequenceMode action.

            :returns: "SequenceMode"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetSequenceMode", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("SequenceMode",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetTestIDs(self, extract_returns=True):
        """
            Calls the GetTestIDs action.

            :returns: "TestIDs"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetTestIDs", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("TestIDs",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetTestInfo(self, TestID, extract_returns=True):
        """
            Calls the GetTestInfo action.

            :returns: "Type", "State"
        """
        arguments = {
            "TestID": TestID,
        }

        out_params = self._proxy_call_action("GetTestInfo", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("Type", "State",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetTracerouteResult(self, TestID, extract_returns=True):
        """
            Calls the GetTracerouteResult action.

            :returns: "Status", "AdditionalInfo", "ResponseTime", "HopHosts"
        """
        arguments = {
            "TestID": TestID,
        }

        out_params = self._proxy_call_action("GetTracerouteResult", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("Status", "AdditionalInfo", "ResponseTime", "HopHosts",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_InterfaceReset(self, Interfaces, extract_returns=True):
        """
            Calls the InterfaceReset action.

            :returns: "TestID"
        """
        arguments = {
            "Interfaces": Interfaces,
        }

        out_params = self._proxy_call_action("InterfaceReset", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("TestID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_NSLookup(self, HostName, DNSServer, NumberOfRepetitions, Timeout, extract_returns=True):
        """
            Calls the NSLookup action.

            :returns: "TestID"
        """
        arguments = {
            "HostName": HostName,
            "DNSServer": DNSServer,
            "NumberOfRepetitions": NumberOfRepetitions,
            "Timeout": Timeout,
        }

        out_params = self._proxy_call_action("NSLookup", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("TestID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_Ping(self, Host, NumberOfRepetitions, Timeout, DataBlockSize, DSCP, extract_returns=True):
        """
            Calls the Ping action.

            :returns: "TestID"
        """
        arguments = {
            "Host": Host,
            "NumberOfRepetitions": NumberOfRepetitions,
            "Timeout": Timeout,
            "DataBlockSize": DataBlockSize,
            "DSCP": DSCP,
        }

        out_params = self._proxy_call_action("Ping", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("TestID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_Reboot(self, extract_returns=True):
        """
            Calls the Reboot action.

            :returns: "RebootStatus"
        """
        arguments = { }

        out_params = self._proxy_call_action("Reboot", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("RebootStatus",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SelfTest(self, extract_returns=True):
        """
            Calls the SelfTest action.

            :returns: "TestID"
        """
        arguments = { }

        out_params = self._proxy_call_action("SelfTest", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("TestID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetLogInfo(self, LogURI, Enabled, LogLevel, extract_returns=True):
        """
            Calls the SetLogInfo action.

            :returns: "result"
        """
        arguments = {
            "LogURI": LogURI,
            "Enabled": Enabled,
            "LogLevel": LogLevel,
        }

        out_params = self._proxy_call_action("SetLogInfo", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetSequenceMode(self, NewSequenceMode, extract_returns=True):
        """
            Calls the SetSequenceMode action.

            :returns: "OldSequenceMode"
        """
        arguments = {
            "NewSequenceMode": NewSequenceMode,
        }

        out_params = self._proxy_call_action("SetSequenceMode", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("OldSequenceMode",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_Traceroute(self, Host, Timeout, DataBlockSize, MaxHopCount, DSCP, extract_returns=True):
        """
            Calls the Traceroute action.

            :returns: "TestID"
        """
        arguments = {
            "Host": Host,
            "Timeout": Timeout,
            "DataBlockSize": DataBlockSize,
            "MaxHopCount": MaxHopCount,
            "DSCP": DSCP,
        }

        out_params = self._proxy_call_action("Traceroute", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("TestID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

