import Rhino as rc
import rhinoscriptsyntax as rs
import o3dm_rhino.data.serialization as ser

doc = rc.RhinoDoc.ActiveDoc
objecttable = doc.Objects

#Get Geometry
doc_object_id = rs.GetObject()
doc_object = objecttable.FindId(doc_object_id)
doc_geometry = doc_object.Geometry

#Create Geometry
line = rc.Geometry.LineCurve(rc.Geometry.Line(rc.Geometry.Point3d(0,0,0), rc.Geometry.Point3d(10,0,0)))

# Create a dictionary with nested objects
data_dict = {
    'doc_geometry': doc_geometry,
    'line': line
}

# Serialize the dictionary and save
file_path = r"C:\Users\ofern\Desktop\geometry_data.pkl"  # Replace with the actual path you want to save the file to
ser.save_data(data_dict, file_path)

