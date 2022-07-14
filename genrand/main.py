#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import forms
from api.random_facade import genera_entero_random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = forms.rand_int.Ui_NumeroRandom()
        self.ui.setupUi(self)
        self.ui.genera_button.clicked.connect(self.random_int)

    def random_int(self):
        inferior = self.ui.spinBox_inferior.text()
        superior = self.ui.spinBox_superior.text()

        n = genera_entero_random(int(inferior), int(superior))

        self.ui.label_respuesta.setText(str(n))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
