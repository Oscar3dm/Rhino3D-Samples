import Rhino as rc
from o3dm_rhino.geometry.extend_curve import extend_curve

#-- GH/Python inputs: curve, extension_type (int), start_extension, end_extension

#Convert extension_type integer to Enum type
extension_type = rc.Geometry.CurveExtensionStyle(extension_type)
#Extend start of curve
curve_end = rc.Geometry.CurveEnd.Start
curve = extend_curve(curve, curve_end, start_extension, extension_type)
#Extend end of curve
curve_end = rc.Geometry.CurveEnd.End
curve = extend_curve(curve, curve_end, end_extension, extension_type)
