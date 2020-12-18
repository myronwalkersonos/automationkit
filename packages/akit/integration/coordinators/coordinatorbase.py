"""
.. module:: coordinatorbase
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Contains the CoordinatorBase which is the base object for coordinators to derive from and establishes
               patterns for coordinators which help to make them threadsafe.

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

from typing import List, Optional

import threading
import weakref

from akit.exceptions import AKitNotOverloadedError
from akit.integration.landscaping.landscapedevice import LandscapeDevice
from akit.integration.landscaping.landscapedeviceextension import LandscapeDeviceExtension

from akit.xlogging.foundations import getAutomatonKitLogger

EMPTY_LIST = []

# Declare a literal UpnpFacotry type for use with typing
# to allow for typing without creating circular reference
LITERAL_LANDSCAPE_TYPE = 'akit.integration.landscaping.landscape.Landscape'

class CoordinatorBase:
    """
        The CoordinatorBase utilizes the expected device declarations of type such as 'network/upnp' to establish and maintain
        connectivity and interoperability with a class of devices.  A derived coordinator will scan the medium such as a network
        for the devices declared in the landscape description.  The coordinator will also create the threads necessary to maintain
        communicates with the external devices over the medium.
    """

    instance = None
    initialized = False

    def __new__(cls, *_args, **_kwargs):
        """
            Constructs new instances of the :class:`UpnpCoordinator` object. The
            :class:`UpnpCoordinator` object is a singleton so following instantiations
            of the object will reference the existing singleton
        """

        if cls.instance is None:
            cls.instance = super(CoordinatorBase, cls).__new__(cls)
        return cls.instance

    def __init__(self, lscape: LITERAL_LANDSCAPE_TYPE, *args, **kwargs):
        """
            Constructs an instance of a derived :class:`CoordinatorBase` object.

            :param lscape: The :class:`Landscape` singleton instance.
            :param *args: A pass through for other positional args.
            :param **kwargs: A pass through for the other keyword args.
        """
        this_type = type(self)
        if not this_type.initialized:
            this_type.initialized = True

            self._logger = getAutomatonKitLogger()

            self._lscape_ref = weakref.ref(lscape)

            self._coord_lock = threading.RLock()

            self._cl_children = {}

            self._initialize(*args, **kwargs)
        return

    def _initialize(self, *_args, **_kwargs):
        """
            Called by the CoordinatorBase constructor to perform the one time initialization of the coordinator Singleton
            of a given type.
        """
        # pylint: disable=no-self-use
        raise AKitNotOverloadedError("_initialize: must be overloaded by derived coordinator classes")

    @property
    def children(self) -> List[LandscapeDevice]:
        """
            Returns a list of the devices created by the coordinator and registered by the coordinator with the Landscape object.
        """
        chlist = EMPTY_LIST

        self._coord_lock.acquire()
        try:
            chlist = [c.basedevice for c in self._cl_children.values()]
        finally:
            self._coord_lock.release()

        return chlist

    @property
    def landscape(self):
        """
            Returns a hard reference to the Landscape singleton instance.
        """
        lscape = self._lscape_ref()
        return lscape

    @property
    def children_as_extension(self) -> List[LandscapeDeviceExtension]:
        """
            Returns a list of the device protocol extensions created by this coordinator that have been attached to a landscape device.
        """
        chlist = EMPTY_LIST

        self._coord_lock.acquire()
        try:
            chlist = [c for c in self._cl_children.values()]
        finally:
            self._coord_lock.release()

        return chlist

    def lookup_device_by_key(self, key) -> LandscapeDevice:
        """
            Looks up a device from the list of children by key in a thread safe way.
        """

        found = None

        self._coord_lock.acquire()
        try:
            if key in self._cl_children:
                found = self._cl_children[key].basedevice
        finally:
            self._coord_lock.release()

        return found

    def verify_connectivity(self, cmd: str = "echo 'It Works'", user: Optional[str] = None, raiseerror: bool = True):
        """
            Loops through the nodes in the SSH pool and utilizes the
            credentials for the specified user in order to verify
            connectivity with the remote node.

            :param cmd: A command to run on the remote machine in order
                        to verify that ssh connectivity can be establish.
            :param user: The name of the user credentials to use for connectivity.
                         If the 'user' parameter is not provided, then the
                         credentials of the default or priviledged user will be used.
            :param raiseerror: A boolean value indicating if this API should raise an Exception on failure.

            :returns: A list of errors encountered when verifying connectivity with the devices managed or watched by the coordinator.
        """
        # pylint: disable=no-self-use
        raise AKitNotOverloadedError("verify_connectivity: must be overloaded by derived coordinator classes")
