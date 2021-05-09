"""
.. module:: coordinatormixin
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the :class:`CoordinatorMixIn` class and associated reflection methods.
        The :class:`CoordinatorMixIn` derived classes can be used to integraton automation resources and roles
        into the test environment.

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

import inspect

from akit.xlogging.foundations import getAutomatonKitLogger

from akit.exceptions import AKitNotOverloadedError
from akit.mixins.integration import IntegrationMixIn

class CoordinatorMixIn(IntegrationMixIn):
    """
        The :class:`CoordinatorMixIn` object serves as the base object for the declaration of an
        automation integration coordinator mixin.
    """

    coordinator = None

    @classmethod
    def create_coordinator(cls) -> object:
        """
            This API is called so that the landscape can create a coordinator for a given coordinator
            integration role.
        """
        raise AKitNotOverloadedError("This method must be overridden by derived coordinator classes.")