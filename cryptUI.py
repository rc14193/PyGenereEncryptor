from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Crypt_Gui(object):
    def setupUi(self, Crypt_Gui):
        Crypt_Gui.setObjectName("Crypt_Gui")
        Crypt_Gui.resize(450, 650)
        self.centralwidget = QtWidgets.QWidget(Crypt_Gui)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.title_label.setObjectName("title_label")
        self.verticalLayout_2.addWidget(self.title_label)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.info_label = QtWidgets.QLabel(self.frame)
        self.info_label.setAutoFillBackground(False)
        self.info_label.setObjectName("info_label")
        self.verticalLayout_3.addWidget(self.info_label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.encrypt_radioButton = QtWidgets.QRadioButton(self.frame)
        self.encrypt_radioButton.setObjectName("encrypt_radioButton")
        self.horizontalLayout_3.addWidget(self.encrypt_radioButton)
        self.decrypt_radioButton = QtWidgets.QRadioButton(self.frame)
        self.decrypt_radioButton.setObjectName("decrypt_radioButton")
        self.horizontalLayout_3.addWidget(self.decrypt_radioButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.key_label = QtWidgets.QLabel(self.frame)
        self.key_label.setObjectName("key_label")
        self.verticalLayout_3.addWidget(self.key_label)
        self.key_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.key_lineEdit.setObjectName("key_lineEdit")
        self.verticalLayout_3.addWidget(self.key_lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gen_key_pushButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gen_key_pushButton.sizePolicy().hasHeightForWidth())
        self.gen_key_pushButton.setSizePolicy(sizePolicy)
        self.gen_key_pushButton.setObjectName("gen_key_pushButton")
        self.horizontalLayout.addWidget(self.gen_key_pushButton)
        self.max_pushButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_pushButton.sizePolicy().hasHeightForWidth())
        self.max_pushButton.setSizePolicy(sizePolicy)
        self.max_pushButton.setObjectName("max_pushButton")
        self.horizontalLayout.addWidget(self.max_pushButton)
        self.key_len_spinBox = QtWidgets.QSpinBox(self.frame)
        self.key_len_spinBox.setObjectName("key_len_spinBox")
        self.horizontalLayout.addWidget(self.key_len_spinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.input_label = QtWidgets.QLabel(self.frame)
        self.input_label.setObjectName("input_label")
        self.verticalLayout_3.addWidget(self.input_label)
        self.input_textEdit = QtWidgets.QTextEdit(self.frame)
        self.input_textEdit.setObjectName("input_textEdit")
        self.verticalLayout_3.addWidget(self.input_textEdit)
        self.out_text_label = QtWidgets.QLabel(self.frame)
        self.out_text_label.setObjectName("out_text_label")
        self.verticalLayout_3.addWidget(self.out_text_label)
        self.output_text = QtWidgets.QTextEdit(self.frame)
        self.output_text.setObjectName("output_text")
        self.verticalLayout_3.addWidget(self.output_text)
        self.cipher_exec = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cipher_exec.sizePolicy().hasHeightForWidth())
        self.cipher_exec.setSizePolicy(sizePolicy)
        self.cipher_exec.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.cipher_exec.setObjectName("cipher_exec")
        self.verticalLayout_3.addWidget(self.cipher_exec)
        self.verticalLayout.addWidget(self.frame)
        Crypt_Gui.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Crypt_Gui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 30))
        self.menubar.setObjectName("menubar")
        Crypt_Gui.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Crypt_Gui)
        self.statusbar.setObjectName("statusbar")
        Crypt_Gui.setStatusBar(self.statusbar)

        self.retranslateUi(Crypt_Gui)
        QtCore.QMetaObject.connectSlotsByName(Crypt_Gui)

    def retranslateUi(self, Crypt_Gui):
        _translate = QtCore.QCoreApplication.translate
        Crypt_Gui.setWindowTitle(_translate("Crypt_Gui", "Pygenere Encryptor"))
        self.title_label.setText(_translate("Crypt_Gui", "Pygenere Encryptor"))
        self.info_label.setText(_translate("Crypt_Gui", "Message"))
        self.encrypt_radioButton.setText(_translate("Crypt_Gui", "Encrypt"))
        self.decrypt_radioButton.setText(_translate("Crypt_Gui", "Decrypt"))
        self.key_label.setText(_translate("Crypt_Gui", "Key"))
        self.gen_key_pushButton.setText(_translate("Crypt_Gui", "Generate Key"))
        self.max_pushButton.setText(_translate("Crypt_Gui", "Set Max Length"))
        self.input_label.setText(_translate("Crypt_Gui", "Input Text"))
        self.out_text_label.setText(_translate("Crypt_Gui", "Output Text"))
        self.cipher_exec.setText(_translate("Crypt_Gui", "Run"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Crypt_Gui = QtWidgets.QMainWindow()
    ui = Ui_Crypt_Gui()
    ui.setupUi(Crypt_Gui)
    Crypt_Gui.show()
    sys.exit(app.exec_())
