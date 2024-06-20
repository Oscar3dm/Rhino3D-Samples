import Rhino as rc

def curve_length_at(curve, t):
	curve_domain = curve.Domain
	domain_start = curve_domain.Min
	domain_end = curve_domain.Max
	if t < domain_start:
		raise ValueError("curve parameter is less than start of curve domain")
	if t > domain_end:
		raise ValueError("curve parameter is greater than end of curve domain")
	sub_domain = rc.Geometry.Interval(domain_start, t)
	length = curve.GetLength(sub_domain)
	return length