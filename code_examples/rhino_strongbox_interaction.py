import Rhino as rc
import System
import clr

doc = rc.RhinoDoc.ActiveDoc
layertable = doc.Layers
objecttable = doc.Objects

layer_i = layertable.FindByFullPath('Default', -1)
layer = layertable[layer_i]
layer_objects = objecttable.FindByLayer(layer)
#Filter layer geometry for curves using list comprehension
curves = [x.Geometry for x in layer_objects if isinstance(x.Geometry, rc.Geometry.Curve)]
#Convert the python list to a System.Array for the Rhino Common function
curves_array = System.Array[rc.Geometry.Curve](curves)
#Create a StrongBox object for the error code
error_code_SB = clr.StrongBox[int](0)

surface = rc.Geometry.NurbsSurface.CreateNetworkSurface(curves_array,0,0.01,0.01,0.01,error_code_SB)

#Extract error code from the StrongBox
error_code = error_code_SB.Value