import sys

#// PyQt5
from PyQt5.QtWidgets import QApplication

#// Castom imports
from logic import MainWindow

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())