def parallel_subcurves_from_curve(curve, vector):
	subcurves = curve.DuplicateSegments() #This could be .GetSubCurves() in Rhino 8
	parallel_subcurves = []
	for subcurve in subcurves:
		if not subcurve.IsLinear():
			continue
		start_t = subcurve.Domain.T0
		subcurve_vector = subcurve.TangentAt(start_t)
		if subcurve_vector.IsParallelTo(vector, 0.01) in [-1,1]:
			parallel_subcurves.append(subcurve)
	return parallel_subcurves

