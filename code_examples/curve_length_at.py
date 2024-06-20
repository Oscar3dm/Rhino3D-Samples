from o3dm_rhino.geometry.curve_length_at import curve_length_at
from o3dm_rhino.geometry.get_layerpath_objects import get_layerpath_objects

curve_object = get_layerpath_objects("GH Reference::Curve")[0]
curve = curve_object.Geometry
point_object = get_layerpath_objects("GH Reference::Point")[0]
point = point_object.Geometry
point_3d = point.Location

closest_point, curve_t = curve.ClosestPoint(point_3d)
length = curve_length_at(curve, curve_t)
print(length)

