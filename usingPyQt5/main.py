import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import mainWindow_CVtest_backup
from PyQt5.QtGui import *
import icos

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(":icons/Icon.png"))
    mainWindow = QMainWindow()
    ui = mainWindow_CVtest_backup.Ui_Form()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

