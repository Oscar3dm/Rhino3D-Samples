import Rhino as rc
import rhinoscriptsyntax as rs
from o3dm_rhino.geometry import get_object_area

doc = rc.RhinoDoc.ActiveDoc
layertable = doc.Layers
objecttable = doc.Objects

#Get layer objects on the default layer, or path of your choice
layer_i = layertable.FindByFullPath('Default', -1)
layer = layertable[layer_i]
r_objects = objecttable.FindByLayer(layer)

areas = []
for r_object in r_objects:
	area = get_object_area(r_object)
	areas.append(area)