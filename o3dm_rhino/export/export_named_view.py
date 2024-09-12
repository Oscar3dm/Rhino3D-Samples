import rhinoscriptsyntax as rs
import Rhino as rc
import scriptcontext as sc
import System.Drawing

def export_named_view(view_name, file_path, width=None, height=None, bbox=None, selected=False):
    is_current_view = rs.RestoreNamedView(view_name)
    if not is_current_view:
        raise Exception("Named view not found.")
    view = sc.doc.Views.ActiveView
    if bbox:
        sc.doc.Views.ActiveView.ActiveViewport.ZoomBoundingBox(bbox)
    view_capture = rc.Display.ViewCapture()
    #view_capture.DrawSelectedObjectsOnly = selected
    view_capture.Width = width or view.ActiveViewport.Size.Width
    view_capture.Height = height or view.ActiveViewport.Size.Height
    view_capture.ScaleScreenItems = False
    view_capture.DrawAxes = False
    view_capture.DrawGrid = False
    view_capture.DrawGridAxes = False
    view_capture.TransparentBackground = True
    bitmap = view_capture.CaptureToBitmap(view)
    if bitmap:
        bitmap.Save(file_path, System.Drawing.Imaging.ImageFormat.Png)