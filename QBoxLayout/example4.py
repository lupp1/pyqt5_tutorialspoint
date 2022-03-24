import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    win = QWidget()

    b1 = QPushButton("Button 1")
    b2 = QPushButton("Button 2")

    vbox = QVBoxLayout()
    vbox.addWidget(b1)
    vbox.addStretch()
    vbox.addWidget(b2)
    hbox = QHBoxLayout()

    b3 = QPushButton("Button 3")
    b4 = QPushButton("Button 4")
    hbox.addWidget(b3)
    hbox.addStretch()
    hbox.addWidget(b4)

    vbox.addStretch()
    vbox.addLayout(hbox)
    win.setLayout(vbox)

    win.setWindowTitle("PyQt5")
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()



