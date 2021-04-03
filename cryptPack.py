import sys
import secrets
import logging
from cryptUI import *
from PySide2 import QtCore, QtGui, QtWidgets

FORMAT = logging.Formatter('%(asctime)-15s %(thread)x:: %(message)s')
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(FORMAT)
log.addHandler(ch)

class Vigenre_Method:
    def init(self):
        self.key = None
        self.input_text = None
        self.output_text = None

    def apply_method(self, plain_text, method, key):
        key_index = 0
        output = ''
        if len(key) == 0 or not key:
            return
        for i in range(len(plain_text)):
            plain_char = ord(plain_text[i])
            key_char = ord(key[key_index])
            
            if method:
                output_char = (plain_char + key_char) % 127
                output_char += 33
            else:
                output_char = ((plain_char-33) - key_char) % 127
            if output_char < 33 or output_char > 127:
                log.error(f"Error: output was a control character {output_char}")
            output += chr(output_char)
            log.debug(f"add plain char {plain_char} and key char {key_char} and got {output_char}")
            key_index = (key_index + 1) % len(key) 
        return (output, key)

class Controller:
    def __init__(self,ui):
        self.ui = ui
        self.init_UI()
        self.Vigenere = Vigenre_Method()

    def init_UI(self):
        self.ui.cipher_exec.pressed.connect(self.execute_method)

    def execute_method(self):
        plain_text = self.ui.input_textEdit.toPlainText()
        key = self.ui.key_lineEdit.text()
        if not self.ui.encrypt_radioButton.isChecked() and not self.ui.decrypt_radioButton.isChecked():
            log.error("Error: no method selected")
            return
        elif self.ui.encrypt_radioButton.isChecked():
            method = True
        elif self.ui.decrypt_radioButton.isChecked():
            method = False
        log.info(f"performing encryption {method} with key {key} on text {plain_text}")
        log.info("Performing Vegenere")
        output = self.Vigenere.apply_method(plain_text,method,key)
        log.info(f"received an output text of {output[0]} and key {output[1]}")
        self.ui.output_text.setText(output[0])
        self.ui.key_lineEdit.setText(output[1])


def main():
    app = QtWidgets.QApplication(sys.argv)
    Crypt_Gui = QtWidgets.QMainWindow()
    ui = Ui_Crypt_Gui()
    ui.setupUi(Crypt_Gui)
    controller = Controller(ui)
    Crypt_Gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

            