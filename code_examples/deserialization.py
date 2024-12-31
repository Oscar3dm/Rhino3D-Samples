import Rhino as rc
import rhinoscriptsyntax as rs
import OESLib.data as data
import OESLib.va_utilities as va_utils
import jsonpickle

object_id = rs.GetObject()
links = data.get_link_directory()
takedown_dict = data.read_takedown_data(links)
td_obj_dict = takedown_dict[str(object_id)]

component_dict = td_obj_dict['load_components'][0]
