import sys
import subprocess
import optparse
import re
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton


class ChangeMacAddress(QWidget):
    def __init__(self):
        super().__init__()

        self.interface_label = QLabel('Interface:', self)
        self.interface_label.move(20, 20)

        self.interface_edit = QLineEdit(self)
        self.interface_edit.move(100, 20)

        self.new_mac_label = QLabel('New MAC:', self)
        self.new_mac_label.move(20, 50)

        self.new_mac_edit = QLineEdit(self)
        self.new_mac_edit.move(100, 50)

        self.submit_button = QPushButton('Change MAC', self)
        self.submit_button.move(20, 80)

        self.result_label = QLabel('', self)
        self.result_label.move(20, 110)

        self.submit_button.clicked.connect(self.change_mac)

    def change_mac(self):
        interface = self.interface_edit.text()
        new_mac = self.new_mac_edit.text()

        print('[+] Changing Mac address for' +interface + 'to' + new_mac)
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
        subprocess.call(["ifconfig", interface, "up"])

        self.result_label.setText('MAC changed successfully!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChangeMacAddress()
    window.show()
    sys.exit(app.exec_())
