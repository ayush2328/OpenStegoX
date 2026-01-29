# main.py
import sys
from PyQt6.QtWidgets import QApplication
from gui import OpenStegoX

app = QApplication(sys.argv)
window = OpenStegoX()
window.show()
sys.exit(app.exec())
