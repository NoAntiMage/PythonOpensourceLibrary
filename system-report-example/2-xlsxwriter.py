# coding: utf-8

import xlsxwriter

workbook = xlsxwriter.Workbook('chart.xlsx')
worksheet = workbook.add_worksheet()
chart = workbook.add_chart({'type': 'column'})
title = [u'星期一', u'星期二', u'星期三', u'星期四', u'星期五', u'星期六', u'星期日']
buname = [u'业务名称', u'新闻中心', u'购物频道', u'体育频道', u'亲子频道']
data = [
    [150,152,158,149,155,145,148],
    [89,88,95,93,98,100,99],
    [201,200,198,175,170,198,150],
    [75,77,78,78,74,70,79],
    [88,85,87,90,93,88,84],
]

format0 = workbook.add_format()
format0.set_border(1)
format_title = workbook.add_format()
format_title.set_border(1)
format_title.set_bg_color('#cccccc')

format_title.set_align('center')
format_title.set_bold()

format_ave = workbook.add_format()
format_ave.set_border(1)
format_ave.set_num_format('0.00')
