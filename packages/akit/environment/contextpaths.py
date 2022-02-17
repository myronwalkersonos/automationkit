
from enum import Enum

class ContextPaths(str, Enum):
    BUILD_BRANCH = "/environment/build/branch"
    BUILD_FLAVOR = "/environment/build/flavor"
    BUILD_NAME = "/environment/build/name"

    CONFIG_FILE_CREDENTIALS = "/configuration/paths/credentials"
    CONFIG_FILE_LANDSCAPE = "/configuration/paths/landscape"
    CONFIG_FILE_RUNTIME = "/configuration/paths/runtime"
    CONFIG_FILE_TOPOLOGY = "/configuration/paths/topology"
    CONFIG_FILE_USER = "/configuration/paths/user"

    DATABASES = "/configuration/databases"

    FILE_RESULTS_TEMPLATE = "/configuration/results-configuration/html-template"

    DIR_RESULTS_RESOURCE_DEST = "/configuration/results-configuration/static-resource-dest-dir"
    DIR_RESULTS_RESOURCE_SRC = "/configuration/results-configuration/static-resource-src-dir"

    DEBUG_BREAKPOINTS = "/configuration/breakpoints"
    DEBUG_DEBUGGER = "/configuration/debugger"

    LOGGING_LEVEL_CONSOLE = "/configuration/logging/levels/console"
    LOGGING_LEVEL_LOGFILE = "/configuration/logging/levels/logfile"

    JOB_TYPE = "/environment/jobtype"
    OUTPUT_DIRECTORY = "/environment/output_directory"
    RUNID = "/environment/runid"
    STARTTIME = "/environment/starttime"

    SKIPPED_DEVICES = "/configuration/skip-devices"

    TESTROOT = "/configuration/testroot"

    TIMETRAVEL = "/configuration/timetravel"
    TIMEPORTALS = "/configuration/timetravel"

    UPNP_LOGGED_EVENTS = "/configuration/networking/upnp/subscriptions/logged-events"