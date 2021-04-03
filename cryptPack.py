import sys
import secrets
import logging
from cryptUI import *
from PySide2 import QtCore, QtGui, QtWidgets

FORMAT = logging.Formatter('%(asctime)s %(thread)x:: %(message)s')
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(FORMAT)
log.addHandler(ch)
log.disabled = True

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
                output_char = ((plain_char-32) + (key_char-32)) % 94
                output_char += 32
            else:
                output_char = ((plain_char-32)-(key_char-32)) % 94
                output_char += 32
            if output_char < 32 or output_char > 126:
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
        self.ui.key_len_spinBox.setRange(0,20000)
        self.ui.input_textEdit.textChanged.connect(self.update_key_range)
        self.ui.max_pushButton.pressed.connect(self.spin_to_max_len)
        self.ui.cipher_exec.pressed.connect(self.execute_method)
        self.ui.gen_key_pushButton.pressed.connect(self.key_generator)

    def spin_to_max_len(self):
        length = len(self.ui.input_textEdit.toPlainText())
        self.ui.key_len_spinBox.setValue(length)

    def update_key_range(self):
        max_leng = len(self.ui.input_textEdit.toPlainText())
        self.ui.key_len_spinBox.setRange(0,max_leng)

    def key_generator(self):
        return_key = ''
        log.info("randomly generating key")
        if self.ui.key_len_spinBox.value() < 1:
            return
        for i in range(self.ui.key_len_spinBox.value()):
            char = secrets.randbelow(93)
            char += 32
            return_key += chr(char)
        if char < 32 or char > 126:
            log.error(f"Error: output was a control character {output_char}")
        self.ui.key_lineEdit.setText(return_key)

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

            