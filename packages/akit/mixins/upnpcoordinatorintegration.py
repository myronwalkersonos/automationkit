"""
.. module:: automationpodmixin
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Contains a ClusterMixIn object to use for working with the nodes of a cluster

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

from typing import Dict, List, Tuple

from akit.exceptions import AKitConfigurationError, AKitSemanticError

from akit.mixins.coordinatormixin import CoordinatorMixIn

from akit.integration.coordinators.upnpcoordinator import UpnpCoordinator


class UpnpCoordinatorIntegration(CoordinatorMixIn):
    """
        The UpnpCoordinatorIntegration handle the requirement registration for the UPNP coordinator.
    """

    pathbase = "/upnp"

    def __init__(self, *args, **kwargs):
        """
            The default contructor for an :class:`AutomationPodMixIn`.
        """
        super(UpnpCoordinatorIntegration, self).__init__(*args, **kwargs)
        return

    @classmethod
    def attach_to_environment(cls, constraints: Dict={}):
        """
            This API is called so that the IntegrationMixIn can process configuration information.  The :class:`IntegrationMixIn`
            will verify that it has a valid environment and configuration to run in.

            :raises :class:`akit.exceptions.AKitMissingConfigError`, :class:`akit.exceptions.AKitInvalidConfigError`:
        """
        resources_acquired = False

        upnp_device_hints = cls.landscape.get_upnp_device_config_lookup_table()
        if len(upnp_device_hints) > 0:
            resources_acquired = True

        if resources_acquired:
            cls.landscape.activate_integration_point("coordinator/upnp", cls.create_coordinator)
        else:
            errmsg = "The required UPNP resources were not configured."
            raise AKitConfigurationError(errmsg)

        return

    @classmethod
    def attach_to_framework(cls, landscape: "Landscape"):
        """
            This API is called so that the IntegrationMixIn can attach to the test framework and participate with
            registration processes.  This allows the framework to ignore the bringing-up of mixins that are not being
            included by a test.
        """
        super(UpnpCoordinatorIntegration, cls).attach_to_framework(landscape)
        cls.landscape.register_integration_point("coordinator/upnp", cls)
        return

    @classmethod
    def collect_resources(cls):
        """
            This API is called so the `IntegrationMixIn` can connect with a resource management
            system and gain access to the resources required for the automation run.

            :raises :class:`akit.exceptions.AKitResourceError`:
        """
        return

    @classmethod
    def create_coordinator(cls, landscape: "Landscape") -> object:
        """
            This API is called so that the landscape can create a coordinator for a given integration role.
        """
        cls.coordinator = UpnpCoordinator(landscape)
        return cls.coordinator

    @classmethod
    def declare_precedence(cls) -> int:
        """
            This API is called so that the IntegrationMixIn can declare an ordinal precedence that should be
            utilized for bringing up its integration state.
        """
        # We need to call the base class, it sets the 'logger' member
        super(UpnpCoordinatorIntegration, cls).declare_precedence()
        return

    @classmethod
    def diagnostic(cls, diag_level: int, diag_folder: str):
        """
            The API is called by the :class:`akit.sequencer.Sequencer` object when the automation sequencer is
            building out a diagnostic package at a diagnostic point in the automation sequence.  Example diagnostic
            points are:

            * pre-run
            * post-run

            Each diagnostic package has its own storage location so derived :class:`akit.scope.ScopeMixIn` objects
            can simply write to their specified output folder.

            :param diag_level: The maximum diagnostic level to run dianostics for.
            :param diag_folder: The output folder path where the diagnostic information should be written.
        """

        return

    @classmethod
    def establish_connectivity(cls, allow_missing_devices: bool=False, upnp_recording: bool = False) -> Tuple[List[str], dict]:
        """
            This API is called so the `IntegrationMixIn` can establish connectivity with any compute or storage
            resources.

            :returns: A tuple with a list of error messages for failed connections and dict of connectivity
                      reports for devices devices based on the coordinator.
        """
        
        upnp_hint_table = cls.landscape.get_upnp_device_config_lookup_table()
        
        if len(upnp_hint_table) == 0:
            raise AKitSemanticError("we should not have been called if the upnp device config had 0 devices.")

        requiredlist = None
        if not allow_missing_devices:
            requiredlist = [usn for usn in upnp_hint_table.keys()]

        found_device_results, matching_device_results, missing_device_results = cls.coordinator.startup_scan(
            upnp_hint_table, watchlist=upnp_hint_table, requiredlist=requiredlist, exclude_interfaces=["lo"], upnp_recording=upnp_recording)

        conn_results = {
            "upnp": {
                "found": found_device_results,
                "matching": matching_device_results,
                "missing": missing_device_results
            }
        }

        conn_errors = []

        return (conn_errors, conn_results)

    @classmethod
    def establish_presence(cls) -> Tuple[List[str], dict]:
        """
            This API is called so the `IntegrationMixIn` can establish presence with any compute or storage
            resources.

            :returns: A tuple with a list of error messages for failed connections and dict of connectivity
                      reports for devices devices based on the coordinator.
        """
        return

    def checkout_upnp_device(self, usn):
        """
            Checkout a device from the device pool by USN.
        """
        codev = None

        if usn in self.upnp_devices_pool:
            codev = self.upnp_devices_pool.pop(usn)
            self.upnp_devices_inuse[usn] = codev

        return codev

    def checkin_upnp_device(self, codev):
        """
            Checkin a device to the device pool.
        """
        usn = codev["USN"]

        if usn in self.upnp_devices_inuse:
            codev = self.upnp_devices_inuse.pop(usn)
            self.upnp_devices_pool[usn] = codev

        return

    
