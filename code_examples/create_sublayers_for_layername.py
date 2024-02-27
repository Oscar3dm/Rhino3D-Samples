import Rhino as rc
import rhinoscriptsyntax as rs
from o3dm_rhino.get_layers_with_name import get_layers_with_name
from o3dm_rhino.create_sublayer import create_sublayer

doc = rc.RhinoDoc.ActiveDoc
layertable = doc.Layers

#Ask user for a layer with the name to replace, then ask the user for the new name
layerpath = rs.GetLayer("Select layer with name to create sublayers for")
new_layername = rs.StringBox("Enter new sublayer name")
#Get the name of the layer from the full path
layername = layerpath.split("::")[-1]
#Search the document for layers with the same name
match_layers = get_layers_with_name(doc, layername)

#-- Option 1: RhinoCommon Add Layer
for layer in match_layers:
	create_sublayer(doc, layer, new_layername)

#-- Option 2: RhinoScriptSyntax Add Layer
#for layer in match_layers:
#	new_layerpath = layer.FullPath + "::" + new_layername
#	rs.AddLayer(new_layerpath)