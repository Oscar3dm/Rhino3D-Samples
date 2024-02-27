import Rhino as rc
import rhinoscriptsyntax as rs
from o3dm_rhino.get_layers_with_name import get_layers_with_name

doc = rc.RhinoDoc.ActiveDoc
layertable = doc.Layers

#Ask user for a layer with the name to replace, then ask the user for the new name
layerpath = rs.GetLayer("Select layer with name to replace")
new_layername = rs.StringBox("Enter new layer name")
#Get the name of the layer from the full path
layername = layerpath.split("::")[-1]
#Search the document for layers with the same name
match_layers = get_layers_with_name(doc, layername)

for layer in match_layers:
    layer.Name = new_layername