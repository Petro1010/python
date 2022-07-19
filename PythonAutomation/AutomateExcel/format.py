from openpyxl import load_workbook
from openpyxl.styles import Font

wb = load_workbook('barchart.xlsx')
sheet = wb['Report']


sheet['A1'] = 'Sales Report'
sheet['A2'] = 'January'

sheet['A1'].font = Font('Arial', bold=True, size=20)
sheet['A2'].font = Font('Arial', size=15)

wb.save('barchart.xlsx')