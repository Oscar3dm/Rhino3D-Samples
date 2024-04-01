import os
from o3dm_rhino.export import trees_to_dict
from o3dm_rhino.export import write_JSON

'''keys, data, and is_list_types are from the inputs of the grasshopper component'''
dict = trees_to_dict(keys, data, is_list_types)
desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
filepath = os.path.join(desktop, 'Test.JSON')
write_JSON(filepath, dict)