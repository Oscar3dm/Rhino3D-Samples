import Rhino as rc

def get_layerpath_objects(layerpath):
	doc = rc.RhinoDoc.ActiveDoc
	layertable = doc.Layers
	objecttable = doc.Objects
	
	layer_i = layertable.FindByFullPath(layerpath, -1)
	if layer_i == -1:
		raise Exception("No layer found: " + layerpath)
	layer = layertable.FindIndex(layer_i)
	objects = objecttable.FindByLayer(layer)
	if not objects:
		raise Exception("No objects found on layer: " + layerpath)
	return objects