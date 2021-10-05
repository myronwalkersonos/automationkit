"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.aspects import Aspects, DEFAULT_ASPECTS

from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class WLANConfiguration1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'WLANConfiguration1' service.
    """

    SERVICE_MANUFACTURER = 'UPnP'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:WLANConfiguration:1'

    SERVICE_EVENT_VARIABLES = {
        "TotalAssociations": { "data_type": "ui2", "default": None, "allowed_list": None},
    }

    def action_FactoryDefaultReset(self, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the FactoryDefaultReset action.
        """
        arguments = { }

        self._proxy_call_action("FactoryDefaultReset", arguments=arguments, aspects=aspects)

        return

    def action_Get11iBeaconSecurityProperties(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the Get11iBeaconSecurityProperties action.

            :returns: "NewIEEE11iEncryptionModes", "NewIEEE11iAuthenticationMode"
        """
        arguments = { }

        out_params = self._proxy_call_action("Get11iBeaconSecurityProperties", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewIEEE11iEncryptionModes", "NewIEEE11iAuthenticationMode",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetAuthenticationServiceMode(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetAuthenticationServiceMode action.

            :returns: "NewAuthenticationServiceMode"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetAuthenticationServiceMode", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewAuthenticationServiceMode",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetAutoRateFallBackMode(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetAutoRateFallBackMode action.

            :returns: "NewAutoRateFallBackEnabled"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetAutoRateFallBackMode", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewAutoRateFallBackEnabled",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetBSSID(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetBSSID action.

            :returns: "NewBSSID"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetBSSID", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewBSSID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetBasicBeaconSecurityProperties(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetBasicBeaconSecurityProperties action.

            :returns: "NewBasicEncryptionModes", "NewBasicAuthenticationMode"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetBasicBeaconSecurityProperties", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewBasicEncryptionModes", "NewBasicAuthenticationMode",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetBeaconAdvertisement(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetBeaconAdvertisement action.

            :returns: "NewBeaconAdvertisementEnabled"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetBeaconAdvertisement", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewBeaconAdvertisementEnabled",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetBeaconType(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetBeaconType action.

            :returns: "NewBeaconType"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetBeaconType", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewBeaconType",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetByteStatistics(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetByteStatistics action.

            :returns: "NewTotalBytesSent", "NewTotalBytesReceived"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetByteStatistics", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewTotalBytesSent", "NewTotalBytesReceived",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetChannelInfo(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetChannelInfo action.

            :returns: "NewChannel", "NewPossibleChannels"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetChannelInfo", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewChannel", "NewPossibleChannels",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetChannelsInUse(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetChannelsInUse action.

            :returns: "NewChannelsInUse"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetChannelsInUse", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewChannelsInUse",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetDataTransmissionRateInfo(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetDataTransmissionRateInfo action.

            :returns: "NewBasicDataTransmissionRates", "NewOperationalDataTransmissionRates", "NewPossibleDataTransmissionRates"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetDataTransmissionRateInfo", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewBasicDataTransmissionRates", "NewOperationalDataTransmissionRates", "NewPossibleDataTransmissionRates",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetDefaultWEPKeyIndex(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetDefaultWEPKeyIndex action.

            :returns: "NewDefaultWEPKeyIndex"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetDefaultWEPKeyIndex", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewDefaultWEPKeyIndex",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetDeviceOperationMode(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetDeviceOperationMode action.

            :returns: "NewDeviceOperationMode", "NewSSID", "NewBSSID", "NewChannel", "NewBasicDataTransmissionRates", "NewOperationalDataTransmissionRates", "NewDistanceFromRoot"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetDeviceOperationMode", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewDeviceOperationMode", "NewSSID", "NewBSSID", "NewChannel", "NewBasicDataTransmissionRates", "NewOperationalDataTransmissionRates", "NewDistanceFromRoot",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetFailureStatusInfo(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetFailureStatusInfo action.

            :returns: "NewTotalIntegrityFailures", "NewTotalPSKFailures"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetFailureStatusInfo", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewTotalIntegrityFailures", "NewTotalPSKFailures",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetGenericAssociatedDeviceInfo(self, NewAssociatedDeviceIndex, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetGenericAssociatedDeviceInfo action.

            :returns: "NewAssociatedDeviceMACAddress", "NewAssociatedDeviceIPAddress", "NewAssociatedDeviceAuthenticationState"
        """
        arguments = {
            "NewAssociatedDeviceIndex": NewAssociatedDeviceIndex,
        }

        out_params = self._proxy_call_action("GetGenericAssociatedDeviceInfo", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewAssociatedDeviceMACAddress", "NewAssociatedDeviceIPAddress", "NewAssociatedDeviceAuthenticationState",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetInsecureOutOfBandAccessMode(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetInsecureOutOfBandAccessMode action.

            :returns: "NewInsecureOutOfBandAccessEnabled"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetInsecureOutOfBandAccessMode", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewInsecureOutOfBandAccessEnabled",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetLocationDescription(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetLocationDescription action.

            :returns: "NewLocationDescription"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetLocationDescription", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewLocationDescription",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetPacketStatistics(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetPacketStatistics action.

            :returns: "NewTotalPacketsSent", "NewTotalPacketsReceived"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetPacketStatistics", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewTotalPacketsSent", "NewTotalPacketsReceived",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetPreSharedKey(self, NewPreSharedKeyIndex, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetPreSharedKey action.

            :returns: "NewPreSharedKey", "NewPSKPassphrase"
        """
        arguments = {
            "NewPreSharedKeyIndex": NewPreSharedKeyIndex,
        }

        out_params = self._proxy_call_action("GetPreSharedKey", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewPreSharedKey", "NewPSKPassphrase",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetRadioMode(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetRadioMode action.

            :returns: "NewRadioEnabled"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetRadioMode", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewRadioEnabled",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetRegulatoryDomain(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetRegulatoryDomain action.

            :returns: "NewRegulatoryDomain"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetRegulatoryDomain", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewRegulatoryDomain",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetSSID(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetSSID action.

            :returns: "NewSSID"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetSSID", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewSSID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetSecurityKeys(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetSecurityKeys action.

            :returns: "NewWEPKey0", "NewWEPKey1", "NewWEPKey2", "NewWEPKey3", "NewPreSharedKey", "NewKeyPassphrase"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetSecurityKeys", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewWEPKey0", "NewWEPKey1", "NewWEPKey2", "NewWEPKey3", "NewPreSharedKey", "NewKeyPassphrase",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetSpecificAssociatedDeviceInfo(self, NewAssociatedDeviceMACAddress, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetSpecificAssociatedDeviceInfo action.

            :returns: "NewAssociatedDeviceIPAddress", "NewAssociatedDeviceAuthenticationState"
        """
        arguments = {
            "NewAssociatedDeviceMACAddress": NewAssociatedDeviceMACAddress,
        }

        out_params = self._proxy_call_action("GetSpecificAssociatedDeviceInfo", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewAssociatedDeviceIPAddress", "NewAssociatedDeviceAuthenticationState",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetTotalAssociations(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetTotalAssociations action.

            :returns: "NewTotalAssociations"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetTotalAssociations", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewTotalAssociations",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetWPABeaconSecurityProperties(self, extract_returns=True, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the GetWPABeaconSecurityProperties action.

            :returns: "NewWPAEncryptionModes", "NewWPAAuthenticationMode"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetWPABeaconSecurityProperties", arguments=arguments, aspects=aspects)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewWPAEncryptionModes", "NewWPAAuthenticationMode",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_ResetAuthentication(self, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the ResetAuthentication action.
        """
        arguments = { }

        self._proxy_call_action("ResetAuthentication", arguments=arguments, aspects=aspects)

        return

    def action_Set11iBeaconSecurityProperties(self, NewIEEE11iEncryptionModes, NewIEEE11iAuthenticationMode, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the Set11iBeaconSecurityProperties action.
        """
        arguments = {
            "NewIEEE11iEncryptionModes": NewIEEE11iEncryptionModes,
            "NewIEEE11iAuthenticationMode": NewIEEE11iAuthenticationMode,
        }

        self._proxy_call_action("Set11iBeaconSecurityProperties", arguments=arguments, aspects=aspects)

        return

    def action_SetAuthenticationServiceMode(self, NewAuthenticationServiceMode, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the SetAuthenticationServiceMode action.
        """
        arguments = {
            "NewAuthenticationServiceMode": NewAuthenticationServiceMode,
        }

        self._proxy_call_action("SetAuthenticationServiceMode", arguments=arguments, aspects=aspects)

        return

    def action_SetAutoRateFallBackMode(self, NewAutoRateFallBackEnabled, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the SetAutoRateFallBackMode action.
        """
        arguments = {
            "NewAutoRateFallBackEnabled": NewAutoRateFallBackEnabled,
        }

        self._proxy_call_action("SetAutoRateFallBackMode", arguments=arguments, aspects=aspects)

        return

    def action_SetBasicBeaconSecurityProperties(self, NewBasicEncryptionModes, NewBasicAuthenticationMode, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the SetBasicBeaconSecurityProperties action.
        """
        arguments = {
            "NewBasicEncryptionModes": NewBasicEncryptionModes,
            "NewBasicAuthenticationMode": NewBasicAuthenticationMode,
        }

        self._proxy_call_action("SetBasicBeaconSecurityProperties", arguments=arguments, aspects=aspects)

        return

    def action_SetBeaconAdvertisement(self, NewBeaconAdvertisementEnabled, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the SetBeaconAdvertisement action.
        """
        arguments = {
            "NewBeaconAdvertisementEnabled": NewBeaconAdvertisementEnabled,
        }

        self._proxy_call_action("SetBeaconAdvertisement", arguments=arguments, aspects=aspects)

        return

    def action_SetBeaconType(self, NewBeaconType, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the SetBeaconType action.
        """
        arguments = {
            "NewBeaconType": NewBeaconType,
        }

        self._proxy_call_action("SetBeaconType", arguments=arguments, aspects=aspects)

        return

    def action_SetChannel(self, NewChannel, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the SetChannel action.
        """
        arguments = {
            "NewChannel": NewChannel,
        }

        self._proxy_call_action("SetChannel", arguments=arguments, aspects=aspects)

        return

    def action_SetDataTransmissionRates(self, NewBasicDataTransmissionRates, NewOperationalDataTransmissionRates, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the SetDataTransmissionRates action.
        """
        arguments = {
            "NewBasicDataTransmissionRates": NewBasicDataTransmissionRates,
            "NewOperationalDataTransmissionRates": NewOperationalDataTransmissionRates,
        }

        self._proxy_call_action("SetDataTransmissionRates", arguments=arguments, aspects=aspects)

        return

    def action_SetDefaultWEPKeyIndex(self, NewDefaultWEPKeyIndex, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the SetDefaultWEPKeyIndex action.
        """
        arguments = {
            "NewDefaultWEPKeyIndex": NewDefaultWEPKeyIndex,
        }

        self._proxy_call_action("SetDefaultWEPKeyIndex", arguments=arguments, aspects=aspects)

        return

    def action_SetDeviceOperationMode(self, NewDeviceOperationMode, NewSSID, NewBSSID, NewChannel, NewBasicDataTransmissionRates, NewOperationalDataTransmissionRates, NewDistanceFromRoot, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the SetDeviceOperationMode action.
        """
        arguments = {
            "NewDeviceOperationMode": NewDeviceOperationMode,
            "NewSSID": NewSSID,
            "NewBSSID": NewBSSID,
            "NewChannel": NewChannel,
            "NewBasicDataTransmissionRates": NewBasicDataTransmissionRates,
            "NewOperationalDataTransmissionRates": NewOperationalDataTransmissionRates,
            "NewDistanceFromRoot": NewDistanceFromRoot,
        }

        self._proxy_call_action("SetDeviceOperationMode", arguments=arguments, aspects=aspects)

        return

    def action_SetInsecureOutOfBandAccessMode(self, NewInsecureOutOfBandAccessEnabled, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the SetInsecureOutOfBandAccessMode action.
        """
        arguments = {
            "NewInsecureOutOfBandAccessEnabled": NewInsecureOutOfBandAccessEnabled,
        }

        self._proxy_call_action("SetInsecureOutOfBandAccessMode", arguments=arguments, aspects=aspects)

        return

    def action_SetLocationDescription(self, NewLocationDescription, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the SetLocationDescription action.
        """
        arguments = {
            "NewLocationDescription": NewLocationDescription,
        }

        self._proxy_call_action("SetLocationDescription", arguments=arguments, aspects=aspects)

        return

    def action_SetPreSharedKey(self, NewPreSharedKeyIndex, NewPreSharedKey, NewPSKPassphrase, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the SetPreSharedKey action.
        """
        arguments = {
            "NewPreSharedKeyIndex": NewPreSharedKeyIndex,
            "NewPreSharedKey": NewPreSharedKey,
            "NewPSKPassphrase": NewPSKPassphrase,
        }

        self._proxy_call_action("SetPreSharedKey", arguments=arguments, aspects=aspects)

        return

    def action_SetRadioMode(self, NewRadioEnabled, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the SetRadioMode action.
        """
        arguments = {
            "NewRadioEnabled": NewRadioEnabled,
        }

        self._proxy_call_action("SetRadioMode", arguments=arguments, aspects=aspects)

        return

    def action_SetRegulatoryDomain(self, NewRegulatoryDomain, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the SetRegulatoryDomain action.
        """
        arguments = {
            "NewRegulatoryDomain": NewRegulatoryDomain,
        }

        self._proxy_call_action("SetRegulatoryDomain", arguments=arguments, aspects=aspects)

        return

    def action_SetSSID(self, NewSSID, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the SetSSID action.
        """
        arguments = {
            "NewSSID": NewSSID,
        }

        self._proxy_call_action("SetSSID", arguments=arguments, aspects=aspects)

        return

    def action_SetSecurityKeys(self, NewWEPKey0, NewWEPKey1, NewWEPKey2, NewWEPKey3, NewPreSharedKey, NewKeyPassphrase, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the SetSecurityKeys action.
        """
        arguments = {
            "NewWEPKey0": NewWEPKey0,
            "NewWEPKey1": NewWEPKey1,
            "NewWEPKey2": NewWEPKey2,
            "NewWEPKey3": NewWEPKey3,
            "NewPreSharedKey": NewPreSharedKey,
            "NewKeyPassphrase": NewKeyPassphrase,
        }

        self._proxy_call_action("SetSecurityKeys", arguments=arguments, aspects=aspects)

        return

    def action_SetWPABeaconSecurityProperties(self, NewWPAEncryptionModes, NewWPAAuthenticationMode, aspects:Aspects=DEFAULT_ASPECTS):
        """
            Calls the SetWPABeaconSecurityProperties action.
        """
        arguments = {
            "NewWPAEncryptionModes": NewWPAEncryptionModes,
            "NewWPAAuthenticationMode": NewWPAAuthenticationMode,
        }

        self._proxy_call_action("SetWPABeaconSecurityProperties", arguments=arguments, aspects=aspects)

        return
