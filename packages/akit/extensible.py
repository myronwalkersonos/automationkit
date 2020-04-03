
import inspect
import os

from akit.compat import import_by_name

class LoadableExtension:
    """
        Marks a class as an extension for collection purposes so we can distinguish
        extension classes from base classes
    """
    pass

def collect_extensions_under_module(module, ext_base_type):

    ext_collection = []

    # This is declare here so it can be used as a closure
    nxtmod = None

    def is_extension_class(obj):
        result = False

        if inspect.isclass(obj):
            obj_module = obj.__module__
            if obj_module == nxtmod.__name__ and LoadableExtension in obj.__bases__:
                result = issubclass(obj, ext_base_type) and obj is not ext_base_type
        return result

    module_name = module.__name__
    module_dir = os.path.dirname(module.__file__).rstrip(os.sep)
    module_parts = module_name.split(".")
    module_root = os.sep.join(module_dir.split(os.sep)[:-len(module_parts)])
    rootlen = len(module_root)

    for dirpath, dirnames, filenames in os.walk(module_dir):
        leafdir = dirpath[rootlen:].lstrip(os.sep)
        leafmodule = leafdir.replace(os.sep, ".")
        for nxtfile in filenames:
            nfbase, nfext = os.path.splitext(nxtfile)
            if nfext != ".py":
                continue

            nxtmodname = "%s.%s" % (leafmodule, nfbase)
            nxtmod = import_by_name(nxtmodname)
            if nxtmod is None:
                continue

            ext_collection.extend(inspect.getmembers(nxtmod, predicate=is_extension_class))

    return ext_collection