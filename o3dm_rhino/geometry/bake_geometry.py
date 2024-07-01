import Rhino as rc
import rhinoscriptsyntax as rs

def bake_geometry(geo, layerpath="Debug"):
	#Get document information
	doc = rc.RhinoDoc.ActiveDoc
	objecttable = doc.Objects
	layertable = doc.Layers
	
	#Find layer if it exists. Make one if not
	layer_i = layertable.FindByFullPath(layerpath, -1)
	if layer_i == -1:
		rs.AddLayer(layerpath)
		layer_i = layertable.FindByFullPath(layerpath, -1)
	
	#Create object attributes and bake geometry
	geo_attr = rc.DocObjects.ObjectAttributes()
	geo_attr.LayerIndex = layer_i
	geo_Id = objecttable.Add(geo, geo_attr)
	return geo_Id


