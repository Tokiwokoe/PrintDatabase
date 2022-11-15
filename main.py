import sys
import connection
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem
from UIclass import AdminWindow


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


class AdminWindow(PrintTable, AdminWindow.Ui_MainWindow):
    def __init__(self):
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
        self.Print_prod_name.clicked.connect(self.to_print_prod_name)
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
        self.DeleteButton.clicked.connect(self.to_delete)
