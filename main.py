import sys
import connection
import generator
import openpyxl
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem

from DeleteClass import DeleteData
from UIclass import AdminWindow, OK
from AddClass import AddClient, AddDistrict, AddProperty, AddPrint, AddFormat, AddOrder, AddProduct, AddProductType


# Класс вывода данных из БД в таблицу
class PrintTable(QMainWindow):
    def __init__(self):
        super(PrintTable, self).__init__()

    def to_print_table(self):
        i = 0
        for elem in self.rows:
            j = 0
            for t in elem:
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(t).strip()))
                j += 1
            i += 1
        i = 0
        self.tableWidget.resizeColumnsToContents()

    def to_print_print(self):
        self.cursor = connection.connection.cursor()
        ok.exec_()
        query = 'SELECT name, "PropertyType".property, "District".district, address, phone, year FROM "Print" ' \
                'LEFT JOIN "District" ON "District".id = "Print".district ' \
                'LEFT JOIN "PropertyType" ON "PropertyType".id = "Print".property ' \
                'ORDER BY "Print".id LIMIT ' + str(rows)
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(6)
        self.labels = ['Название типографии', 'Тип собственности', 'Район', 'Адрес', 'Телефон', 'Год открытия']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_customer(self):
        self.cursor = connection.connection.cursor()
        ok.exec_()
        query = 'SELECT name, address, birthday, phone ' \
                'FROM "Customer" ORDER BY "Customer".id LIMIT ' + str(rows)
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(4)
        self.labels = ['ФИО', 'Адрес', 'Дата рождения', 'Телефон']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_product(self):
        self.cursor = connection.connection.cursor()
        ok.exec_()
        query = 'SELECT publication, list_count, calculation, price, "ProductType".product, "Density".density, "PaperType".type FROM "Product" ' \
                'LEFT JOIN "ProductType" ON "ProductType".id = "Product".type ' \
                'LEFT JOIN "Density" ON "Density".id = "Product".density ' \
                'LEFT JOIN "PaperType" ON "PaperType".id = "Product".paper_type ' \
                'ORDER BY "Product".id LIMIT ' + str(rows)
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(7)
        self.labels = ['Название изделия', 'Количество страниц', 'Тираж', 'Цена за экземпляр', 'Тип изделия', 'Плостность бумаги', 'Тип бумаги']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_format(self):
        self.cursor = connection.connection.cursor()
        ok.exec_()
        query = 'SELECT density FROM "Density" ORDER BY "Density".id LIMIT ' + str(rows)
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(1)
        self.labels = ['Плотность бумаги']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_paper(self):
        self.cursor = connection.connection.cursor()
        ok.exec_()
        query = 'SELECT type FROM "PaperType" ORDER BY "PaperType".id LIMIT ' + str(rows)
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(1)
        self.labels = ['Тип бумаги']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_dist(self):
        self.cursor = connection.connection.cursor()
        ok.exec_()
        query = 'SELECT district FROM "District" ORDER BY "District".id LIMIT ' + str(rows)
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(1)
        self.labels = ['Название района']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_order(self):
        self.cursor = connection.connection.cursor()
        ok.exec_()
        query = 'SELECT "Customer".name, "Product".publication, date_start, date_plan, date_fact, cost ' \
                'FROM "Order" ' \
                'LEFT JOIN "Product" ON "Product".id = "Order".product ' \
                'LEFT JOIN "Customer" ON "Customer".id = "Order".client ORDER BY "Order".id LIMIT ' + str(rows)
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(6)
        self.labels = ['ФИО заказчика', 'Название изделия', 'Дата взятия заказа', 'Дата завершения (план)', 'Дата завершения (факт)', 'Аванс']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_prop(self):
        self.cursor = connection.connection.cursor()
        ok.exec_()
        query = 'SELECT property FROM "PropertyType" ORDER BY "PropertyType".id LIMIT ' + str(rows)
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(1)
        self.labels = ['Тип собственности']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_prod_type(self):
        self.cursor = connection.connection.cursor()
        ok.exec_()
        query = 'SELECT product FROM "ProductType" ORDER BY "ProductType".id LIMIT ' + str(rows)
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(1)
        self.labels = ['Тип изделия']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_8_1(self):
        self.cursor = connection.connection.cursor()
        ok.exec_()
        query = 'SELECT name, "District".district, year, phone FROM "Print" ' \
                'INNER JOIN "District" ON "District".id = "Print".district ' \
                'WHERE "Print".id > 3 LIMIT ' + str(rows)
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(4)
        self.labels = ['Название типографии', 'Район', 'Год открытия', 'Телефон']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_8_2(self):
        self.cursor = connection.connection.cursor()
        ok.exec_()
        query = 'SELECT name, "District".district, year, phone FROM "Print" ' \
                'INNER JOIN "District" ON "District".id = "Print".district ' \
                'WHERE "District".id > 1 LIMIT ' + str(rows)
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(4)
        self.labels = ['Название типографии', 'Район', 'Год открытия', 'Телефон']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_8_3(self):
        self.cursor = connection.connection.cursor()
        ok.exec_()
        query = 'SELECT name, date_start FROM "Order" ' \
                'INNER JOIN "Customer" ON "Customer".id = "Order".client ' \
                'WHERE birthday BETWEEN \'15.05.1997\' AND \'29.12.2000\' LIMIT ' + str(rows)
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(2)
        self.labels = ['ФИО', 'Дата рождения']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_8_4(self):
        self.cursor = connection.connection.cursor()
        ok.exec_()
        query = 'SELECT name, date_start FROM "Order" ' \
                'INNER JOIN "Customer" ON "Customer".id = "Order".client ' \
                'WHERE date_start < \'15.07.2022\' LIMIT ' + str(rows)
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(2)
        self.labels = ['ФИО', 'Дата заказа']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_8_5(self):
        self.cursor = connection.connection.cursor()
        ok.exec_()
        query = 'SELECT name, phone, "PropertyType".property FROM "Print" ' \
                'INNER JOIN "PropertyType" ON "PropertyType".id = "Print".property LIMIT ' + str(rows)
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(3)
        self.labels = ['Название типографии', 'Телефон', 'Тип собственности']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_8_6(self):
        self.cursor = connection.connection.cursor()
        ok.exec_()
        query = 'SELECT name, "Order".id FROM "Customer" ' \
                'INNER JOIN "Order" ON "Order".client = "Customer".id LIMIT ' + str(rows)
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(2)
        self.labels = ['ФИО', 'ID заказа']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_8_7(self):
        self.cursor = connection.connection.cursor()
        ok.exec_()
        query = 'SELECT name, "District".district, address FROM "Print" ' \
                'INNER JOIN "District" ON "District".id = "Print".district LIMIT ' + str(rows)
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(3)
        self.labels = ['Название типографии', 'Район', 'Адрес']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_8_8(self):
        self.cursor = connection.connection.cursor()
        ok.exec_()
        query = 'SELECT name, "Order".id FROM "Customer" ' \
                'LEFT JOIN "Order" ON "Order".client = "Customer".id LIMIT ' + str(rows)
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(2)
        self.labels = ['ФИО', 'ID заказа']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_8_9(self):
        self.cursor = connection.connection.cursor()
        ok.exec_()
        query = 'SELECT name, "Order".id FROM "Customer" ' \
                'RIGHT JOIN "Order" ON "Order".client = "Customer".id LIMIT ' + str(rows)
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(2)
        self.labels = ['ФИО', 'ID заказа']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_8_10(self):
        self.cursor = connection.connection.cursor()
        ok.exec_()
        query = 'SELECT "Print".id, name, "District".district FROM "Print" ' \
                'LEFT JOIN "District" ON "District".id = "Print".district ' \
                'WHERE "District".district = ' \
                '(SELECT DISTINCT district FROM "District" WHERE district LIKE \'В%\') LIMIT ' + str(rows)
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(3)
        self.labels = ['ID типографии', 'Название типографии', 'Район']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_9_1(self):
        self.cursor = connection.connection.cursor()
        ok.exec_()
        query = 'SELECT name, COUNT("Order".id) AS total_orders FROM "Customer" ' \
                'LEFT JOIN "Order" ON "Order".client = "Customer".id ' \
                'GROUP BY name ' \
                'ORDER BY total_orders DESC LIMIT ' + str(rows)
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(2)
        self.labels = ['ФИО', 'Количество заказов']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_9_2(self):
        self.cursor = connection.connection.cursor()
        ok.exec_()
        query = 'SELECT name, COUNT("Order".id) AS total_orders FROM "Customer" ' \
                'LEFT JOIN "Order" ON "Order".client = "Customer".id ' \
                'WHERE name LIKE \'К%\' GROUP BY name ' \
                'ORDER BY total_orders DESC LIMIT ' + str(rows)
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(2)
        self.labels = ['ФИО', 'Количество заказов']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_9_3(self):
        self.cursor = connection.connection.cursor()
        ok.exec_()
        query = 'SELECT name, COUNT("Order".id) AS total_orders FROM "Customer" ' \
                'LEFT JOIN "Order" ON "Order".client = "Customer".id ' \
                'GROUP BY name ' \
                'HAVING COUNT("Order".id) > 1 ' \
                'ORDER BY total_orders DESC LIMIT ' + str(rows)
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(2)
        self.labels = ['ФИО', 'Количество заказов']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_9_4(self):
        self.cursor = connection.connection.cursor()
        ok.exec_()
        query = 'SELECT name, COUNT("Order".id) AS total_orders FROM "Customer" ' \
                'LEFT JOIN "Order" ON "Order".client = "Customer".id ' \
                'WHERE name LIKE \'К%\' ' \
                'GROUP BY name ' \
                'HAVING COUNT("Order".id) < 2 ' \
                'ORDER BY total_orders DESC LIMIT ' + str(rows)
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(2)
        self.labels = ['ФИО', 'Количество заказов']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_9_5(self):
        self.cursor = connection.connection.cursor()
        ok.exec_()
        query = 'SELECT "Customer".id, COUNT("Order".id) AS order_count FROM "Customer" ' \
                'LEFT JOIN "Order" ON "Order".client = "Customer".id ' \
                'GROUP BY "Customer".id ' \
                'HAVING COUNT("Order".id) = ' \
                '(SELECT COUNT("Order".id) AS order_count FROM "Customer" ' \
                'GROUP BY order_count ' \
                'HAVING COUNT("Order".id) = 1) LIMIT ' + str(rows)
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(2)
        self.labels = ['ID заказчика', 'Количество заказов']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_9_6(self):
        self.cursor = connection.connection.cursor()
        ok.exec_()
        query = 'SELECT name, publication, price FROM "Product" ' \
                'LEFT JOIN "Order" ON "Order".product = "Product".id ' \
                'LEFT JOIN "Customer" ON "Customer".id = "Order".client ' \
                'WHERE EXISTS ' \
                '(SELECT name FROM "Customer" ' \
                'WHERE "Customer".id = 2) ' \
                'ORDER BY price DESC LIMIT ' + str(rows)
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(3)
        self.labels = ['ФИО', 'Название изделия', 'Стоимость']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()


# Класс главного окна
class AdminWindow(PrintTable, AdminWindow.Ui_MainWindow):
    def __init__(self):
        """ Установка интерфейса, фиксация размера и соединение кнопок с функциями"""
        super(AdminWindow, self).__init__()
        self.setupUi(self)
        self.setFixedSize(1050, 1000)
        self.Print_print.clicked.connect(self.to_print_print)
        self.Print_customer.clicked.connect(self.to_print_customer)
        self.Print_product.clicked.connect(self.to_print_product)
        self.Print_density.clicked.connect(self.to_print_format)
        self.Print_density_2.clicked.connect(self.to_print_paper)
        self.Print_dist.clicked.connect(self.to_print_dist)
        self.Print_order.clicked.connect(self.to_print_order)
        self.Print_prop.clicked.connect(self.to_print_prop)
        self.Print_prod_type.clicked.connect(self.to_print_prod_type)
        self.Q_3_8_1.clicked.connect(self.to_print_Q_3_8_1)
        self.Q_3_8_2.clicked.connect(self.to_print_Q_3_8_2)
        self.Q_3_8_3.clicked.connect(self.to_print_Q_3_8_3)
        self.Q_3_8_4.clicked.connect(self.to_print_Q_3_8_4)
        self.Q_3_8_5.clicked.connect(self.to_print_Q_3_8_5)
        self.Q_3_8_6.clicked.connect(self.to_print_Q_3_8_6)
        self.Q_3_8_7.clicked.connect(self.to_print_Q_3_8_7)
        self.Q_3_8_8.clicked.connect(self.to_print_Q_3_8_8)
        self.Q_3_8_9.clicked.connect(self.to_print_Q_3_8_9)
        self.Q_3_8_10.clicked.connect(self.to_print_Q_3_8_10)
        self.Q_3_9_1.clicked.connect(self.to_print_Q_3_9_1)
        self.Q_3_9_2.clicked.connect(self.to_print_Q_3_9_2)
        self.Q_3_9_3.clicked.connect(self.to_print_Q_3_9_3)
        self.Q_3_9_4.clicked.connect(self.to_print_Q_3_9_4)
        self.Q_3_9_5.clicked.connect(self.to_print_Q_3_9_5)
        self.Q_3_9_6.clicked.connect(self.to_print_Q_3_9_6)
        self.add_customer.clicked.connect(self.to_add_customer)
        self.add_dist.clicked.connect(self.to_add_dist)
        self.add_prop.clicked.connect(self.to_add_prop)
        self.add_print.clicked.connect(self.to_add_print)
        self.add_density.clicked.connect(self.to_add_format)
        self.add_order.clicked.connect(self.to_add_order)
        self.add_product.clicked.connect(self.to_add_product)
        self.add_prod_type.clicked.connect(self.to_add_prod_type)
        self.DeleteButton.clicked.connect(self.to_delete)
        self.generate_customer.clicked.connect(self.to_generate_customer)
        self.generate_print.clicked.connect(self.to_generate_print)
        self.generate_product.clicked.connect(self.to_generate_product)
        self.generate_dist.clicked.connect(self.to_generate_dist)
        self.generate_prop.clicked.connect(self.to_generate_prop)
        self.generate_order.clicked.connect(self.to_generate_order)
        self.generate_prod_type.clicked.connect(self.to_generate_prod_type)
        self.generate_density.clicked.connect(self.to_generate_density)
        self.generate_paper.clicked.connect(self.to_generate_paper_type)
        self.excel.clicked.connect(self.export)

    def export(self):
        self.cursor = connection.connection.cursor()
        book = openpyxl.Workbook()
        sheet = book.active
        self.cursor.execute('SELECT name, COUNT("Order".id) AS total_orders FROM "Customer" LEFT JOIN "Order" ON "Order".client = "Customer".id GROUP BY name ORDER BY total_orders DESC')
        results = self.cursor.fetchall()
        i = 0
        for row in results:
            i += 1
            j = 1
            for col in row:
                cell = sheet.cell(row=i, column=j)
                cell.value = col
                j += 1
        book.save("Q_3_9_1.xlsx")

    def to_add_customer(self):
        client = AddClient()
        client.exec_()

    def to_add_dist(self):
        dist = AddDistrict()
        dist.exec_()

    def to_add_prop(self):
        prop = AddProperty()
        prop.exec_()

    def to_add_print(self):
        print = AddPrint()
        print.exec_()

    def to_add_format(self):
        format = AddFormat()
        format.exec_()

    def to_add_order(self):
        order = AddOrder()
        order.exec_()

    def to_add_product(self):
        prod = AddProduct()
        prod.exec_()

    def to_add_prod_type(self):
        prod_type = AddProductType()
        prod_type.exec_()

    def to_delete(self):
        delete = DeleteData()
        delete.exec_()

    def to_generate_customer(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT id FROM "Customer" ORDER BY id DESC LIMIT 1'
        self.cursor.execute(query)
        self.id = self.cursor.fetchone()
        try:
            query = generator.generate_customer(self.id)
            self.cursor.execute(query)
            connection.connection.commit()
            self.gen_label.setText('Генерация заказчиков завершена')
        except Exception as err:
            print(err)
            self.gen_label.setText('Ошибка')

    def to_generate_print(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT id FROM "Print" ORDER BY id DESC LIMIT 1'
        self.cursor.execute(query)
        self.id = self.cursor.fetchone()
        query = 'SELECT id FROM "District" ORDER BY id DESC LIMIT 1'
        self.cursor.execute(query)
        self.dist = self.cursor.fetchone()
        query = 'SELECT id FROM "PropertyType" ORDER BY id DESC LIMIT 1'
        self.cursor.execute(query)
        self.prop = self.cursor.fetchone()
        try:
            query = generator.generate_print(self.id, self.dist, self.prop)
            self.cursor.execute(query)
            connection.connection.commit()
            self.gen_label.setText('Генерация типографий завершена')
        except Exception as err:
            print(err)
            self.gen_label.setText('Ошибка')

    def to_generate_product(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT id FROM "Product" ORDER BY id DESC LIMIT 1'
        self.cursor.execute(query)
        self.id = self.cursor.fetchone()
        query = 'SELECT id FROM "Density" ORDER BY id DESC LIMIT 1'
        self.cursor.execute(query)
        self.density = self.cursor.fetchone()
        query = 'SELECT id FROM "PaperType" ORDER BY id DESC LIMIT 1'
        self.cursor.execute(query)
        self.paper = self.cursor.fetchone()
        query = 'SELECT id FROM "ProductType" ORDER BY id DESC LIMIT 1'
        self.cursor.execute(query)
        self.type = self.cursor.fetchone()
        try:
            query = generator.generate_product(self.id, self.density, self.paper, self.type)
            self.cursor.execute(query)
            connection.connection.commit()
            self.gen_label.setText('Генерация изделий завершена')
        except Exception as err:
            print(err)
            self.gen_label.setText('Ошибка')

    def to_generate_density(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT id FROM "Density" ORDER BY id DESC LIMIT 1'
        self.cursor.execute(query)
        self.id = self.cursor.fetchone()
        try:
            query = generator.generate_density(self.id)
            self.cursor.execute(query)
            connection.connection.commit()
            self.gen_label.setText('Генерация плотности бумаги завершена')
        except Exception as err:
            print(err)
            self.gen_label.setText('Ошибка')

    def to_generate_paper_type(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT id FROM "PaperType" ORDER BY id DESC LIMIT 1'
        self.cursor.execute(query)
        self.id = self.cursor.fetchone()
        try:
            query = generator.generate_paper_type(self.id)
            self.cursor.execute(query)
            connection.connection.commit()
            self.gen_label.setText('Генерация типа бумаги завершена')
        except Exception as err:
            print(err)
            self.gen_label.setText('Ошибка')

    def to_generate_dist(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT id FROM "District" ORDER BY id DESC LIMIT 1'
        self.cursor.execute(query)
        self.id = self.cursor.fetchone()
        try:
            query = generator.generate_dist(self.id)
            self.cursor.execute(query)
            connection.connection.commit()
            self.gen_label.setText('Генерация районов завершена')
        except Exception as err:
            print(err)
            self.gen_label.setText('Ошибка')

    def to_generate_prop(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT id FROM "PropertyType" ORDER BY id DESC LIMIT 1'
        self.cursor.execute(query)
        self.id = self.cursor.fetchone()
        try:
            query = generator.generate_prop(self.id)
            self.cursor.execute(query)
            connection.connection.commit()
            self.gen_label.setText('Генерация собственности завершена')
        except Exception as err:
            print(err)
            self.gen_label.setText('Ошибка')

    def to_generate_order(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT id FROM "Order" ORDER BY id DESC LIMIT 1'
        self.cursor.execute(query)
        self.id = self.cursor.fetchone()
        query = 'SELECT id FROM "Customer" ORDER BY id DESC LIMIT 1'
        self.cursor.execute(query)
        self.cust = self.cursor.fetchone()
        query = 'SELECT id FROM "Product" ORDER BY id DESC LIMIT 1'
        self.cursor.execute(query)
        self.prod = self.cursor.fetchone()
        try:
            query = generator.generate_order(self.id, self.cust, self.prod)
            self.cursor.execute(query)
            connection.connection.commit()
            self.gen_label.setText('Генерация изделий завершена')
        except Exception as err:
            print(err)
            self.gen_label.setText('Ошибка')

    def to_generate_prod_type(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT id FROM "ProductType" ORDER BY id DESC LIMIT 1'
        self.cursor.execute(query)
        self.id = self.cursor.fetchone()
        try:
            query = generator.generate_prod_type(self.id)
            self.cursor.execute(query)
            connection.connection.commit()
            self.gen_label.setText('Генерация собственности завершена')
        except Exception as err:
            print(err)
            self.gen_label.setText('Ошибка')


class OK(QDialog, OK.Ui_Dialog):
    def __init__(self):
        super(OK, self).__init__()
        self.setupUi(self)
        self.setFixedSize(560, 150)
        self.OKbutton.clicked.connect(self.correct_data)

    def correct_data(self):
        self.cursor = connection.connection.cursor()
        global rows
        rows = self.rows.text()
        if str(rows).strip().isalnum() and 0 < int(rows) < 1000001:
            self.close()
        else:
            self.error.setText('Проверьте корректность заполнения полей!')


# Запуск программы
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdminWindow()
    ok = OK()

    window.show()
    sys.exit(app.exec_())
