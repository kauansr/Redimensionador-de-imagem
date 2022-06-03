from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(593, 551)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.input_largura = QtWidgets.QLineEdit(self.centralwidget)
        self.input_largura.setObjectName("input_largura")
        self.gridLayout.addWidget(self.input_largura, 2, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 573, 444))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_img = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_img.setText("")
        self.label_img.setObjectName("label_img")
        self.gridLayout_2.addWidget(self.label_img, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 5)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.btn_escolher_arquivo = QtWidgets.QPushButton(self.centralwidget)
        self.btn_escolher_arquivo.setObjectName("btn_escolher_arquivo")
        self.gridLayout.addWidget(self.btn_escolher_arquivo, 1, 4, 1, 1)
        self.input_altura = QtWidgets.QLineEdit(self.centralwidget)
        self.input_altura.setObjectName("input_altura")
        self.gridLayout.addWidget(self.input_altura, 2, 3, 1, 1)
        self.Redimensionar = QtWidgets.QPushButton(self.centralwidget)
        self.Redimensionar.setObjectName("Redimensionar")
        self.gridLayout.addWidget(self.Redimensionar, 2, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.Salvar = QtWidgets.QPushButton(self.centralwidget)
        self.Salvar.setObjectName("Salvar")
        self.gridLayout.addWidget(self.Salvar, 3, 4, 1, 1)
        self.input_abrir_arquivo = QtWidgets.QLineEdit(self.centralwidget)
        self.input_abrir_arquivo.setObjectName("input_abrir_arquivo")
        self.gridLayout.addWidget(self.input_abrir_arquivo, 1, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Redimensionar imagem"))
        self.label.setText(_translate("MainWindow", "Largura"))
        self.btn_escolher_arquivo.setText(_translate("MainWindow", "Escolher arquivo"))
        self.Redimensionar.setText(_translate("MainWindow", "Redimensionar"))
        self.label_2.setText(_translate("MainWindow", "Altura"))
        self.Salvar.setText(_translate("MainWindow", "Salvar"))