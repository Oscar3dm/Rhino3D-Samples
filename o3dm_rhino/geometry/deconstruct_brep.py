import Rhino as rc

def deconstruct_brep(brep):
	"""Takes a brep and returns its faces, vertices, and edges"""
	sub_breps = []
	vertices = []
	edges = []
	for face_i in range(brep.Faces.Count):
		sub_brep = brep.DuplicateSubBrep([face_i])
		sub_breps.append(sub_brep)
	for vertex in brep.Vertices:
		point_3d = vertex.Location
		point = rc.Geometry.Point(point_3d)
		vertices.append(point)
	for edge in brep.Edges:
		edge_curve = edge.EdgeCurve
		edges.append(edge_curve)
	return sub_breps, vertices, edges