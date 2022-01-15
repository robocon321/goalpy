import xlsxwriter

def save():
    workbook = xlsxwriter.Workbook("demo.xlsx")
    worksheet = workbook.add_worksheet()

    worksheet.set_column('A:A', 5)
    worksheet.set_column('B:B', 15)
    worksheet.set_column('C:C', 20)
    worksheet.set_column('D:D', 15)
    worksheet.set_column('E:E', 15)

    bold = workbook.add_format({'bold': True})
    worksheet.write('A1', 'STT', bold)
    worksheet.write('B1', 'MÃ SẢN PHẨM', bold)
    worksheet.write('C1', 'TÊN SẢN PHẨM', bold)

    worksheet.write('A2', 2)
    worksheet.write('B2', 'Sp2')
    worksheet.write('C2', 'Bánh mì')

    worksheet.write('A3', 3)
    worksheet.write('B3', 'Sp3')
    worksheet.write('C3', 'Nước ngọt')

    worksheet.insert_image('B5', './../image/Capture.JPG')
    workbook.close()

def read():
    pass