
from sqlalchemy import create_engine

from akit.exceptions import AKitConfigurationError, AKitNotOverloadedError

from akit.xlogging.foundations import getAutomatonKitLogger

logger = getAutomatonKitLogger()

class DatabaseConnectionFactory:
    def create_engine(self, *, dbname=None, echo=True):
        errmsg = "The 'create_engine' method must be overloaded by 'DatabaseConnectionFactory' derived types."
        raise AKitNotOverloadedError(errmsg)

class BasicDatabaseConnectionFactory(DatabaseConnectionFactory):

    def __init__(self, profile_name, *, conntype: str, dbtype:str, username: str, password: str, dbname: str=None):
        self.profile_name = profile_name
        self.conntype = conntype
        self.dbtype = dbtype
        self.username = username
        self.password = password
        self.dbname = dbname
        return

    def create_engine(self, *, dbname=None, echo=True):
        # TODO: Implement pipe based DB connection engine creation
        return

class BasicTcpDatabaseConnectionFactory(DatabaseConnectionFactory):

    def __init__(self, profile_name, *, conntype: str, dbtype:str, host: str, port: int, username: str, password: str, dbname: str=None):
        self.profile_name = profile_name
        self.conntype = conntype
        self.dbtype = dbtype
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.dbname = dbname
        return

    def create_engine(self, *, dbname=None, echo=True):

        if dbname is None and self.dbname is not None:
            dbname = self.dbname

        if dbname is None:
            warnmsg = "BasicTcpDatabaseConnectionFactory.create_engine: dbname was None."
            logger.warn(warnmsg)

        connstr = '%s://%s:%s@%s:%d/%s' % (
            self.dbtype, self.username, self.password, self.host, self.port, dbname)
        dbengine = create_engine(connstr, echo=echo)

        return dbengine

database_connection_factories = {}

def lookup_database_connection_factory(conn_profile: str):

    global database_connection_factories

    conn_factory = None

    if conn_profile in database_connection_factories:
        conn_factory = database_connection_factories[conn_profile]
    else:
        from akit.environment.context import Context

        ctx = Context()
        
        conn_info = None

        rcdatabases = ctx.lookup("/environment/configuration/databases")
        if rcdatabases is not None and conn_profile in rcdatabases:
            conn_info = rcdatabases[conn_profile].value
        else:
            from akit.integration.landscaping.landscape import Landscape

            lscape = Landscape()
            lsdatabases = lscape.databases
            if lsdatabases is not None and conn_profile in lsdatabases:
                conn_info = lsdatabases[conn_profile]

        if conn_info is not None:
            if "conntype" in conn_info:
                conntype = conn_info["conntype"].lower()
                if conntype == "basic":
                    conn_factory = BasicDatabaseConnectionFactory(conn_profile, **conn_info)
                elif conntype == "basic-tcp":
                    conn_factory = BasicTcpDatabaseConnectionFactory(conn_profile, **conn_info)
                else:
                    errmsg = "Unknown database connection type. connection={} conntype={}".format(
                        conn_profile, conntype)
                    raise AKitConfigurationError(errmsg)

                database_connection_factories[conn_profile] = conn_factory
            else:
                errmsg = "Database connection entries must have a 'conntype' entry. connection={}".format(
                    conn_profile
                )
                raise AKitConfigurationError(errmsg)
        else:
            errmsg = "Database connection not found. connection={}".format(
                conn_profile
            )
            raise AKitConfigurationError(errmsg)

    return conn_factory