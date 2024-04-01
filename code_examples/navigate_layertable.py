import Rhino as rc
import rhinoscriptsyntax as rs
import System

#Get the document and layertable
doc = rc.RhinoDoc.ActiveDoc
layertable = doc.Layers

#Get a layer by its full path
layerpath = 'Layer::Sublayer 1'
layer_i = layertable.FindByFullPath(layerpath, -1)
if layer_i == -1:
    rs.MessageBox('Layer not found\n' + layerpath)
layer = layertable.FindIndex(layer_i)

#--Examples of what you can do with the layer

#--Rename the layer
#layer.Name = 'New Layer Name'

#--Delete the layer and geometry in that layer
#layertable.Purge(layer_i, False)

#--Select objects on the layer
#objecttable = doc.Objects
#layer_objects = objecttable.FindByLayer(layer)
#object_Ids_enum = System.Collections.Generic.List[System.Guid]([x.Id for x in layer_objects])
#objecttable.Select(object_Ids_enum, True)

#--Select objects on the layer (2)
#rs.ObjectsByLayer(layerpath, True)

#--Move the layer to a new parent
#new_parent_path = 'Layer::Sublayer 2'
#new_parent_i = layertable.FindByFullPath(new_parent_path, -1)
#new_parent_layer = layertable.FindIndex(new_parent_i)
#new_parent_layer_Id = new_parent_layer.Id
#layer.ParentLayerId = new_parent_layer_Id