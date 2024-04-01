import glob
import os

def dynamic_module_import(module_path, module_name, target_globals):
	# Loop through all .py files in the directory
	for file in glob.glob(os.path.join(module_path, "*.py")):
		# Skip __init__.py to avoid recursive imports
		if file == os.path.join(module_path, '__init__.py'):
			continue
		# Extract module name from the file path
		submodule_name = os.path.splitext(os.path.basename(file))[0]
		full_module_name = module_name + '.' + submodule_name

		# Dynamic import with __import__
		module = __import__(full_module_name, globals(), locals(), ['*'], -1)

		# Import all names from the module into the current namespace
		names = [name for name in dir(module) if not name.startswith('_')]
		target_globals.update({name: getattr(module, name) for name in names})