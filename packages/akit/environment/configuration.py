"""
.. module:: akit.environment.configuration
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that contains the default runtime configration dictionary and the functions that
               are used to load the automation configuration file and overlay the settings on top of the
               default runtime configuration.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@automationmojo.com"
__status__ = "Development" # Prototype, Development or Production
#__license__ = ""

import os

RUNTIME_CONFIGURATION = {
    "version": "1.0.0",
    "logging": {
        "levels": {
            "console": "INFO",
            "logfile": "DEBUG"
        },
        "logname": "%(jobtype)s.log"
    },
    "paths": {
        "runresults": os.sep.join(("~", "aresults", "runresults", "%(starttime)s")),
        "testresults": os.sep.join(("~", "aresults", "testresults", "%(starttime)s"))
    }
}


