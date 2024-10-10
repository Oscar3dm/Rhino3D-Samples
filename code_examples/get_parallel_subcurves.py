import Rhino as rc
import rhinoscriptsyntax as rs
from o3dm_rhino.geometry.bake_geometry import bake_geometry
from o3dm_rhino.geometry.parallel_subcurves_from_curve import parallel_subcurves_from_curve
	
doc = rc.RhinoDoc.ActiveDoc
objecttable = doc.Objects

curve_ids = rs.GetObjects()
curves = [objecttable.FindId(x).Geometry for x in curve_ids]
line_points = rs.GetLine()
filter_line = rc.Geometry.Line(line_points[0], line_points[-1])
filter_vector = filter_line.Direction

parallel_subcurves = []
for curve in curves:
	parallel_subcurves.extend(parallel_subcurves_from_curve(curve, filter_vector))

[bake_geometry(x) for x in parallel_subcurves]