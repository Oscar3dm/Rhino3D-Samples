def extend_curve(curve, curve_end, extension, extension_type):
	if extension >= 0:
		curve = curve.Extend(curve_end, extension, extension_type)
	else:
		extension = -extension
		curve = curve.Trim(curve_end, extension)
	return curve