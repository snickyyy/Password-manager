from ConnectDataBase import Tables, db
from design import Ui_MainWindow, Ui_Authorization
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QIcon
from pyperclip import copy
from Key import Key
from discord import turnDiscord
import sys


class PasswordHandler:
    """
    A class that takes into account the processing of operations, ownership with owners: generation, creation of records,
    receiving records, copying records to the buffer, sharing, updating and deleting records,
    as well as user authorization.
    """
    def __init__(self):
        """Initializer of a class that has a password attribute for copying to the buffer"""
        self.password = None

    def passwordGen(self):
        """
        Generates a strong password and displays it in the password field on the interface.
        """
        My_UI.ui.LINEED_Password.setText("")
        My_UI.ui.LINEED_Password.setText(key.generatePass())

    def createRecord(self):
        """
        Creates an entry with a password, login and social network name.
        Checks the password for complexity, encrypts it and saves it to the database.
        """
        Pass = My_UI.ui.LINEED_Password.text()
        SetLog = My_UI.ui.LINEED_SetnetLogin.text()
        SetNet = My_UI.ui.LINEED_Setnet.text()
        if key.password_checker(Pass)[0]:
            dic = {"Sotnet": SetNet, "LoginSotNet": SetLog, "Password": key.encryptPass(Pass)}
            tab.Passwords.insert(dic).execute()
            My_UI.ui.LB_StatusPass.setText("successfully")
        else:
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("Пароль слишком простой.\n\n"
                          "Хороший пароль должен включать в себя:\n"
                          "- Не менее 8 символов\n"
                          "- 1 заглавную букву\n"
                          "- 1 маленькую букву\n"
                          "- 1 цифру\n"
                          "- 1 специальный символ\n\n"
                          "Для генерации надежного пароля нажмите кнопку generate")
            error.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint, True)
            error.exec()

    def getReocrd(self):
        """
         Receives and decrypts a password from the database using the specified social network name and login.
         """

        setnet = My_UI.ui.LINEED_Setnet.text()
        setnetLogin = My_UI.ui.LINEED_SetnetLogin.text()
        ress = tab.Passwords.select().where((Tables.Passwords.LoginSotNet == setnetLogin) & (Tables.Passwords.Sotnet == setnet))
        if ress:
            res = key.decrypt(str(*ress))
            My_UI.ui.LB_StatusPass.setText(f"Password: {res}")
            My_UI.ui.BT_CopyPaste.show()
            self.password = res
        else:
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("Данные указаны не верно")
            error.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint, True)
            error.exec()

    def CopyPaste(self):
        """
        Saves the password to the clipboard.
        """
        copy(self.password)

    def UpdatePass(self):
        """
        Updates the password in the database.
        """
        OLDsetnet = My_UI.ui.LINEED_Setnet.text()
        OLDsetnetLogin = My_UI.ui.LINEED_SetnetLogin.text()
        newPass = My_UI.ui.LINEED_Password.text()
        if key.password_checker(newPass)[0]:
            tab.Passwords.update(Password= key.encryptPass(newPass)).where((tab.Passwords.Sotnet == OLDsetnet) & (tab.Passwords.LoginSotNet == OLDsetnetLogin)).execute()
            My_UI.ui.LB_StatusPass.setText("successfully")
        else:
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("Пароль слишком простой.\n\n"
                          "Хороший пароль должен включать в себя:\n"
                          "- Не менее 8 символов\n"
                          "- 1 заглавную букву\n"
                          "- 1 маленькую букву\n"
                          "- 1 цифру\n"
                          "- 1 специальный символ\n\n"
                          "Для генерации надежного пароля нажмите кнопку generate")
            error.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint, True)
            error.exec()

    def DeleteRecord(self):
        """
        Deletes an entry from the database.
        """
        setnet = My_UI.ui.LINEED_Setnet.text()
        setnetLogin = My_UI.ui.LINEED_SetnetLogin.text()

        tab.Passwords.delete().where((tab.Passwords.Sotnet == setnet) & (tab.Passwords.LoginSotNet == setnetLogin)).execute()
        My_UI.ui.LB_StatusPass.setText("successfully")

    def authorization(self):
        """
        Performs user authorization.
        """
        login = UI_AU.uii.LINEED_Login.text()
        password = UI_AU.uii.LINEED_Password.text()
        flag = tab.Account.select(tab.Account.Password).where(tab.Account.Login == login).execute()
        decPass = key.decrypt(str(*flag))
        if decPass == password:
            My_UI.show()
            UI_AU.close()
            self.AuthorizatePass = str(*flag)
        else:
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("Пароль не правильный")
            error.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint, True)
            error.exec()


class MainWindow(QtWidgets.QMainWindow):
    """Class describing the design of the main window"""
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowIcon(QIcon(r"cfg\MainIco.png"))

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.roundBorder()
        self.change_opacity()

        self.old_pos = None

        self.ui.BT_createRecord.clicked.connect(self.ui.openCreatePasMenu)
        self.ui.BT_getRecord.clicked.connect(self.ui.openGetRecord)
        self.ui.BT_ExitForMain.clicked.connect(self.ui.openMainManu)
        self.ui.BT_ChangePassword.clicked.connect(self.ui.openChangePas)
        self.ui.BT_SavePassword.clicked.connect(PasswordHandler.createRecord)
        self.ui.BT_GeneratePassword.clicked.connect(pas.passwordGen)
        self.ui.BT_Get.clicked.connect(pas.getReocrd)
        self.ui.BT_CopyPaste.clicked.connect(pas.CopyPaste)
        self.ui.BT_SaveNew.clicked.connect(pas.UpdatePass)
        self.ui.BT_Delete.clicked.connect(pas.DeleteRecord)

        self.ui.BT_close_win.clicked.connect(QCoreApplication.instance().quit)
        self.ui.BT_hide_win.clicked.connect(self.showMinimized)
        self.ui.BT_Info.clicked.connect(self.ui.openTG)

    def mousePressEvent(self, event):
        """
        Remembers the mouse position when clicked to implement window movement.
        """
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        """
        Handles window movement.
        """
        if self.old_pos:
            delta = event.globalPosition().toPoint() - self.old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        """
        Resets the mouse position when the button is released.
        """
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.old_pos = None

    def roundBorder(self):
        """
        Rounds the corners of the window.
        """
        radius = 7
        path = QtGui.QPainterPath()
        rect = QtCore.QRectF(self.rect())
        path.addRoundedRect(rect, radius, radius)
        region = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)

    def change_opacity(self):
        """
          Makes the window transparent.
          """
        current_opacity = self.windowOpacity()
        new_opacity = 0.9 if current_opacity == 1.0 else 1.0
        self.setWindowOpacity(new_opacity)


class WindowAuthorization(QtWidgets.QMainWindow):
    """
    A class that describes the design of the login window.
    """
    def __init__(self):
        super(WindowAuthorization, self).__init__()

        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowIcon(QIcon(r"cfg\AuthorizateIcon.png"))

        self.uii = Ui_Authorization()
        self.uii.setupUi(self)

        self.roundBorder()
        self.change_opacity()

        self.uii.BT_SignIn.clicked.connect(pas.authorization)

    def roundBorder(self):
        """The method rounds the login window"""
        radius = 6
        path = QtGui.QPainterPath()
        rect = QtCore.QRectF(self.rect())
        path.addRoundedRect(rect, radius, radius)
        region = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)

    def change_opacity(self):
        """The method makes the login window transparent"""
        current_opacity = self.windowOpacity()
        new_opacity = 0.9 if current_opacity == 1.0 else 1.0
        self.setWindowOpacity(new_opacity)


if __name__ == "__main__":
    """
    Launches a status in discord, creates class objects, launches a window.
    """
    turnDiscord()
    tab = Tables()
    key = Key()
    pas = PasswordHandler()

    app = QtWidgets.QApplication(sys.argv)
    My_UI = MainWindow()
    UI_AU = WindowAuthorization()
    UI_AU.show()
    sys.exit(app.exec())
