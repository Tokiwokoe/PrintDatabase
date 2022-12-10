from PyQt5.QtWidgets import QDialog
from UIclass import AddProp, AddDist, AddClient, AddFormat, AddPrint, AddOrder, AddProduct, AddProductType, AddPaper
import connection


class AddClient(QDialog, AddClient.Ui_Dialog):
    def __init__(self):
        super(AddClient, self).__init__()
        self.setupUi(self)
        self.setFixedSize(740, 140)
        self.OKbutton.clicked.connect(self.correct_data)

    def correct_data(self):
        self.cursor = connection.connection.cursor()
        name = self.name.text()
        birthdate = self.dateEdit.text()
        raw_phone = self.phone.text()
        address = self.addres.text()
        new_phone = raw_phone.replace('+', '').replace('-', '')
        if len(new_phone) == 12:
            phone = '+'
            phone = phone + new_phone[0:2] + '(' + new_phone[2:5] + ')' + new_phone[5:8] + '-' + new_phone[8:10] + '-' + new_phone[10:12]
        else:
            phone = new_phone
        if len(name) == 0 or len(new_phone) == 0 or len(address) == 0:
            self.error.setText('Заполните все поля!')
        elif len(name) > 128 or len(new_phone) > 30 or len(address) > 128:
            self.error.setText('Проверьте корректность заполнения полей!')
        elif name.replace(' ', '').isalpha() and new_phone.strip().isalnum():
            try:
                query = 'SELECT id FROM "Customer" ORDER BY id DESC LIMIT 1'
                self.cursor.execute(query)
                self.id = self.cursor.fetchone()
                query = f"INSERT INTO \"Customer\" VALUES({int(self.id[0])+1}, '{name}', '{address}', '{birthdate}', '{phone}')"
                self.cursor.execute(query)
                connection.connection.commit()
                self.error.setText('Успешно добавлено')
            except Exception as err:
                print(err)
                self.error.setText('Что-то пошло не так :(')
        else:
            self.error.setText('Проверьте корректность заполнения полей!')


class AddDistrict(QDialog, AddDist.Ui_Dialog):
    def __init__(self):
        super(AddDistrict, self).__init__()
        self.setupUi(self)
        self.setFixedSize(560, 150)
        self.OKbutton.clicked.connect(self.correct_data)

    def correct_data(self):
        self.cursor = connection.connection.cursor()
        dist = self.dist.text()
        query = 'SELECT id FROM "District" ORDER BY id DESC LIMIT 1'
        self.cursor.execute(query)
        self.id = self.cursor.fetchone()
        if 0 < len(dist) < 30:
            try:
                query = f"INSERT INTO \"District\" VALUES ({int(self.id[0])+1}, '{dist}')"
                self.cursor.execute(query)
                connection.connection.commit()
                self.error.setText('Успешно добавлено')
            except Exception as err:
                print(err)
                self.error.setText('Что-то пошло не так :(')
        else:
            self.error.setText('Проверьте корректность заполнения полей!')


class AddProperty(QDialog, AddProp.Ui_Dialog):
    def __init__(self):
        super(AddProperty, self).__init__()
        self.setupUi(self)
        self.setFixedSize(560, 150)
        self.OKbutton.clicked.connect(self.correct_data)

    def correct_data(self):
        self.cursor = connection.connection.cursor()
        prop = self.prop.text()
        query = 'SELECT id FROM "PropertyType" ORDER BY id DESC LIMIT 1'
        self.cursor.execute(query)
        self.id = self.cursor.fetchone()
        if 0 < len(prop) < 30:
            try:
                query = f"INSERT INTO \"PropertyType\" VALUES ({int(self.id[0])+1}, '{prop}')"
                self.cursor.execute(query)
                connection.connection.commit()
                self.error.setText('Успешно добавлено')
            except Exception as err:
                print(err)
                self.error.setText('Что-то пошло не так :(')
        else:
            self.error.setText('Проверьте корректность заполнения полей!')


class AddPrint(QDialog, AddPrint.Ui_Dialog):
    def __init__(self):
        super(AddPrint, self).__init__()
        self.setupUi(self)
        self.setFixedSize(740, 140)
        self.OKbutton.clicked.connect(self.correct_data)
        self.cursor = connection.connection.cursor()
        query = 'SELECT id, district FROM "District"'
        self.cursor.execute(query)
        for t in self.cursor.fetchall():
            self.dist.addItem(str(t))
        query = 'SELECT id, property FROM "PropertyType"'
        self.cursor.execute(query)
        for t in self.cursor.fetchall():
            self.prop.addItem(str(t))

    def correct_data(self):
        print = self.print.text()
        year_opened = self.year_opened.text()
        raw_phone = self.phone.text()
        address = self.address.text()
        new_phone = raw_phone.replace('+', '').replace('-', '')
        dist = self.dist.currentText().replace('(', '').replace(')', '').replace(' \'', '\'').split(',')
        dist_id = str(dist[0])
        prop = self.prop.currentText().replace('(', '').replace(')', '').replace(' \'', '\'').split(',')
        prop_id = str(prop[0])
        if 0 < len(print) < 129 and len(new_phone) > 0 and 1900 < int(year_opened) < 2023 and year_opened.isalnum() and new_phone.isalnum() or 129 < len(address) < 1:
            try:
                if len(new_phone) == 12:
                    phone = ''
                    phone = '+' + phone + new_phone[0:2] + '(' + new_phone[2:5] + ')' + new_phone[5:8] + '-' + new_phone[8:10] + '-' + new_phone[10:12]
                else:
                    phone = new_phone
                query = 'SELECT id FROM "Print" ORDER BY id DESC LIMIT 1'
                self.cursor.execute(query)
                self.id = self.cursor.fetchone()
                query = f"INSERT INTO \"Print\" VALUES({int(self.id[0]) + 1}, '{print}', '{address}', '{phone}', '{year_opened}', {prop_id}, {dist_id})"
                self.cursor.execute(query)
                connection.connection.commit()
                self.error.setText('Успешно добавлено')
            except Exception as err:
                print(err)
                self.error.setText('Что-то пошло не так :(')
        else:
            self.error.setText('Проверьте корректность заполнения полей!')


class AddFormat(QDialog, AddFormat.Ui_Dialog):
    def __init__(self):
        super(AddFormat, self).__init__()
        self.setupUi(self)
        self.setFixedSize(560, 150)
        self.OKbutton.clicked.connect(self.correct_data)

    def correct_data(self):
        self.cursor = connection.connection.cursor()
        density = self.density.text()
        query = 'SELECT id FROM "PaperFormat" ORDER BY id DESC LIMIT 1'
        self.cursor.execute(query)
        self.id = self.cursor.fetchone()
        if 0 < len(density) < 30:
            try:
                query = f"INSERT INTO \"Density\" VALUES ({int(self.id[0])+1}, '{density}')"
                self.cursor.execute(query)
                connection.connection.commit()
                self.error.setText('Успешно добавлено')
            except Exception as err:
                print(err)
                self.error.setText('Что-то пошло не так :(')
        else:
            self.error.setText('Проверьте корректность заполнения полей!')


class AddPaper(QDialog, AddPaper.Ui_Dialog):
    def __init__(self):
        super(AddPaper, self).__init__()
        self.setupUi(self)
        self.setFixedSize(560, 150)
        self.OKbutton.clicked.connect(self.correct_data)

    def correct_data(self):
        self.cursor = connection.connection.cursor()
        paper = self.paper.text()
        query = 'SELECT id FROM "PaperType" ORDER BY id DESC LIMIT 1'
        self.cursor.execute(query)
        self.id = self.cursor.fetchone()
        if 0 < len(paper) < 30:
            try:
                query = f"INSERT INTO \"PaperType\" VALUES ({int(self.id[0])+1}, '{paper}')"
                self.cursor.execute(query)
                connection.connection.commit()
                self.error.setText('Успешно добавлено')
            except Exception as err:
                print(err)
                self.error.setText('Что-то пошло не так :(')
        else:
            self.error.setText('Проверьте корректность заполнения полей!')


class AddOrder(QDialog, AddOrder.Ui_Dialog):
    def __init__(self):
        super(AddOrder, self).__init__()
        self.setupUi(self)
        self.setFixedSize(1040, 140)
        self.OKbutton.clicked.connect(self.correct_data)
        self.cursor = connection.connection.cursor()
        query = 'SELECT id, name FROM "Customer"'
        self.cursor.execute(query)
        for t in self.cursor.fetchall():
            self.client.addItem(str(t))
        query = 'SELECT id, publication FROM "Product"'
        self.cursor.execute(query)
        for t in self.cursor.fetchall():
            self.product.addItem(str(t))

    def correct_data(self):
        date_start = self.date_start.text()
        date_plan = self.date_plan.text()
        date_fact = self.date_fact.text()
        cost = self.cost.text()
        client = self.client.currentText().replace('(', '').replace(')', '').replace(' \'', '\'').split(',')
        product = self.product.currentText().replace('(', '').replace(')', '').replace(' \'', '\'').split(',')
        client_id = str(client[0])
        product_id = str(product[0])
        if client_id.isalnum() and product_id.isalnum() and cost.isalnum():
            try:
                query = 'SELECT id FROM "Order" ORDER BY id DESC LIMIT 1'
                self.cursor.execute(query)
                self.id = self.cursor.fetchone()
                query = f"INSERT INTO \"Order\" VALUES({int(self.id[0]) + 1}, '{date_start}', '{date_plan}', '{date_fact}', '{cost}', {client_id}, {product_id})"
                self.cursor.execute(query)
                connection.connection.commit()
                self.error.setText('Успешно добавлено')
            except Exception as err:
                print(err)
                self.error.setText('Что-то пошло не так :(')
        else:
            self.error.setText('Проверьте корректность заполнения полей!')


class AddProduct(QDialog, AddProduct.Ui_Dialog):
    def __init__(self):
        super(AddProduct, self).__init__()
        self.setupUi(self)
        self.setFixedSize(740, 140)
        self.OKbutton.clicked.connect(self.correct_data)
        self.cursor = connection.connection.cursor()
        query = 'SELECT id, product FROM "ProductType"'
        self.cursor.execute(query)
        for t in self.cursor.fetchall():
            self.prod_type.addItem(str(t))
        query = 'SELECT id, density FROM "Density"'
        self.cursor.execute(query)
        for t in self.cursor.fetchall():
            self.density.addItem(str(t))
        query = 'SELECT id, type FROM "PaperType"'
        self.cursor.execute(query)
        for t in self.cursor.fetchall():
            self.paper.addItem(str(t))

    def correct_data(self):
        publication = self.publication.text()
        count = self.count.text()
        calculation = self.calculation.text()
        price = self.price.text()
        prod_type = self.prod_type.currentText().replace('(', '').replace(')', '').replace(' \'', '\'').split(',')
        prod_type_id = str(prod_type[0])
        density = self.density.currentText().replace('(', '').replace(')', '').replace(' \'', '\'').split(',')
        paper = self.paper.currentText().replace('(', '').replace(')', '').replace(' \'', '\'').split(',')
        density_id = str(density[0])
        paper_id = str(paper[0])
        if 0 < len(publication) < 129 and 0 < int(calculation) < 1000001 and 0 < int(count) < 1000000 and price.isalnum():
            try:
                query = 'SELECT id FROM "Product" ORDER BY id DESC LIMIT 1'
                self.cursor.execute(query)
                self.id = self.cursor.fetchone()
                query = f"INSERT INTO \"Product\" VALUES({int(self.id[0]) + 1}, '{count}', '{calculation}', '{price}', '{publication}', {density_id}, {paper_id}, {prod_type_id})"
                self.cursor.execute(query)
                connection.connection.commit()
                self.error.setText('Успешно добавлено')
            except Exception as err:
                print(err)
                self.error.setText('Что-то пошло не так :(')
        else:
            self.error.setText('Проверьте корректность заполнения полей!')


class AddProductType(QDialog, AddProductType.Ui_Dialog):
    def __init__(self):
        super(AddProductType, self).__init__()
        self.setupUi(self)
        self.setFixedSize(560, 150)
        self.OKbutton.clicked.connect(self.correct_data)

    def correct_data(self):
        self.cursor = connection.connection.cursor()
        prod_type = self.prod_type.text()
        query = 'SELECT id FROM "ProductType" ORDER BY id DESC LIMIT 1'
        self.cursor.execute(query)
        self.id = self.cursor.fetchone()
        if 0 < len(prod_type) < 30:
            try:
                query = f"INSERT INTO \"ProductType\" VALUES ({int(self.id[0]) + 1}, '{prod_type}')"
                self.cursor.execute(query)
                connection.connection.commit()
                self.error.setText('Успешно добавлено')
            except Exception as err:
                print(err)
                self.error.setText('Что-то пошло не так :(')
        else:
            self.error.setText('Проверьте корректность заполнения полей!')
