from PyQt5.QtWidgets import QDialog
from UIclass import DeleteMessage, DeleteData
import connection


class DeleteMessage(QDialog, DeleteMessage.Ui_Dialog):
    def __init__(self):
        super(DeleteMessage, self).__init__()
        self.setupUi(self)
        self.setFixedSize(560, 150)
        self.cursor = connection.connection.cursor()
        query = f'SELECT * FROM {table} WHERE id = {id}'
        self.cursor.execute(query)
        self.text.setText(f'Вы действительно хотите удалить {self.cursor.fetchall()}')
        self.OKbutton.clicked.connect(self.delete)
        self.CancelButton.clicked.connect(self.cancel)

    def delete(self):
        try:
            query = f'DELETE FROM {table} WHERE id = {id}'
            self.cursor.execute(query)
            connection.connection.commit()
            self.error.setText('Удалено!')
        except Exception as err:
            print(err)
            self.error.setText('Ошибка!')

    def cancel(self):
        self.close()


class DeleteData(QDialog, DeleteData.Ui_Dialog):
    def __init__(self):
        super(DeleteData, self).__init__()
        self.setupUi(self)
        self.setFixedSize(450, 150)
        self.table.addItem('Типографии')
        self.table.addItem('Заказчики')
        self.table.addItem('Изделия')
        self.table.addItem('Формат листов')
        self.table.addItem('Заказы')
        self.table.addItem('Районы')
        self.table.addItem('Тип собственности')
        self.table.addItem('Вид изделия')
        self.OKbutton.clicked.connect(self.to_delete)
        self.cursor = connection.connection.cursor()

    def to_delete(self):
        global id
        id = self.id.text()
        global table
        if self.table.currentText() == 'Типографии':
            table = '"Print"'
        elif self.table.currentText() == 'Заказчики':
            table = '"Customer"'
        elif self.table.currentText() == 'Изделия':
            table = '"Product"'
        elif self.table.currentText() == 'Формат листов':
            table = '"PaperFormat"'
        elif self.table.currentText() == 'Заказы':
            table = '"Order"'
        elif self.table.currentText() == 'Районы':
            table = '"District"'
        elif self.table.currentText() == 'Вид изделия':
            table = '"ProductType"'
        elif self.table.currentText() == 'Тип собственности':
            table = '"PropertyType"'
        message = DeleteMessage()
        message.exec_()
