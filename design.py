from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QDesktopServices

class Ui_MainWindow(object):
    """A class that creates objects for the main window design"""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(502, 388)
        MainWindow.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LB_MainFon = QtWidgets.QLabel(parent=self.centralwidget)
        self.LB_MainFon.setGeometry(QtCore.QRect(-10, -20, 531, 551))
        self.LB_MainFon.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.LB_MainFon.setText("")
        self.LB_MainFon.setObjectName("LB_MainFon")
        self.LB_Welcome = QtWidgets.QLabel(parent=self.centralwidget)
        self.LB_Welcome.setGeometry(QtCore.QRect(110, 30, 301, 21))
        self.LB_Welcome.setStyleSheet("color: white;\n"
"font: 15pt \"Copperplate Gothic Light\";")
        self.LB_Welcome.setObjectName("LB_Welcome")
        self.BT_createRecord = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BT_createRecord.setGeometry(QtCore.QRect(150, 120, 201, 31))
        self.BT_createRecord.setStyleSheet("QPushButton {\n"
"background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"border: 2px solid red;\n"
"border-radius: 7px;\n"
"font: 12pt \"Arial Rounded MT Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(50,50,50);\n""}")
        self.BT_createRecord.setObjectName("BT_createRecord")
        self.BT_getRecord = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BT_getRecord.setGeometry(QtCore.QRect(150, 170, 201, 31))
        self.BT_getRecord.setStyleSheet("QPushButton {\n"
"background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"border: 2px solid red;\n"
"border-radius: 7px;\n"
"font: 12pt \"Arial Rounded MT Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(50,50,50);\n"
"}")
        self.BT_getRecord.setObjectName("BT_getRecord")
        self.BT_ChangePassword = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BT_ChangePassword.setGeometry(QtCore.QRect(150, 220, 201, 31))
        self.BT_ChangePassword.setStyleSheet("QPushButton {\n"
"background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"border: 2px solid red;\n"
"border-radius: 7px;\n"
"font: 12pt \"Arial Rounded MT Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(50,50,50);\n"
"}")
        self.BT_ChangePassword.setObjectName("BT_ChangePassword")
        self.WIDGT_line_underWelcome = QtWidgets.QWidget(parent=self.centralwidget)
        self.WIDGT_line_underWelcome.setGeometry(QtCore.QRect(80, 60, 339, 2))
        self.WIDGT_line_underWelcome.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.WIDGT_line_underWelcome.setObjectName("WIDGT_line_underWelcome")
        self.LB_Setnet = QtWidgets.QLabel(parent=self.centralwidget)
        self.LB_Setnet.setGeometry(QtCore.QRect(100, 110, 110, 21))
        self.LB_Setnet.setStyleSheet("color: white;\n"
"font: 18pt \"Tw Cen MT Condensed Extra Bold\";\n")
        self.LB_Setnet.setObjectName("LB_Setnet")
        self.LB_SetnetLogin = QtWidgets.QLabel(parent=self.centralwidget)
        self.LB_SetnetLogin.setGeometry(QtCore.QRect(100, 150, 160, 25))
        self.LB_SetnetLogin.setStyleSheet("color: white;\n"
                                     "font: 18pt \"Tw Cen MT Condensed Extra Bold\";\n")
        self.LB_SetnetLogin.setObjectName("LB_SetnetLogin")
        self.LB_SetnetPass = QtWidgets.QLabel(parent=self.centralwidget)
        self.LB_SetnetPass.setGeometry(QtCore.QRect(100, 190, 150, 25))
        self.LB_SetnetPass.setStyleSheet("color: white;\n"
                                     "font: 18pt \"Tw Cen MT Condensed Extra Bold\";\n")
        self.LB_SetnetPass.setObjectName("LB_SetnetPass")
        self.LINEED_Setnet = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.LINEED_Setnet.setGeometry(QtCore.QRect(215, 114, 120, 19))
        self.LINEED_Setnet.setStyleSheet("QLineEdit {\n"
" background-color: rgb(45, 45, 45);\n"
"border: 1px solid rgb(80,80,80);\n"
"border-radius: 2px;\n"
"color:white;\n"
"font: 10pt \"Arial Rounded MT Bold\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 1px solid red;\n"
"}")
        self.LINEED_Setnet.setObjectName("LINEED_Setnet")



        self.LINEED_SetnetLogin = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.LINEED_SetnetLogin.setGeometry(QtCore.QRect(265, 155, 120, 19))
        self.LINEED_SetnetLogin.setStyleSheet("QLineEdit {\n"
" background-color: rgb(45, 45, 45);\n"
"border: 1px solid rgb(80,80,80);\n"
"border-radius: 2px;\n"
"color:white;\n"
"font: 10pt \"Arial Rounded MT Bold\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 1px solid red;\n"
"}")
        self.LINEED_SetnetLogin.setObjectName("LINEED_SetnetLogin")

        self.LINEED_Password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.LINEED_Password.setGeometry(QtCore.QRect(247, 195, 120, 19))
        self.LINEED_Password.setStyleSheet("QLineEdit {\n"
" background-color: rgb(45, 45, 45);\n"
"border: 1px solid rgb(80,80,80);\n"
"border-radius: 2px;\n"
"color:white;\n"
"font: 10pt \"Arial Rounded MT Bold\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 1px solid red;\n"
"}")
        self.LINEED_Password.setObjectName("LINEED_Password")

        self.BT_GeneratePassword = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BT_GeneratePassword.setGeometry(QtCore.QRect(375, 194, 70, 22))
        self.BT_GeneratePassword.setStyleSheet("QPushButton {\n"
"background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"border: 2px solid red;\n"
"border-radius: 7px;\n"
"font: 10pt \"Arial Rounded MT Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(50,50,50);\n"
"}")
        self.BT_GeneratePassword.setObjectName("BT_GeneratePassword")

        self.BT_SavePassword = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BT_SavePassword.setGeometry(QtCore.QRect(102, 230, 130, 25))
        self.BT_SavePassword.setStyleSheet("QPushButton {\n"
"background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"border: 2px solid red;\n"
"border-radius: 7px;\n"
"font: 12pt \"Arial Rounded MT Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(50,50,50);\n"
"}")
        self.BT_SavePassword.setObjectName("BT_SavePassword")

        self.BT_Get = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BT_Get.setGeometry(QtCore.QRect(102, 187, 130, 25))
        self.BT_Get.setStyleSheet("QPushButton {\n"
"background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"border: 2px solid red;\n"
"border-radius: 7px;\n"
"font: 12pt \"Arial Rounded MT Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(50,50,50);\n"
"}")
        self.BT_Get.setObjectName("BT_Get")

        self.BT_SaveNew = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BT_SaveNew.setGeometry(QtCore.QRect(60, 230, 120, 25))
        self.BT_SaveNew.setStyleSheet("QPushButton {\n"
"background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"border: 2px solid red;\n"
"border-radius: 7px;\n"
"font: 12pt \"Arial Rounded MT Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(50,50,50);\n"
"}")
        self.BT_SaveNew.setObjectName("BT_SaveNew")

        self.LB_StatusPass = QtWidgets.QLabel(parent=self.centralwidget)
        self.LB_StatusPass.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.LB_StatusPass.setStyleSheet("color: white;\n"
                                      "font: 12pt \"Copperplate Gothic Light\";")
        self.LB_StatusPass.setObjectName("LB_StatusPass")

        self.BT_close_win = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BT_close_win.setGeometry(QtCore.QRect(470, 3, 25, 25))
        self.BT_close_win.setStyleSheet("QPushButton {\n"
                                        "font-size: 20pt;\n"
                                        "background-color: rgba(255, 85, 0, 0);\n"
                                        "color: white;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgba(255, 255, 255, 60);\n"
                                        "    border-radius: 4px;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color: rgba(255, 255, 255, 90);\n"
                                        "    border-radius: 4px;\n"
                                        "}")

        self.BT_hide_win = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BT_hide_win.setGeometry(QtCore.QRect(440, 3, 25, 25))
        self.BT_hide_win.setStyleSheet("QPushButton {\n"
                                       "font-size: 12pt;\n"
                                       "background-color: rgba(255, 85, 0, 0);\n"
                                       "color: white;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "    background-color: rgba(255, 255, 255, 60);\n"
                                       "    border-radius: 4px;\n"
                                       "}\n"
                                       "QPushButton:pressed{\n"
                                       "    background-color: rgba(255, 255, 255, 90);\n"
                                       "    border-radius: 4px;\n"
                                       "}")

        self.BT_Delete = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BT_Delete.setGeometry(QtCore.QRect(190, 230, 120, 25))
        self.BT_Delete.setStyleSheet("QPushButton {\n"
"background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"border: 2px solid red;\n"
"border-radius: 7px;\n"
"font: 12pt \"Arial Rounded MT Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(50,50,50);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(r"cfg\Delete.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.BT_Delete.setText("")
        self.BT_Delete.setIcon(icon2)
        self.BT_Delete.setObjectName("BT_Delete")

        self.BT_CopyPaste = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BT_CopyPaste.setGeometry(QtCore.QRect(388, 187, 25, 25))
        self.BT_CopyPaste.setStyleSheet("QPushButton {\n"
"background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"border: 2px solid red;\n"
"border-radius: 7px;\n"
"font: 12pt \"Arial Rounded MT Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(50,50,50);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(r"cfg\CopyPaste.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.BT_CopyPaste.setText("")
        self.BT_CopyPaste.setIcon(icon2)
        self.BT_CopyPaste.setObjectName("BT_CopyPaste")

        self.BT_Info = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BT_Info.setGeometry(QtCore.QRect(8, 7, 31, 31))
        self.BT_Info.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.BT_Info.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(r"cfg\Info.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.BT_Info.setIcon(icon3)
        self.BT_Info.setObjectName("BT_Info")

        self.BT_ExitForMain = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BT_ExitForMain.setGeometry(QtCore.QRect(245, 230, 130, 25))
        self.BT_ExitForMain.setStyleSheet("QPushButton {\n"
"background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"border: 2px solid red;\n"
"border-radius: 7px;\n"
"font: 12pt \"Arial Rounded MT Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(50,50,50);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(r"cfg\WhiteExit.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.BT_ExitForMain.setText("")
        self.BT_ExitForMain.setIcon(icon2)
        self.BT_ExitForMain.setObjectName("BT_ExitForMain")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Data"))
        self.LB_Welcome.setText(_translate("MainWindow", "Welcome to PasswordManager"))
        self.BT_createRecord.setText(_translate("MainWindow", "create record"))
        self.BT_getRecord.setText(_translate("MainWindow", "get record"))
        self.BT_ChangePassword.setText(_translate("MainWindow", "update password"))
        self.LB_Setnet.setText(_translate("MainWindow", "Enter setnet: "))
        self.LB_SetnetLogin.setText(_translate("MainWindow", "Enter setnet login: "))
        self.BT_GeneratePassword.setText(_translate("MainWindow", "generate"))
        self.BT_SavePassword.setText(_translate("MainWindow", "save"))
        self.BT_Get.setText(_translate("MainWindow", "get"))
        self.BT_close_win.setText("×")
        self.BT_hide_win.setText("—")
        self.BT_SaveNew.setText(_translate("MainWindow", "save"))
        self.openMainManu()

    def openMainManu(self):
        """Method that opens the main menu"""
        self.showMainManu()

        self.BT_ExitForMain.hide()

        self.hideCreatePasMenu()
        self.hideGetRecord()
        self.hideChangePas()

        self.BT_CopyPaste.hide()

        self.LB_Welcome.setGeometry(QtCore.QRect(110, 30, 301, 21))
        self.LB_StatusPass.setGeometry(QtCore.QRect(185, 265, 251, 21))
        self.LB_Welcome.setText("Welcome to PassManager")
        self.LB_StatusPass.setText("")
        self.LINEED_Password.clear()
        self.LINEED_SetnetLogin.clear()
        self.LINEED_Setnet.clear()

    def openCreatePasMenu(self):
        """Method that reveals the section interface ("Create record")"""
        self.showCreatePasMenu()
        self.hideMainManu()

        self.LB_Welcome.setText("create record")
        self.LB_Welcome.setGeometry(QtCore.QRect(170, 30, 301, 21))
        self.BT_ExitForMain.setGeometry(QtCore.QRect(245, 230, 130, 25))

        self.LB_SetnetPass.setText("Enter password: ")
        self.LINEED_Password.setGeometry(QtCore.QRect(247, 195, 120, 19))

    def openGetRecord(self):
        """Method that reveals the section interface ("get record")"""
        self.hideMainManu()
        self.hideCreatePasMenu()

        self.showGetRecord()

        self.LB_Welcome.setText("get record")
        self.LB_Welcome.setGeometry(QtCore.QRect(184, 30, 301, 21))
        self.LB_StatusPass.setGeometry(QtCore.QRect(110, 220, 300, 25))
        self.BT_ExitForMain.setGeometry(QtCore.QRect(245, 187, 130, 25))

    def openChangePas(self):
        """Method that opens the section interface ("update record")"""
        self.hideCreatePasMenu()
        self.hideMainManu()
        self.hideGetRecord()

        self.showChangePas()
        self.BT_ExitForMain.setGeometry(QtCore.QRect(320, 230, 120, 25))
        self.LB_Welcome.setGeometry(QtCore.QRect(155, 30, 301, 21))
        self.LB_Welcome.setText("update password")
        self.LB_SetnetPass.setText("Enter new password: ")
        self.LB_SetnetPass.setGeometry(QtCore.QRect(100, 187, 185, 25))
        self.LINEED_Password.setGeometry(QtCore.QRect(290, 190, 120, 19))

    def hideMainManu(self):
        """Method that hides main menu interface elements"""
        self.BT_createRecord.hide()
        self.BT_getRecord.hide()
        self.BT_ChangePassword.hide()

    def hideCreatePasMenu(self):
        """Method that hides menu interface elements for creating an entry"""
        self.LB_SetnetPass.hide()
        self.LB_Setnet.hide()
        self.LB_SetnetLogin.hide()

        self.LINEED_Setnet.hide()
        self.LINEED_SetnetLogin.hide()
        self.LINEED_Password.hide()

        self.BT_GeneratePassword.hide()
        self.BT_SavePassword.hide()

    def hideGetRecord(self):
        """Method that hides menu interface elements to obtain a password"""
        self.LB_Setnet.hide()
        self.LB_SetnetLogin.hide()
        self.LINEED_Setnet.hide()
        self.LINEED_SetnetLogin.hide()
        self.BT_Get.hide()
        self.BT_ExitForMain.hide()

    def hideChangePas(self):
        """Method that hides menu interface elements for changing password"""
        self.LINEED_Password.hide()
        self.LINEED_Setnet.hide()
        self.LINEED_SetnetLogin.hide()

        self.LB_SetnetPass.hide()
        self.LB_Setnet.hide()
        self.LB_SetnetLogin.hide()

        self.BT_SaveNew.hide()
        self.BT_ExitForMain.hide()
        self.BT_Delete.hide()

    def showMainManu(self):
        """Method that reveals main menu interface elements"""
        self.BT_createRecord.show()
        self.BT_getRecord.show()
        self.BT_ChangePassword.show()

    def showCreatePasMenu(self):
        """A method that exposes menu interface elements for creating an entry"""
        self.LB_SetnetPass.show()
        self.LB_Setnet.show()
        self.LB_SetnetLogin.show()

        self.LINEED_Setnet.show()
        self.LINEED_SetnetLogin.show()
        self.LINEED_Password.show()

        self.BT_GeneratePassword.show()
        self.BT_SavePassword.show()
        self.BT_ExitForMain.show()

    def showGetRecord(self):
        """A method that opens menu interface elements to obtain a password"""
        self.LB_Setnet.show()
        self.LB_SetnetLogin.show()
        self.LINEED_Setnet.show()
        self.LINEED_SetnetLogin.show()
        self.BT_Get.show()
        self.BT_ExitForMain.show()

    def showChangePas(self):
        """A method that opens menu interface elements to change the password"""
        self.LINEED_Password.show()
        self.LINEED_Setnet.show()
        self.LINEED_SetnetLogin.show()

        self.LB_SetnetPass.show()
        self.LB_Setnet.show()
        self.LB_SetnetLogin.show()

        self.BT_SaveNew.show()
        self.BT_ExitForMain.show()
        self.BT_Delete.show()


    def openTG(self):
        """Method for opening a link using a button"""
        TgInfo_url = QUrl('Enter link')
        QDesktopServices.openUrl(TgInfo_url)


class Ui_Authorization(object):
    """A class that creates objects for the design of the login window"""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(309, 220)
        MainWindow.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LB_MainFon = QtWidgets.QLabel(parent=self.centralwidget)
        self.LB_MainFon.setGeometry(QtCore.QRect(-2, -1, 311, 241))
        self.LB_MainFon.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.LB_MainFon.setText("")
        self.LB_MainFon.setObjectName("LB_MainFon")
        self.LB_Login = QtWidgets.QLabel(parent=self.centralwidget)
        self.LB_Login.setGeometry(QtCore.QRect(10, 50, 111, 31))
        self.LB_Login.setStyleSheet("color:white;\n"
"font: 12pt \"Arial Rounded MT Bold\";")
        self.LB_Login.setObjectName("LB_Login")
        self.LB_Pass = QtWidgets.QLabel(parent=self.centralwidget)
        self.LB_Pass.setGeometry(QtCore.QRect(10, 100, 151, 31))
        self.LB_Pass.setStyleSheet("color:white;\n"
"font: 12pt \"Arial Rounded MT Bold\";")
        self.LB_Pass.setObjectName("LB_Pass")
        self.LINEED_Login = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.LINEED_Login.setGeometry(QtCore.QRect(110, 55, 113, 22))
        self.LINEED_Login.setStyleSheet("QLineEdit {\n"
" background-color: rgb(45, 45, 45);\n"
"border: 1px solid rgb(80,80,80);\n"
"border-radius: 2px;\n"
"color: white;\n"
"font: 10pt \"Arial Rounded MT Bold\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 1px solid red;\n"
"}")
        self.LINEED_Login.setObjectName("LINEED_Login")
        self.LINEED_Password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.LINEED_Password.setGeometry(QtCore.QRect(147, 105, 113, 22))
        self.LINEED_Password.setStyleSheet("QLineEdit {\n"
" background-color: rgb(45, 45, 45);\n"
"border: 1px solid rgb(80,80,80);\n"
"border-radius: 2px;\n"
"color:white;\n"
"font: 10pt \"Arial Rounded MT Bold\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 1px solid red;\n"
"}")
        self.LINEED_Password.setObjectName("LINEED_Password")
        self.BT_SignIn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BT_SignIn.setGeometry(QtCore.QRect(80, 150, 135, 30))
        self.BT_SignIn.setStyleSheet("QPushButton {\n"
"background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"border: 2px solid red;\n"
"border-radius: 7px;\n"
"font: 12pt \"Arial Rounded MT Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(50,50,50);\n"
"}")
        self.BT_SignIn.setObjectName("BT_SignIn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Data"))
        self.LB_Login.setText(_translate("MainWindow", "Enter login:"))
        self.LB_Pass.setText(_translate("MainWindow", "Enter password:"))
        self.BT_SignIn.setText(_translate("MainWindow", "Sign in"))


class designAccountCreator(object):
    """Class describing the design of the account creation window"""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(444, 249)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LB_Main = QtWidgets.QLabel(parent=self.centralwidget)
        self.LB_Main.setGeometry(QtCore.QRect(-2, -1, 451, 251))
        self.LB_Main.setStyleSheet("background-color: rgb(30,30,30);")
        self.LB_Main.setText("")
        self.LB_Main.setObjectName("LB_Main")
        self.LB_Welcome = QtWidgets.QLabel(parent=self.centralwidget)
        self.LB_Welcome.setGeometry(QtCore.QRect(130, 20, 171, 31))
        self.LB_Welcome.setStyleSheet("font: 16pt \"Arial Rounded MT Bold\";\n"
"color:white;")
        self.LB_Welcome.setObjectName("LB_Welcome")
        self.LB_Login = QtWidgets.QLabel(parent=self.centralwidget)
        self.LB_Login.setGeometry(QtCore.QRect(30, 80, 141, 31))
        self.LB_Login.setStyleSheet("font: 14pt \"Arial Rounded MT Bold\";\n"
"color:white;")
        self.LB_Login.setObjectName("LB_Login")
        self.LB_Password = QtWidgets.QLabel(parent=self.centralwidget)
        self.LB_Password.setGeometry(QtCore.QRect(20, 140, 181, 21))
        self.LB_Password.setStyleSheet("font: 14pt \"Arial Rounded MT Bold\";\n"
"color:white;")
        self.LB_Password.setObjectName("LB_Password")
        self.LINEED_Login = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.LINEED_Login.setGeometry(QtCore.QRect(170, 85, 121, 22))
        self.LINEED_Login.setStyleSheet("QLineEdit {\n"
" background-color: rgb(45, 45, 45);\n"
"border: 1px solid rgb(80,80,80);\n"
"border-radius: 2px;\n"
"color:white;\n"
"font: 10pt \"Arial Rounded MT Bold\";\n"
"}\n"
"QLineEdit:focus{\n"
"border: 1px solid red;\n"
"}")
        self.LINEED_Login.setObjectName("LINEED_Login")
        self.LINEED_Password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.LINEED_Password.setGeometry(QtCore.QRect(207, 138, 121, 22))
        self.LINEED_Password.setStyleSheet("QLineEdit {\n"
" background-color: rgb(45, 45, 45);\n"
"border: 1px solid rgb(80,80,80);\n"
"border-radius: 2px;\n"
"color:white;\n"
"font: 10pt \"Arial Rounded MT Bold\";\n"
"}\n"
"QLineEdit:focus{\n"
"border: 1px solid red;\n"
"}")
        self.LINEED_Password.setObjectName("LINEED_Password")
        self.WIDGT_UnderWelcome = QtWidgets.QWidget(parent=self.centralwidget)
        self.WIDGT_UnderWelcome.setGeometry(QtCore.QRect(80, 55, 280, 2))
        self.WIDGT_UnderWelcome.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.WIDGT_UnderWelcome.setObjectName("WIDGT_UnderWelcome")
        self.BT_Append = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BT_Append.setGeometry(QtCore.QRect(140, 190, 151, 31))
        self.BT_Append.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: white;\n"
"    border: 2px solid red;\n"
"    border-radius: 7px;\n"
"    font: 12pt \"Arial Rounded MT Bold\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(50, 50, 50);\n"
"}")
        self.BT_Append.setObjectName("BT_Append")
        self.BT_close_win = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BT_close_win.setGeometry(QtCore.QRect(415, 3, 25, 25))
        self.BT_close_win.setStyleSheet("QPushButton {\n"
                                        "font-size: 20pt;\n"
                                        "background-color: rgba(255, 85, 0, 0);\n"
                                        "color: white;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgba(255, 255, 255, 60);\n"
                                        "    border-radius: 4px;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color: rgba(255, 255, 255, 90);\n"
                                        "    border-radius: 4px;\n"
                                        "}")


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LB_Welcome.setText(_translate("MainWindow", "Account creator"))
        self.LB_Login.setText(_translate("MainWindow", "Account login:"))
        self.LB_Password.setText(_translate("MainWindow", "Account password:"))
        self.BT_Append.setText(_translate("MainWindow", "create"))
        self.BT_close_win.setText("×")

