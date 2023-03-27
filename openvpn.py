from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
import subprocess

class OpenVPNDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("OpenVPN Connector")
        self.setWindowModality(Qt.ApplicationModal)

        self.server_label = QLabel("Server:")
        self.server_input = QLineEdit()
        self.port_label = QLabel("Port:")
        self.port_input = QLineEdit()
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.connect_button = QPushButton("Connect")
        self.disconnect_button = QPushButton("Disconnect")
        self.disconnect_button.setEnabled(False)

        self.layout = QVBoxLayout()
        self.server_layout = QHBoxLayout()
        self.username_layout = QHBoxLayout()
        self.password_layout = QHBoxLayout()
        self.button_layout = QHBoxLayout()

        self.server_layout.addWidget(self.server_label)
        self.server_layout.addWidget(self.server_input)
        self.server_layout.addWidget(self.port_label)
        self.server_layout.addWidget(self.port_input)
        self.username_layout.addWidget(self.username_label)
        self.username_layout.addWidget(self.username_input)
        self.password_layout.addWidget(self.password_label)
        self.password_layout.addWidget(self.password_input)
        self.button_layout.addWidget(self.connect_button)
        self.button_layout.addWidget(self.disconnect_button)

        self.layout.addLayout(self.server_layout)
        self.layout.addLayout(self.username_layout)
        self.layout.addLayout(self.password_layout)
        self.layout.addLayout(self.button_layout)

        self.setLayout(self.layout)
        self.connect_button.clicked.connect(self.connect_to_vpn)
        self.disconnect_button.clicked.connect(self.disconnect_from_vpn)

    def connect_to_vpn(self):
        server = self.server_input.text()
        port = self.port_input.text()
        username = self.username_input.text()
        password = self.password_input.text()

        command = f"openvpn --config {server}:{port} --auth-user-pass <(echo '{username}\n{password}')"

        subprocess.Popen(command, shell=True)

        self.disconnect_button.setEnabled(True)
        self.connect_button.setEnabled(False)

    def disconnect_from_vpn(self):
        subprocess.Popen("killall openvpn", shell=True)

        self.disconnect_button.setEnabled(False)
        self.connect_button.setEnabled(True)
        
if __name__ == "__main__":
    app = QApplication([])
    dialog = OpenVPNDialog()
    dialog.show()
    app.exec_()
