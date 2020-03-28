"""
.. module:: akit.environment.options
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that contains the :class:`Context` object and :class:`ContextCursor` that
               are used to maintain the shared automation context.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@automationmojo.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = ""

import argparse

from akit.xlogging import LEVEL_NAMES

ENVIRONMENT_OPTIONS = [
    (("-o", "--output"), { "dest":"output", "action":"store", "default":None, "help":"The output directory where results and artifacts are collected."}),
    (("--console-level",), { "dest":"consolelevel", "action":"store", "default":"INFO", "choices":LEVEL_NAMES, "help":"The logging level for console output."}),
    (("--logfile-level",), { "dest":"logfilelevel", "action":"store", "default":"DEBUG", "choices":LEVEL_NAMES, "help":"The logging level for logfile output."})
]

def process_environment_options():
    """
        Processes the basic automation kit environment commandline options which
        are used to configure the base automation functionality such as:

        * output directory
        * console log level
        * logfile log level
    """
    env_parser = argparse.ArgumentParser()
    for opt_args, opt_kwargs in ENVIRONMENT_OPTIONS:
        env_parser.add_argument(*opt_args, **opt_kwargs)

    args, unknown = env_parser.parse_known_args()

    output_dir = args.output
    console_level = args.consolelevel
    logfile_level = args.logfilelevel

    return output_dir, console_level, logfile_level
