import Rhino as rc
import sys
import os
#Make sure parent folder of o3dm_rhino is in your Rhino Module Search Paths
from o3dm_rhino.geometry import get_surface_from_doc_object

doc = rc.RhinoDoc.ActiveDoc
layertable = doc.Layers
objecttable = doc.Objects

#Get layer objects on the default layer, or path of your choice
layer_i = layertable.FindByFullPath('Default', -1)
layer = layertable[layer_i]
layer_objects = objecttable.FindByLayer(layer)
#Filter layer geometry for surface types. Alternatively, you can rely on the function to return None if the object does not contain a surface
surface_doc_types = (rc.DocObjects.BrepObject, rc.DocObjects.BrepObject)
surface_objects = [x for x in layer_objects if isinstance(x, surface_doc_types)]
surfaces = []
for surface_object in surface_objects:
	surface = get_surface_from_doc_object(surface_object, match_boundary = True)
	if surface:
		surfaces.append(surface)

print(surfaces)
