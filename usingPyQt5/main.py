import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import mainWindow_CVtest_backup

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = mainWindow_CVtest_backup.Ui_Form()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

