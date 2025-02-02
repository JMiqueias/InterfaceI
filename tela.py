# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from cadastro import Cadastro
from pessoa import Pessoa


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 10, 131, 41))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 60, 291, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 60, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 90, 71, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 120, 67, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 150, 91, 17))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 120, 291, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 150, 291, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(170, 290, 151, 25))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 190, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 240, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 290, 67, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 360, 67, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(60, 390, 67, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(60, 430, 91, 17))
        self.label_10.setObjectName("label_10")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 290, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 90, 291, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(170, 350, 271, 25))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(170, 390, 271, 25))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(170, 430, 113, 25))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 220, 631, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        '''modificacoes'''
        self.cad = Cadastro()
        self.pushButton.clicked.connect(self.botaoCadastra)
        self.pushButton_2.clicked.connect(self.botaoBusca)

    def botaoCadastra(self):
        nome = self.lineEdit.text()
        endereco = self.lineEdit_2.text()
        cpf = self.lineEdit_3.text()
        nascimento = self.lineEdit_4.text()

        if not(nome == '' or endereco == '' or cpf == '' or nascimento == ''):
            p = Pessoa(nome,endereco,cpf,nascimento)
            if (self.cad.cadastra(p)):
                QMessageBox.information(None,'POOII','Cadastro realizado com sucesso!')
                self.lineEdit.setText('')
                self.lineEdit_2.setText('')
                self.lineEdit_3.setText('')
                self.lineEdit_4.setText('')
            else:
                QMessageBox.information(None,'POOII','O CPF informado já está cadastrado na base de dados!')
        else:
            QMessageBox.information(None,'POOII','Todos os valores devem ser preenchidos!')

    def botaoBusca(self):
        cpf = self.lineEdit_5.text()
        pessoa = self.cad.busca(cpf)
        if (pessoa != None):
            self.lineEdit_6.setText(pessoa.nome)
            self.lineEdit_7.setText(pessoa.endereco)
            self.lineEdit_8.setText(pessoa.nascimento)
        else:
            QMessageBox.information(None,'POOII','CPF não encontrado!')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Cadastra"))
        self.label_2.setText(_translate("MainWindow", "Nome:"))
        self.label_3.setText(_translate("MainWindow", "Endereço:"))
        self.label_4.setText(_translate("MainWindow", "CPF:"))
        self.label_5.setText(_translate("MainWindow", "Nascimento:"))
        self.pushButton.setText(_translate("MainWindow", "Cadastre!"))
        self.label_6.setText(_translate("MainWindow", "Busca"))
        self.label_7.setText(_translate("MainWindow", "CPF:"))
        self.label_8.setText(_translate("MainWindow", "Nome:"))
        self.label_9.setText(_translate("MainWindow", "Endereço:"))
        self.label_10.setText(_translate("MainWindow", "Nascimento:"))
        self.pushButton_2.setText(_translate("MainWindow", "Buscar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
