import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    w = QWidget()

    b = QPushButton(w)
    b.setText("Hello world")
    b.move(50, 20)

    w.setGeometry(100, 100, 300, 100)
    w.setWindowTitle("PyQt5 Window")
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()