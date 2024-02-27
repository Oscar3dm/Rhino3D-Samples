def create_sublayer(doc, parent_layer, sublayer_name):
	import Rhino as rc

	layertable = doc.Layers
	#Make sure layer doesn't exist
	new_layerpath = parent_layer.FullPath + "::" + sublayer_name
	new_layer_i = layertable.FindByFullPath(new_layerpath, -1)
	if new_layer_i != -1:
		new_layer = layertable.FindIndex(new_layer_i)
		if not new_layer.IsDeleted:
			print('Layer already exists: ' + new_layer.FullPath)
			return new_layer
	#Create the sublayer
	new_layer = rc.DocObjects.Layer.GetDefaultLayerProperties()
	new_layer.Name = sublayer_name
	new_layer.ParentLayerId = parent_layer.Id
	new_layer_i = layertable.Add(new_layer)
	return new_layer
