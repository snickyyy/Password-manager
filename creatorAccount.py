from design import designAccountCreator
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QCoreApplication
from ConnectDataBase import Tables
from Key import Key
import sys


def CreateAccount():
    """The function creates an account"""
    login = My_UI.uii.LINEED_Login.text()
    pas = My_UI.uii.LINEED_Password.text()
    data = {"Login": login, "Password": key.encryptPass(pas), "AccountHwid": 'jugug'}
    tab.Account.insert(data).execute()

class CreatorAccount(QtWidgets.QMainWindow):
    """
    A class that describes the design of the account creation window.
    """
    def __init__(self):
        super(CreatorAccount, self).__init__()

        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowIcon(QIcon(r"cfg\AuthorizateIcon.png"))

        self.uii = designAccountCreator()
        self.uii.setupUi(self)

        self.roundBorder()
        self.change_opacity()

        self.uii.BT_Append.clicked.connect(CreateAccount)
        self.uii.BT_close_win.clicked.connect(QCoreApplication.instance().quit)

    def roundBorder(self):
        radius = 6
        path = QtGui.QPainterPath()
        rect = QtCore.QRectF(self.rect())
        path.addRoundedRect(rect, radius, radius)
        region = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)

    def change_opacity(self):
        current_opacity = self.windowOpacity()
        new_opacity = 0.9 if current_opacity == 1.0 else 1.0
        self.setWindowOpacity(new_opacity)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    tab = Tables()
    key = Key()
    My_UI = CreatorAccount()
    My_UI.show()
    sys.exit(app.exec())