import sys
import connection
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem
from UIclass import AdminWindow


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
        query = 'SELECT name, "PropertyType".property, "District".district, address, phone, year FROM "Print" ' \
                'LEFT JOIN "District" ON "District".id = "Print".district ' \
                'LEFT JOIN "PropertyType" ON "PropertyType".id = "Print".property ' \
                'ORDER BY "Print".id'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(6)
        self.labels = ['Название типографии', 'Тип собственности', 'Район', 'Адрес', 'Телефон', 'Год открытия']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_customer(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT name, address, birthday, phone ' \
                'FROM "Customer" ORDER BY "Customer".id'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(4)
        self.labels = ['ФИО', 'Адрес', 'Дата рождения', 'Телефон']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_product(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT publication, list_count, calculation, price, "ProductType".product FROM "Product" ' \
                'LEFT JOIN "ProductType" ON "ProductType".id = "Product".type ' \
                'ORDER BY "Product".id'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(5)
        self.labels = ['Название изделия', 'Количество страниц', 'Тираж', 'Цена за экземпляр', 'Тип изделия']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_format(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT paper_type, density FROM "PaperFormat" ORDER BY "PaperFormat".id'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(2)
        self.labels = ['Тип бумаги', 'Плотность бумаги']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_dist(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT district FROM "District" ORDER BY "District".id'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(1)
        self.labels = ['Название района']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_order(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT "Customer".name, "Product".publication, date_start, date_plan, date_fact, cost, comment ' \
                'FROM "Order" ' \
                'LEFT JOIN "Product" ON "Product".id = "Order".product ' \
                'LEFT JOIN "Customer" ON "Customer".id = "Order".client ORDER BY "Order".id'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(7)
        self.labels = ['ФИО заказчика', 'Название изделия', 'Дата взятия заказа', 'Дата завершения (план)', 'Дата завершения (факт)', 'Аванс', 'Доп. информация']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_prop(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT property FROM "PropertyType" ORDER BY "PropertyType".id'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(1)
        self.labels = ['Тип собственности']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_prod_type(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT product FROM "ProductType" ORDER BY "ProductType".id'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(1)
        self.labels = ['Тип изделия']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()


# Класс главного окна
class AdminWindow(PrintTable, AdminWindow.Ui_MainWindow):
    def __init__(self):
        """ Установка интерфейса, фиксация размера и соединение кнопок с функциями"""
        super(AdminWindow, self).__init__()
        self.setupUi(self)
        self.setFixedSize(860, 1000)
        self.Print_print.clicked.connect(self.to_print_print)
        self.Print_customer.clicked.connect(self.to_print_customer)
        self.Print_product.clicked.connect(self.to_print_product)
        self.Print_format.clicked.connect(self.to_print_format)
        self.Print_dist.clicked.connect(self.to_print_dist)
        self.Print_order.clicked.connect(self.to_print_order)
        self.Print_prop.clicked.connect(self.to_print_prop)
        self.Print_prod_type.clicked.connect(self.to_print_prod_type)
        """
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
        self.add_order.clicked.connect(self.to_add_order)
        self.add_print.clicked.connect(self.to_add_print)
        self.add_dist.clicked.connect(self.to_add_dist)
        self.add_product.clicked.connect(self.to_add_product)
        self.add_prop.clicked.connect(self.to_add_prop)
        self.add_format.clicked.connect(self.to_add_format)
        self.add_prod_type.clicked.connect(self.to_add_prod_type)
        self.add_prod_name.clicked.connect(self.to_add_prod_name)
        self.DeleteButton.clicked.connect(self.to_delete)"""


# Запуск программы
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdminWindow()

    window.show()
    sys.exit(app.exec_())
