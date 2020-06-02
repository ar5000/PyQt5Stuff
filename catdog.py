# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'catdog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(491, 391)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 491, 391))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.picture = QtWidgets.QLabel(self.gridLayoutWidget)
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap("cat.JPG"))
        self.picture.setScaledContents(True)
        self.picture.setObjectName("picture")
        self.verticalLayout.addWidget(self.picture)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cat = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cat.setFont(font)
        self.cat.setObjectName("cat")
        self.horizontalLayout.addWidget(self.cat, 0, QtCore.Qt.AlignTop)
        self.cat.clicked.connect(self.show_cat)
        self.dog = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dog.setFont(font)
        self.dog.setObjectName("dog")
        self.dog.clicked.connect(self.show_dog)
        self.horizontalLayout.addWidget(self.dog, 0, QtCore.Qt.AlignTop)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cat.setText(_translate("MainWindow", "Cat"))
        self.dog.setText(_translate("MainWindow", "Dog"))

    def show_dog(self):
        self.picture.setPixmap(QtGui.QPixmap("dog.JPG"))

    def show_cat(self):
        self.picture.setPixmap(QtGui.QPixmap("cat.JPG"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
