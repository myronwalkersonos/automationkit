"""
.. module:: akit.datum.dbio
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Contains helper functions for working with specific databases

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


import traceback

from sqlalchemy import create_engine

from akit.datum.orm import AutomationPod

def database_exists(username, password, dbname):
    engine = create_engine('postgresql://%s:%s@localhost:5432/postgres' % (username, password), echo=True)
    result = engine.execute("SELECT 1 AS result FROM pg_database WHERE datname='%s'" % dbname)
    return result.rowcount > 0


def database_create(username, password, dbname):
    engine = create_engine('postgresql://%s:%s@localhost:5432/postgres' % (username, password), echo=True)

    conn = engine.connect()
    try:
        conn.connection.set_isolation_level(0)
        result = conn.execute("CREATE DATABASE %s" % dbname)
    except Exception as xcpt:
        print(traceback.format_exc())
        raise
    finally:
        conn.close()

    return

def create_apod_postgresql_database(host='localhost', port=5432, username=None, password=None):

    if not database_exists(username, password, "apod"):
        database_create(username, password, "apod")

    engine = create_engine('postgresql://%s:%s@localhost:5432/apod' % (username, password), echo=True)

    AutomationPod.metadata.create_all(engine, checkfirst=True)

    return

def open_apod_postgresql_database(host='localhost', port=5432, username=None, password=None):
    
    create_apod_postgresql_database(host=host, port=port, username=username, password=password)

    connstr = 'postgresql://'
    if username is not None:
        connstr += username

    if password is not None:
        connstr += ":%s" % password
    
    connstr += "%s@:%d/apod" % (host, port)

    engine = create_engine(connstr, echo=True)

    return engine

if __name__ == "__main__":
    from akit.integration.landscaping import Landscape
    landscape = Landscape()

    dbinfo = landscape.get_databases()

    apoddb_info = dbinfo["apod"]
    open_apod_postgresql_database(**apoddb_info)