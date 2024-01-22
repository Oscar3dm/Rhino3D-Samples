import Rhino as rc

def get_surface_from_doc_object(obj, match_boundary = False):
	surface = None
	if isinstance(obj, rc.DocObjects.BrepObject):
		Brep = obj.BrepGeometry
		surfaces = Brep.Surfaces
		faces = Brep.Faces
		#This Brep is surface-like with one Brep face and no trimming curves
		if Brep.IsSurface:
			surface = faces[0].DuplicateSurface()
		#This surface could be larger than the trimmed BREP face boundary
		elif surfaces.Count == 1 and not match_boundary:
			surface = surfaces[0]
	elif isinstance(obj, rc.DocObjects.SurfaceObject):
		surface = obj.SurfaceGeometry
	return surface