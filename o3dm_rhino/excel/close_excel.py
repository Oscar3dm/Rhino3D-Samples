import System

def close_excel(excel_app, workbook, save_file=False):
	workbook.Close(save_file)
	excel_app.Quit()
	System.Runtime.InteropServices.Marshal.ReleaseComObject(workbook)
	System.Runtime.InteropServices.Marshal.ReleaseComObject(excel_app)