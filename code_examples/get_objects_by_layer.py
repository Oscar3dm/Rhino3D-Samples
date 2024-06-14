import Rhino as rc

doc = rc.RhinoDoc.ActiveDoc
layertable = doc.Layers
objecttable = doc.Objects

layer_i = layertable.FindByFullPath("Div Line", -1)
layer = layertable.FindIndex(layer_i)
objects = objecttable.FindByLayer(layer)
#Get a single object
object = objects[0]
geometry = object.Geometry