import xlrd
import datetime
excel= xlrd.open_workbook(r'C:\Users\1234\Desktop\工作计划.xlsx','rb')
print(excel.sheet_names())
print(excel.sheets()[0])
table=excel.sheets()[0]
row= table.nrows
print("行数：%d"%row)
ncols = table.ncols
print("列：%d"%ncols)
cell_A1 = table.cell(66,3).value
a=xlrd.xldate_as_tuple(cell_A1,0)
b=xlrd.xldate_as_datetime(cell_A1,0)
print(cell_A1)
print(a[0])
print(type(b))
import time
print(b)
print(type(datetime.datetime.now().time()))
print(time.time())
# for i in range(row):
#     for j in range(ncols):
#         print(table.cell(i,j).value)