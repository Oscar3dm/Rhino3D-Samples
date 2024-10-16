import pickle
import copy
import Rhino.Geometry as rg
import Rhino.FileIO as rfi
import Rhino.Runtime as rr

def clean_data(data):
	"""Recursively replaces instances of Rhino.Geometry objects with their JSON representations."""
	if isinstance(data, rg.GeometryBase):
		json_data = data.ToJSON(rfi.SerializationOptions())
		return json_data
	elif isinstance(data, dict):
		return {k: clean_data(v) for k, v in data.items()}
	elif isinstance(data, list):
		return [clean_data(v) for v in data]
	elif isinstance(data, tuple):
		return tuple(clean_data(v) for v in data)
	elif hasattr(data, '__dict__'):
		try:
			new_obj = data.__class__()
		except:
			new_obj = copy.copy(data)
		for attr in vars(data):
			setattr(new_obj, attr, clean_data(getattr(data, attr)))
		return new_obj
	else:
		return data

def reconstruct_data(data):
    """Recursively reconstructs Rhino.Geometry objects from their JSON representations."""
    if isinstance(data, str):
        try:
            geometry = rr.CommonObject.FromJSON(data)
            if geometry is not None:
                return geometry
            else:
                return data  # Not a geometry JSON string
        except:
            return data  # Not a valid JSON string for geometry
    elif isinstance(data, dict):
        return {k: reconstruct_data(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [reconstruct_data(v) for v in data]
    elif isinstance(data, tuple):
        return tuple(reconstruct_data(v) for v in data)
    elif hasattr(data, '__dict__'):
        new_obj = data.__class__()
        for attr in vars(data):
            setattr(new_obj, attr, reconstruct_data(getattr(data, attr)))
        return new_obj
    else:
        return data

def save_data(data, file_path):
	"""Saves the cleaned data structure to a text file after pickling."""
	cleaned_data = clean_data(data)
	with open(file_path, 'wb') as file:
		pickle.dump(cleaned_data, file)

def load_data(file_path):
	"""Loads the pickled data from a text file and reconstructs the Rhino.Geometry objects."""
	with open(file_path, 'rb') as file:
		data = pickle.load(file)
	reconstructed_data = reconstruct_data(data)
	return reconstructed_data