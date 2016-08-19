
from os.path import join
from xlrd import open_workbook
from xlutils.copy import copy


def motify():
    rb = open_workbook(join('/home/qianxu/vir_folder/read_excel', 'file.xls'), formatting_info=True, on_demand=True)
    nrows = rb.sheet_by_index(0).nrows  # 行数
    wb = copy(rb)
    nrows -= 1
    while nrows>0:
        str1 = '1' + str(int(rb.sheet_by_index(0).cell(nrows, 0).value))
        wb.get_sheet(0).write(nrows, 0, str1)
        nrows -= 1
    wb.save(join('/home/qianxu/vir_folder/read_excel/data', 'file.xls'))


if __name__ == '__main__':
    motify()