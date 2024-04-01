import Rhino as rc

def get_object_area(r_object):
	#convert geometry to brep or break loop
	if isinstance(r_object.Geometry, rc.Geometry.Brep):
		brep = r_object.Geometry
	elif isinstance(r_object.Geometry, rc.Geometry.Extrusion):
		brep = r_object.Geometry.ToBrep(True)
	elif isinstance(r_object.Geometry, rc.Geometry.Surface):
		brep = rc.Geometry.Brep.CreateFromSurface(r_object.Geometry)
	else:
		print('Object is not a brep or surface')
		return None
	#find area of BREP
	area = brep.GetArea()
	return area