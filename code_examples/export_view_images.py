from o3dm_rhino.standard_dialog import StandardDialog
from o3dm_rhino.export_named_view import export_named_view
import Rhino as rc
import rhinoscriptsyntax as rs
import Eto.Forms as forms
import os

class ExportViewDialog(StandardDialog):
	def __init__(self):
		super(ExportViewDialog, self).__init__('Select Views')
		#Create checklist of view names
		doc = rc.RhinoDoc.ActiveDoc
		viewtable = doc.NamedViews
		view_names = [x.Name for x in viewtable]
		self.view_checklist = self.create_checklist(view_names)
		#Add layout rows for our checklist
		self.layout.AddRow('View Names')
		self.layout.AddRow(self.view_checklist)
		#Create button for close
		close_button = forms.Button(Text = 'Close')
		close_button.Click += self.OnCloseButtonClick
		#Create button for export
		export_button = forms.Button(Text = 'Export')
		export_button.Click += self.OnExportButtonClick
		#Add last row with close and export buttons. Instantiate layout
		self.layout.AddRow(close_button, export_button)
		self.create_layout(include_buttons=False)

	def OnCloseButtonClick(self, sender, e):
		return self.Close(True)
	
	def OnExportButtonClick(self, sender, e):
		export_views = self.get_control_value(self.view_checklist)
		doc_folder = rs.DocumentPath()
		export_folder = rs.BrowseForFolder(doc_folder, 'Select Export Folder', 'Export Folder')
		if export_folder:
			for view_name in export_views:
				file_path = os.path.join(export_folder, view_name + '.png')
				export_named_view(view_name, file_path)

dialog = ExportViewDialog()
dialog_rc = dialog.ShowModal(rc.UI.RhinoEtoApp.MainWindow)