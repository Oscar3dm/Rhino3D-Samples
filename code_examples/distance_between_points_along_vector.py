import Rhino as rc
import rhinoscriptsyntax as rs
from o3dm_rhino.geometry.points_distance_along_vector import points_distance_along_vector
	
#Initialize doc
doc = rc.RhinoDoc.ActiveDoc
objecttable = doc.Objects

#Get points from user
point_ids = rs.GetObjects("Select Points to Measure Between")
points_3d = [objecttable.FindId(x).Geometry.Location for x in point_ids]

#Get measurement vector from user
measure_points = rs.GetLine(message1="Pick Points for Measurement Vector")
measure_points = [rc.Geometry.Point3d(x) for x in measure_points]
measure_vector = rc.Geometry.Vector3d(measure_points[1] - measure_points[0])

#Call our function
distance = points_distance_along_vector(points_3d[0], points_3d[1], measure_vector)
print(distance)