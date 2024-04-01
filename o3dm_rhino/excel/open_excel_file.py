import rhinoscriptsyntax as rs
import clr
clr.AddReferenceByName('Microsoft.Office.Interop.Excel, Version=11.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c')
from Microsoft.Office.Interop import Excel

def open_excel_file(filepath):
	excel_app = Excel.ApplicationClass()   
	excel_app.Visible = False
	excel_app.DisplayAlerts = False 

	workbook = excel_app.Workbooks.Open(filepath)

	return excel_app, workbook