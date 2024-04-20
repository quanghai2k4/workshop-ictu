# Description: This file contains the main code for the application.
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from ui.Ui_login import *
from ui.master import Ui_MainWindow
import dbcontrol
import sys
from PyQt6 import uic

# Create the application
app = QApplication(sys.argv)

#--------------------------------------------------------------
# Create the UI classes
class UI_LoginWindow(QMainWindow):
    # Initialize the class
    def __init__(self):
        super().__init__()
        self.uic = Ui_LoginUI()
        self.uic.setupUi(self)

        # Connect the buttons to functions
        self.uic.exitButton.clicked.connect(sys.exit)
        self.uic.loginButton.clicked.connect(self.loginApp)

    # Define login function
    def loginApp(self):
        username = self.uic.usernameLine.text()
        password = self.uic.passwordLine.text()
        print(f'Username: {username}, Password: {password}')  # Debug statement
        role = dbcontrol.check_acc(username, password)
        print(f'Role: {role}')  # Debug statement
        if role == '1':
            stack.setCurrentWidget(mainUI)
        elif role == '0':
            stack.setCurrentWidget(mainUI)
            mainUI.uic.accButton.hide()
            mainUI.uic.employeeButton.hide()
            mainUI.uic.accounts.hide()
            mainUI.uic.employees.hide()
        else:
            QMessageBox.warning(self, 'Error', 'Invalid username or password')
        # Rest of the code...
#--------------------------------------------------------------

        
#--------------------------------------------------------------
# Create the UI classes
class UI_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        # set hide iconwidget
        self.uic.iconwidget.hide()

        # Change page when click on the button
        # iconwidget
        self.uic.accounts.clicked.connect(self.showAcc)
        self.uic.employees.clicked.connect(self.showEmployee)
        self.uic.products.clicked.connect(self.showProduct)
        self.uic.customers.clicked.connect(self.showCustomer)
        self.uic.orders.clicked.connect(self.showOrder)
        self.uic.services.clicked.connect(self.showService)
        self.uic.chart.clicked.connect(self.showChart)

        # fullmenuwidget
        self.uic.accButton.clicked.connect(self.showAcc)
        self.uic.employeeButton.clicked.connect(self.showEmployee)
        self.uic.productButton.clicked.connect(self.showProduct)
        self.uic.customerButton.clicked.connect(self.showCustomer)
        self.uic.orderButton.clicked.connect(self.showOrder)
        self.uic.serviceButton.clicked.connect(self.showService)
        self.uic.chartButton.clicked.connect(self.showChart)

        # Connect the update buttons to functions
        self.uic.accUpdate.clicked.connect(self.updateAcc)
        self.uic.employeeUpdate.clicked.connect(self.updateEmployee)
        self.uic.updateProduct.clicked.connect(self.updateProduct)
        self.uic.updateCus.clicked.connect(self.updateCustomer)
        self.uic.updateOrder.clicked.connect(self.updateOrder)
        self.uic.loadService.clicked.connect(self.updateService)

        # Connect the load buttons to functions
        self.uic.loadAcc.clicked.connect(self.loadAcc)
        self.uic.loadEmployee.clicked.connect(self.loadEmployee)
        self.uic.loadProduct.clicked.connect(self.loadProduct)
        self.uic.loadCus.clicked.connect(self.loadCustomer)
        self.uic.loadOrder.clicked.connect(self.loadOrder)
        self.uic.loadService.clicked.connect(self.loadService)

        # Connect the select buttons to functions
        self.uic.selectAcc.clicked.connect(self.selectAcc)
        self.uic.selectEmployee.clicked.connect(self.selectEmployee)
        self.uic.selectProduct.clicked.connect(self.selectProduct)
        self.uic.selectCus.clicked.connect(self.selectCustomer)
        self.uic.selectOrder.clicked.connect(self.selectOrder)
        self.uic.selectService.clicked.connect(self.selectService)

        # Connect the add buttons to functions
        self.uic.addAcc.clicked.connect(self.addAcc)
        self.uic.addEmployee.clicked.connect(self.addEmployee)
        self.uic.addProduct.clicked.connect(self.addProduct)
        self.uic.addCus.clicked.connect(self.addCustomer)
        self.uic.addOrder.clicked.connect(self.addOrder)
        self.uic.addService.clicked.connect(self.addService)
        # ok button
        self.uic.ok_button.clicked.connect(self.totalAmount)

        # Connect the delete buttons to functions
        self.uic.delAcc.clicked.connect(self.deleteAcc)
        self.uic.delEmployee.clicked.connect(self.deleteEmployee)
        self.uic.delProduct.clicked.connect(self.deleteProduct)
        self.uic.delCus.clicked.connect(self.deleteCustomer)
        self.uic.delOrder.clicked.connect(self.deleteOrder)
        self.uic.delService.clicked.connect(self.deleteService)

        # Connect the clear buttons to functions
        self.uic.clearAcc.clicked.connect(self.clearAcc)
        self.uic.clearEmployee.clicked.connect(self.clearEmployee)
        self.uic.clearProduct.clicked.connect(self.clearProduct)
        self.uic.clearCus.clicked.connect(self.clearCustomer)
        self.uic.clearOrder.clicked.connect(self.clearOrder)
        self.uic.clearService.clicked.connect(self.clearService)

# Show functions
    def showAcc(self):
        self.uic.stackedWidget_2.setCurrentWidget(self.uic.pageAcc)

    def showEmployee(self):
        self.uic.stackedWidget_2.setCurrentWidget(self.uic.pageEmployee)

    def showProduct(self):
        self.uic.stackedWidget_2.setCurrentWidget(self.uic.pageProduct)

    def showCustomer(self):
        self.uic.stackedWidget_2.setCurrentWidget(self.uic.pageCus)

    def showOrder(self):
        self.uic.stackedWidget_2.setCurrentWidget(self.uic.pageOrder)

    def showService(self):
        self.uic.stackedWidget_2.setCurrentWidget(self.uic.pageService)

    def showChart(self):
        self.uic.stackedWidget_2.setCurrentWidget(self.uic.pageChart)

# Update functions
    def updateAcc(self):
        username = self.uic.username.text()
        password = self.uic.password.text()
        role = self.uic.role.text()
        dbcontrol.update_acc(username, password, role)
        self.loadAcc()

    def updateEmployee(self):
        _id = self.uic.idEmployee.text()
        name = self.uic.nameEmployee.text()
        age = self.uic.ageEmployee.text()
        sex = self.uic.sexEmployee.text()
        phone = self.uic.phoneEmployee.text()
        address = self.uic.addressEmployee.text()
        position = self.uic.position.text()
        salary = self.uic.salary.text()
        dbcontrol.update_employee(_id, name, age, sex, phone, address, position, salary)
        self.loadEmployee()

    def updateProduct(self):
        _id = self.uic.idProduct.text()
        name = self.uic.nameProduct.text()
        price = self.uic.priceProduct.text()
        quantity = self.uic.quantity.text()
        dbcontrol.update_product(_id, name, price, quantity)
        self.loadProduct()

    def updateCustomer(self):
        _id = self.uic.idCus.text()
        name = self.uic.nameCus.text()
        email = self.uic.emailCus.text()
        phone = self.uic.phoneCus.text()
        address = self.uic.addressCus.text()
        dbcontrol.update_customer(_id, name, address, phone, email)
        self.loadCustomer()

    def updateOrder(self):
        _id = self.uic.idOrder.text()
        customer_id = self.uic.customerID.text()
        orderdate = self.uic.orderdate.date()
        enddate = self.uic.enddate.date()
        total = self.uic.total.text()
        status = self.uic.status.text()
        dbcontrol.update_order(_id, customer_id, orderdate, enddate, total, status)
        self.loadOrder()

    def updateService(self):
        _id = self.uic.idService.text()
        name = self.uic.nameService.text()
        price = self.uic.priceService.text()
        dbcontrol.update_service(_id, name, price)
        self.loadService()

# Select functions
    def selectAcc(self):
        self.uic.idacc.setText(self.uic.tableAcc.item(self.uic.tableAcc.currentRow(), 0).text())
        self.uic.username.setText(self.uic.tableAcc.item(self.uic.tableAcc.currentRow(), 1).text())
        self.uic.password.setText(self.uic.tableAcc.item(self.uic.tableAcc.currentRow(), 2).text())
        self.uic.role.setText(self.uic.tableAcc.item(self.uic.tableAcc.currentRow(), 3).text())

    def selectEmployee(self):
        self.uic.idEmployee.setText(self.uic.tableEmployee.item(self.uic.tableEmployee.currentRow(), 0).text())
        self.uic.nameEmployee.setText(self.uic.tableEmployee.item(self.uic.tableEmployee.currentRow(), 1).text())
        self.uic.ageEmployee.setText(self.uic.tableEmployee.item(self.uic.tableEmployee.currentRow(), 2).text())
        self.uic.sexEmployee.setText(self.uic.tableEmployee.item(self.uic.tableEmployee.currentRow(), 3).text())
        self.uic.phoneEmployee.setText(self.uic.tableEmployee.item(self.uic.tableEmployee.currentRow(), 4).text())
        self.uic.salary.setText(self.uic.tableEmployee.item(self.uic.tableEmployee.currentRow(), 5).text())
        self.uic.addressEmployee.setText(self.uic.tableEmployee.item(self.uic.tableEmployee.currentRow(), 6).text())
        self.uic.position.setText(self.uic.tableEmployee.item(self.uic.tableEmployee.currentRow(), 7).text())
        self.uic.startdate.date(self.uic.tableEmployee.item(self.uic.tableEmployee.currentRow(), 8).text())

    def selectProduct(self):
        self.uic.idProduct.setText(self.uic.tableProduct.item(self.uic.tableProduct.currentRow(), 0).text())
        self.uic.nameProduct.setText(self.uic.tableProduct.item(self.uic.tableProduct.currentRow(), 1).text())
        self.uic.priceProduct.setText(self.uic.tableProduct.item(self.uic.tableProduct.currentRow(), 2).text())
        self.uic.quantity.setText(self.uic.tableProduct.item(self.uic.tableProduct.currentRow(), 3).text())

    def selectCustomer(self):
        self.uic.idCus.setText(self.uic.tableCus.item(self.uic.tableCus.currentRow(), 0).text())
        self.uic.nameCus.setText(self.uic.tableCus.item(self.uic.tableCus.currentRow(), 1).text())
        self.uic.emailCus.setText(self.uic.tableCus.item(self.uic.tableCus.currentRow(), 2).text())
        self.uic.phoneCus.setText(self.uic.tableCus.item(self.uic.tableCus.currentRow(), 3).text())
        self.uic.addressCus.setText(self.uic.tableCus.item(self.uic.tableCus.currentRow(), 4).text())
        self.uic.orderID.setText(self.uic.tableCus.item(self.uic.tableCus.currentRow(), 5).text())

    def selectOrder(self):
        self.uic.orderdate.setEnabled(True)
        self.uic.idOrder.setText(self.uic.tableOrder.item(self.uic.tableOrder.currentRow(), 0).text())
        date_string = self.uic.tableOrder.item(self.uic.tableOrder.currentRow(), 1).text()
        date = QtCore.QDate.fromString(date_string, 'yyyy-MM-dd')
        self.uic.orderdate.setDate(date)
        self.uic.total.setText(self.uic.tableOrder.item(self.uic.tableOrder.currentRow(), 2).text())
        #self.uic.enddate.date(self.uic.tableOrder.item(self.uic.tableOrder.currentRow(), 3).text())
        self.uic.customerID.setText(self.uic.tableOrder.item(self.uic.tableOrder.currentRow(), 4).text())
        try:
            self.uic.status.setText(self.uic.tableOrder.item(self.uic.tableOrder.currentRow(), 5).text())
        except:
            self.uic.status.setText('Chưa giao hàng')

    def selectService(self):
        self.uic.idService.setText(self.uic.tableService.item(self.uic.tableService.currentRow(), 0).text())
        self.uic.nameService.setText(self.uic.tableService.item(self.uic.tableService.currentRow(), 1).text())
        self.uic.priceService.setText(self.uic.tableService.item(self.uic.tableService.currentRow(), 2).text())

# Clear functions
    def clearAcc(self):
        self.uic.idacc.clear()
        self.uic.username.clear()
        self.uic.password.clear()
        self.uic.role.clear()

    def clearEmployee(self):
        self.uic.idEmployee.clear()
        self.uic.nameEmployee.clear()
        self.uic.ageEmployee.clear()
        self.uic.sexEmployee.clear()
        self.uic.phoneEmployee.clear()
        self.uic.salary.clear()
        self.uic.addressEmployee.clear()
        self.uic.position.clear()
        self.uic.startdate.clear()

    def clearProduct(self):
        self.uic.idProduct.clear()
        self.uic.nameProduct.clear()
        self.uic.priceProduct.clear()
        self.uic.quantity.clear()

    def clearCustomer(self):
        self.uic.idCus.clear()
        self.uic.nameCus.clear()
        self.uic.emailCus.clear()
        self.uic.phoneCus.clear()
        self.uic.addressCus.clear()
        self.uic.orderID.clear()

    def clearOrder(self):
        self.uic.idOrder.clear()
        self.uic.customerID.clear()
        self.uic.orderdate.clear()
        self.uic.enddate.clear()
        self.uic.total.clear()
        self.uic.status.clear()

    def clearService(self):
        self.uic.idService.clear()
        self.uic.nameService.clear()
        self.uic.priceService.clear()


# Add functions
    def addAcc(self):
        username = self.uic.username.text()
        password = self.uic.password.text()
        role = self.uic.role.text()
        dbcontrol.insert_acc(username, password, role)
        self.loadAcc()

    def addEmployee(self):
        _id = self.uic.idEmployee.text()
        name = self.uic.nameEmployee.text()
        age = self.uic.ageEmployee.text()
        sex = self.uic.sexEmployee.text()
        phone = self.uic.phoneEmployee.text()
        address = self.uic.addressEmployee.text()
        position = self.uic.position.text()
        salary = self.uic.salary.text()
        dbcontrol.insert_employee(_id, name, age, sex, phone, address, position, salary)
        self.loadEmployee()

    def addProduct(self):
        _id = self.uic.idProduct.text()
        name = self.uic.nameProduct.text()
        price = self.uic.priceProduct.text()
        quantity = self.uic.quantity.text()
        dbcontrol.insert_product(_id, name, price, quantity)
        self.loadProduct()

    def addCustomer(self):
        _id = self.uic.idCus.text()
        name = self.uic.nameCus.text()
        email = self.uic.emailCus.text()
        phone = self.uic.phoneCus.text()
        address = self.uic.addressCus.text()
        dbcontrol.insert_customer(_id, name, address, phone, email)
        self.loadCustomer()

    def addOrder(self):
        prd1 = self.uic.cb1.text()
        prd2 = self.uic.cb2.text()
        prd3 = self.uic.cb3.text()
        prd4 = self.uic.cb4.text()
        products = []
        if self.uic.cb1.isChecked():
            products.append(prd1)
        if self.uic.cb2.isChecked():
            products.append(prd2)
        if self.uic.cb3.isChecked():
            products.append(prd3)
        if self.uic.cb4.isChecked():
            products.append(prd4)
        _id = int(self.uic.idOrder.text())
        customer_id = self.uic.customerID.text()
        total = self.totalAmount()
        dbcontrol.insert_order(_id, total, products, customer_id)
        self.loadOrder()

    def addService(self):
        _id = self.uic.idService.text()
        name = self.uic.nameService.text()
        price = self.uic.priceService.text()
        dbcontrol.insert_service(_id, name, price)
        self.loadService()

# Delete functions
    def deleteAcc(self):
        _id  = self.uic.idacc.text()
        dbcontrol.delete_acc(_id)
        self.loadAcc()
    
    def deleteEmployee(self):
        _id = self.uic.idEmployee.text()
        dbcontrol.delete_employee(_id)
        self.loadEmployee()

    def deleteProduct(self):
        _id = self.uic.idProduct.text()
        dbcontrol.delete_product(_id)
        self.loadProduct()

    def deleteCustomer(self):
        _id = self.uic.idCus.text()
        dbcontrol.delete_customer(_id)
        self.loadCustomer()

    def deleteOrder(self):
        _id = int(self.uic.idOrder.text())
        dbcontrol.delete_order(_id)
        self.loadOrder()

    def deleteService(self):
        _id = self.uic.idService.text()
        dbcontrol.delete_service(_id)
        self.loadService()

# Load data from MongoDB and display it in the table
    def loadAcc(self):
        # Fetch data from MongoDB and convert it into a pandas DataFrame
        df = dbcontrol.load_acc()
        if df is None:
            QMessageBox.warning(self, 'Error', 'No data to load')
            return

        # Determine the number of rows and columns
        self.uic.tableAcc.setRowCount(len(df))
        self.uic.tableAcc.setColumnCount(len(df.columns))

        # Add data to the table
        for row in range(df.shape[0]):
            for column in range(df.shape[1]):
                table_item = QTableWidgetItem(str(df.iat[row, column]))  # Ensure item is a string
                self.uic.tableAcc.setItem(row, column, table_item)

    def loadEmployee(self):
        df = dbcontrol.load_employee()
        if df is None:
            QMessageBox.warning(self, 'Error', 'No data to load')
            return

        self.uic.tableEmployee.setRowCount(len(df))
        self.uic.tableEmployee.setColumnCount(len(df.columns))

        for row in range(df.shape[0]):
            for column in range(df.shape[1]):
                table_item = QTableWidgetItem(str(df.iat[row, column]))
                self.uic.tableEmployee.setItem(row, column, table_item)

    def loadProduct(self):
        df = dbcontrol.load_product()
        if df is None:
            print('No data to load')
            return

        self.uic.tableProduct.setRowCount(len(df))
        self.uic.tableProduct.setColumnCount(len(df.columns))

        for row in range(df.shape[0]):
            for column in range(df.shape[1]):
                table_item = QTableWidgetItem(str(df.iat[row, column]))
                self.uic.tableProduct.setItem(row, column, table_item)
        
    def loadCustomer(self):
        df = dbcontrol.load_customer()
        if df is None:
            print('No data to load')
            return

        self.uic.tableCus.setRowCount(len(df))
        self.uic.tableCus.setColumnCount(len(df.columns))

        for row in range(df.shape[0]):
            for column in range(df.shape[1]):
                table_item = QTableWidgetItem(str(df.iat[row, column]))
                self.uic.tableCus.setItem(row, column, table_item)

    def loadOrder(self):
        df = dbcontrol.load_order()
        if df is None:
            print('No data to load')
            return

        self.uic.tableOrder.setRowCount(len(df))
        self.uic.tableOrder.setColumnCount(len(df.columns))

        for row in range(df.shape[0]):
            for column in range(df.shape[1]):
                table_item = QTableWidgetItem(str(df.iat[row, column]))
                self.uic.tableOrder.setItem(row, column, table_item)

    def loadService(self):
        df = dbcontrol.load_service()
        if df is None:
            print('No data to load')
            return

        self.uic.tableService.setRowCount(len(df))
        self.uic.tableService.setColumnCount(len(df.columns))

        for row in range(df.shape[0]):
            for column in range(df.shape[1]):
                table_item = QTableWidgetItem(str(df.iat[row, column]))
                self.uic.tableService.setItem(row, column, table_item)

#--------------------------------------------------------------
# Define the checkbox function
    def totalAmount(self):
        total = 0
        prc1 = self.uic.pr1.text()
        prc2 = self.uic.pr2.text()
        prc3 = self.uic.pr3.text()
        prc4 = self.uic.pr4.text()
        if self.uic.cb1.isChecked():
            total += float(prc1)
        if self.uic.cb2.isChecked():
            total += float(prc2)
        if self.uic.cb3.isChecked():
            total += float(prc3)
        if self.uic.cb4.isChecked():
            total += float(prc4)
        self.uic.total_4.setText(str(total))
        return total

# Create instances of the UI classes
loginUI = UI_LoginWindow()
mainUI = UI_MainWindow()
stack = QtWidgets.QStackedWidget()
stack.addWidget(loginUI)
stack.addWidget(mainUI)

# Show the login window
if __name__ == "__main__":
    
    stack.setCurrentWidget(loginUI)
    stack.show()

    sys.exit(app.exec())