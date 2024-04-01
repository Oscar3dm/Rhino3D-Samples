import o3dm_rhino.excel.open_excel_file as open_excel_file
import o3dm_rhino.excel.close_excel as close_excel
import traceback

excel_filepath = r"C:\Users\ofern\OneDrive\Documents\Test.xlsx"
excel_app, workbook = open_excel_file(excel_filepath)
#We need to make sure excel is closed properly. All logic should be handled using try/finally
try:
    worksheet = workbook.Worksheets[1]
    worksheet_range = worksheet.UsedRange
    #Rows and Columns are 1-based index
    for row_i in range(1, worksheet_range.Rows.Count + 1):
        for col_i in range(1, worksheet_range.Columns.Count + 1):
            cell = worksheet.Cells(row_i, col_i)
            #Read Cell Value
            print(cell.Value2)
            #Write Cell Value
            cell.Value2 = 'Test'
except Exception as e:
    error_message = traceback.format_exc()
    print(error_message)
finally:
    close_excel(excel_app, workbook, save_file=True)