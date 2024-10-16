import Rhino as rc
import o3dm_rhino.data.serialization as ser
from o3dm_rhino.geometry.bake_geometry import bake_geometry

#Read data
file_path = r"C:\Users\ofern\Desktop\geometry_data.pkl" 
data = ser.load_data(file_path)

#Get values by data keys
doc_geometry = data['doc_geometry']

#Test output
bake_geometry(doc_geometry)