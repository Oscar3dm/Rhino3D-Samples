def points_distance_along_vector(point1, point2, measure_vector):
	"""Calculate the distance between two points along a given vector."""
	vector_between_points = point2 - point1
	#Unitize the measurement vector
	measure_vector.Unitize()
	#Get the dot product between the vectors
	dot_product = vector_between_points * measure_vector
	distance = abs(dot_product)

	return distance