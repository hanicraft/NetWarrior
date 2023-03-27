import sys
import socket
from PySide2.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout

class ProxyConnectionDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Proxy Connection')
        self.address_label = QLabel('Proxy Address:')
        self.address_input = QLineEdit()
        self.port_label = QLabel('Proxy Port:')
        self.port_input = QLineEdit()
        self.connect_button = QPushButton('Connect')
        self.connect_button.clicked.connect(self.connect_to_proxy)
        layout = QVBoxLayout()
        layout.addWidget(self.address_label)
        layout.addWidget(self.address_input)
        layout.addWidget(self.port_label)
        layout.addWidget(self.port_input)
        layout.addWidget(self.connect_button)
        self.setLayout(layout)

    def connect_to_proxy(self):
        try:
            proxy_address = self.address_input.text()
            proxy_port = int(self.port_input.text())
            proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            proxy_socket.connect((proxy_address, proxy_port))
            print(f'Connected to proxy at {proxy_address}:{proxy_port}')
        except Exception as e:
            print(f'Error connecting to proxy: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = ProxyConnectionDialog()
    dialog.show()
    sys.exit(app.exec_())
