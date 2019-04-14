from xlwt import Workbook

def write(data_table, data_invoice):
    wb = Workbook()
    sheet = wb.add_sheet('Накладная_' + data_invoice[0] + "_" + data_invoice[1] + '.xls')
    sheet.write(0, 0, "Номер накладной")
    sheet.write(0, 1, data_invoice[0])

    sheet.write(1, 0, "Дата формирования")
    sheet.write(1, 1, data_invoice[1])


    sheet.write(3, 0, "Поезд")
    sheet.write(3, 1, data_invoice[2])

    sheet.write(4, 0, "Вагон")
    sheet.write(4, 1, data_invoice[3])

    sheet.write(5, 0, "Заводской номер")
    sheet.write(5, 1, data_invoice[4])

    sheet.write(8, 1, "Остаток")
    sheet.write(8, 2, "Выдано")
    sheet.write(8, 3, "Сдано исп. (шт.)")
    sheet.write(8, 4, "Сдано неисп. (шт.)")
    sheet.write(8, 5, "Остаток (застил) шт.")
    sheet.write(8, 6, "Принято исп. (шт.)")
    sheet.write(8, 7, "Принято неисп. (шт.)")
    sheet.write(8, 8, "Недостача")

    l = 8;
    row = 0

    sheet.write(row+9, 0, "Книга описи")
    for i in range(0, 8):
        sheet.write(row+9, i + 1, data_table[row*l + i])
    row = row +1

    sheet.write(row+9, 0, "Ковровая дорожка купейная шерсть(1,5*0,65)")
    for i in range(0, 8):
        sheet.write(row+9, i + 1, data_table[row*l + i])
    row = row +1

    sheet.write(row+9, 0, "Комплект бязь, x/б (Рабочий)")
    for i in range(0, 8):
        sheet.write(row+9, i + 1, data_table[row*l + i])
    row = row +1

    sheet.write(row+9, 0, "Комплект купе бязь")
    for i in range(0, 8):
        sheet.write(row+9, i + 1, data_table[row*l + i])
    row = row +1

    sheet.write(row+9, 0, "Матрац ватный")
    for i in range(0, 8):
        sheet.write(row+9, i + 1, data_table[row*l + i])
    row = row +1

    sheet.write(row+9, 0, "Мешок для хранения постельного белья")
    for i in range(0, 8):
        sheet.write(row+9, i + 1, data_table[row*l + i])
    row = row +1

    sheet.write(row+9, 0, "Одеяло синтетическое волокно")
    for i in range(0, 8):
        sheet.write(row+9, i + 1, data_table[row*l + i])
    row = row +1

    sheet.write(row+9, 0, "Подушка синтетическое волокно")
    for i in range(0, 8):
        sheet.write(row+9, i + 1, data_table[row*l + i])
    row = row +1

    sheet.write(row+9, 0, "Полотенце полулен")
    for i in range(0, 8):
        sheet.write(row+9, i + 1, data_table[row*l + i])
    row = row +1

    sheet.write(row+9, 0, "Полотенце х/б")
    for i in range(0, 8):
        sheet.write(row+9, i + 1, data_table[row*l + i])
    row = row +1

    sheet.write(row+9, 0, "Полуштора шелк")
    for i in range(0, 8):
        sheet.write(row+9, i + 1, data_table[row*l + i])
    row = row +1

    sheet.write(row+9, 0, "Салфетка для подоконных столиков полистэр серая")
    for i in range(0, 8):
        sheet.write(row+9, i + 1, data_table[row*l + i])
    row = row +1

    sheet.write(row+9, 0, "Чехол на матрац х/б")
    for i in range(0, 8):
        sheet.write(row+9, i+1, data_table[row*l + i])

    sheet.write(23, 0, "В рейс")
    sheet.write(23, 1, data_invoice[5])

    sheet.write(25, 0, "Выдал")
    sheet.write(25, 1, data_invoice[6])

    sheet.write(26, 0, "Принял экипировщик")
    sheet.write(26, 1, data_invoice[7])

    sheet.write(27, 0, "Принял проводник")
    sheet.write(27, 1, data_invoice[8])
    sheet.write(27, 2, data_invoice[9])

    sheet.write(28, 0, "Принял проводник")
    sheet.write(28, 1, data_invoice[10])
    sheet.write(28, 2, data_invoice[11])

    sheet.write(31, 0, "Из рейса")
    sheet.write(31, 1, data_invoice[12])

    sheet.write(33, 0, "Сдал")
    sheet.write(33, 1, data_invoice[13])
    sheet.write(34, 0, "Принял экипировщик")
    sheet.write(34, 1, data_invoice[14])
    sheet.write(35, 0, "Принял использованное")
    sheet.write(35, 1, data_invoice[15])
    sheet.write(36, 0, "Принял неиспользованное")
    sheet.write(36, 1, data_invoice[16])
    sheet.write(37, 0, "Представитель РЖД")
    sheet.write(37, 1, data_invoice[17])
    sheet.write(38, 0, "ЛНП")
    sheet.write(38, 1, data_invoice[18])

    sheet.write(40, 0, "С недостачей согласен")
    sheet.write(40, 1, data_invoice[19])
    sheet.write(41, 0, "Проводник")
    sheet.write(41, 1, data_invoice[20])

    wb.save('C:/Users/Konver/Desktop/Накладная_' + data_invoice[0] + "_" + data_invoice[1] + '.xls')