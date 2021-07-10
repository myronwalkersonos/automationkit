
import os

from akit.exceptions import AKitSemanticError

from akit.testing.testplus.testjob import DefaultTestJob as DefaultTestJobTestPlus
from akit.testing.unittest.testjob import DefaultTestJob as DefaultTestJobUnitTest

class TestRootType:
    TESTPLUS = "testplus"
    UNITTEST = "unittest"

def lookup_default_test_job_type(test_root):
    def_job_type = None

    test_root_type = lookup_test_root_type(test_root)

    if test_root_type == TestRootType.TESTPLUS:
        def_job_type = DefaultTestJobTestPlus
    elif test_root_type == TestRootType.UNITTEST:
        def_job_type = DefaultTestJobUnitTest
    else:
        errmsg = "No default test job type for nknown test root type '{}'.".format(test_root_type)
        raise AKitSemanticError(errmsg)

    return def_job_type

def lookup_test_root_type(test_root):

    test_root_module = os.path.join(test_root, os.path.join("__init__.py"))
    if not os.path.exists(test_root_module):
        errmsg = "The test root must have a module '__init__.py'. testroot={}".format(test_root_module)
        raise AKitSemanticError(errmsg)

    ROOT_TYPE = None

    trm_content = ""
    with open(test_root_module, 'r') as trmf:
        trm_content = trmf.read().strip()

    locals_vars = {}
    exec(trm_content, None, locals_vars)
    if "ROOT_TYPE" in locals_vars:
        ROOT_TYPE = locals_vars["ROOT_TYPE"]

    if ROOT_TYPE is None:
        errmsg = "The test root module must have a 'ROOT_TYPE' variable specifying (testplus, unittest).".format(test_root_module)
        raise AKitSemanticError(errmsg)

    if not ((ROOT_TYPE == TestRootType.TESTPLUS) or (ROOT_TYPE == TestRootType.UNITTEST)):
        errmsg = "Unknow test root type {}".format(ROOT_TYPE)
        raise AKitSemanticError(errmsg)

    return ROOT_TYPE
