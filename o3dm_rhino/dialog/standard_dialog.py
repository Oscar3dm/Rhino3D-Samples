import Eto.Drawing as drawing
import Eto.Forms as forms

class StandardDialog(forms.Dialog[bool]):
	'''This contains standard boilerplate for ETO modal dialogs, as well as some helper functions'''
	def __init__(self, title):
		#super().__init__()
		#All dialogs need Title, Padding, Resizable
		self.Title = title
		self.Padding = drawing.Padding(10)
		self.Resizable = True
		
		#Create the default button
		self.DefaultButton = forms.Button()
		self.DefaultButton.Text = 'OK'
		self.DefaultButton.Click += self.OnOKButtonClick
		
		#Create the abort button
		self.AbortButton = forms.Button()
		self.AbortButton.Text = 'Cancel'
		self.AbortButton.Click += self.OnCloseButtonClick
		
		#Create Dynamic Layout to place gridview and button row
		self.layout = forms.DynamicLayout()
		self.layout.Spacing = drawing.Size(5,5)
		
	#Class functions
	def OnCloseButtonClick(self, sender, e):
		self.Close(False)
		
	def OnOKButtonClick(self, sender, e):
		self.Close(True)

	def create_layout(self, include_buttons=True):
		if include_buttons:
			self.layout.AddRow(self.DefaultButton, self.AbortButton)
		self.layout.Create()
		self.Content = self.layout

	#Control Creation Helpers
	def create_field(self, value):
		textbox = forms.TextBox(Text=value)
		return textbox

	def create_radio(self, options):
		radio = forms.RadioButtonList()
		radio.DataStore = options
		radio.Orientation = forms.Orientation.Vertical
		radio.SelectedIndex = 0
		return radio

	def create_dropdown(self, options):
		dropdown = forms.DropDown()
		dropdown.DataStore = options
		dropdown.SelectedIndex = 0
		return dropdown
	
	def create_checklist(self, options):
		checkbox_list = forms.CheckBoxList()
		checkbox_list.DataStore = options
		checkbox_list.Orientation = forms.Orientation.Vertical
		return checkbox_list
	
	def get_control_value(self, control):
		if isinstance(control, forms.TextBox):
			return control.Text
		elif isinstance(control, forms.RadioButtonList):
			index = control.SelectedIndex
			value = control.DataStore[index]
			return value
		elif isinstance(control, forms.DropDown):
			index = control.SelectedIndex
			value = control.DataStore[index]
			return value
		elif isinstance(control, forms.CheckBoxList):
			return [x for x in control.SelectedKeys]
		else:
			print('No value found for control type')
			return None
	
