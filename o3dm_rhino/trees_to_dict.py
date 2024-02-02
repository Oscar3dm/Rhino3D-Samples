import Rhino as rc

def format_data_item(item):
	'''Formats a data item to a dict or string representation.
	Currently handles points and vectors.'''
	def point_to_dict(point):
		item_dict = {}
		item_dict['X'] = point.X
		item_dict['Y'] = point.Y
		item_dict['Z'] = point.Z
		return item_dict
	if isinstance(item, rc.Geometry.Point3d):
		item_entry = point_to_dict(item)
	elif isinstance(item, rc.Geometry.Vector3d):
		item_entry = point_to_dict(item)
	else:
		item_entry = str(item)
	return item_entry

def trees_to_dict(keys, data, is_list_types):
	'''Converts a data tree to a dictionary.'''
	dict = {}
	#check that the input lists are the same length
	if not (len(keys) == len(data.Branches) == len(is_list_types)):
		raise ValueError("keys, data.Branches, and is_list_types must all be of the same length.")
	#iterate through the lists and convert to dictionary
	for key, branch, is_list_type in zip(keys, data.Branches, is_list_types):
		data_entry = [format_data_item(item) for item in branch]
		if not is_list_type:
			data_entry = data_entry[0] if data_entry else None  
		dict[key] = data_entry
	return dict