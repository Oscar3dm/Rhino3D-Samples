import os
from o3dm_rhino.dynamic_importer import dynamic_module_import

# Get the directory of the current file (__init__.py)
module_path = os.path.dirname(__file__)
module_name = 'o3dm_rhino.geometry'

dynamic_module_import(module_path, module_name, globals())