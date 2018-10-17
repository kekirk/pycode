#-*- coding: utf8 -*-
import xlrd

fname = 'E:/pycode/data/crm_data.xlsx'
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
# print (shxrange)
try:
    sh = bk.sheets()[1]
except:
    print ("no sheet in %s named Sheet1" % fname)
#获取行数
nrows = sh.nrows
#获取列数
ncols = sh.ncols
print ("nrows %d, ncols %d" % (nrows,ncols))
#获取首行
row_value1 = sh.row_values(0,5,ncols)
print (row_value1)