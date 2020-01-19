
# Reading an excel file using Python
from __future__ import print_function

import xlrd

from os.path import join, dirname, abspath
import xlrd

fname = join(dirname(dirname(abspath(__file__))), 'test_data', 'C:/Users/sidha/Downloads/List_of_restrooms.xlsx')

xl_workbook = xlrd.open_workbook(fname)
sheet_names = xl_workbook.sheet_names()
print('Sheet Names', sheet_names)

xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])
xl_sheet = xl_workbook.sheet_by_index(0)
print ('Sheet name: %s' % xl_sheet.name)

