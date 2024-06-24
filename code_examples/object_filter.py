import rhinoscriptsyntax as rs
import Rhino as rc

def select_filter(rhino_object, geometry, component_index):
	if not isinstance(geometry, rc.Geometry.Brep):
		return False
	volume = geometry.GetVolume()
	if volume < 10000:
		return False
	return True
	
object_Ids = rs.GetObjects(custom_filter = select_filter)


