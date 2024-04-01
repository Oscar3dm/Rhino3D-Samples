def create_excel_file(filepath):
	import rhinoscriptsyntax as rs
	import clr
	import traceback
	clr.AddReferenceByName('Microsoft.Office.Interop.Excel, Version=11.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c')
	from Microsoft.Office.Interop import Excel
	import close_excel.close_excel as close_excel

	result = False
	try:
		excel_app = Excel.ApplicationClass()   
		excel_app.Visible = False
		excel_app.DisplayAlerts = False
		workbook = excel_app.Workbooks.Add()
		workbook.SaveAs(filepath)
		result = True
	except Exception as e:
		error_message = traceback.format_exc()
		print(error_message)
	finally:
		close_excel(excel_app, workbook)
		return result