#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import forms
from api.random_facade import genera_entero_random
import logging
import logging.config

logging.config.fileConfig("logger.conf")

logger = logging.getLogger("genrandLogger")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        logger.debug("Setup of form rand_int")
        self.ui = forms.rand_int.Ui_NumeroRandom()
        self.ui.setupUi(self)

        self.ui.genera_button.clicked.connect(self.random_int)

    def random_int(self):
        logger.info("random_int method has been called")
        inferior = int(self.ui.spinBox_inferior.text())
        superior = int(self.ui.spinBox_superior.text())

        logger.info(f"Generating integer between {inferior} and {superior}")
        n = genera_entero_random(inferior, superior)
        logger.info(f"Number generated: {n}")
        self.ui.label_respuesta.setText(str(n))


if __name__ == "__main__":
    logger.info("Starting...")
    app = QApplication(sys.argv)
    w = MainWindow()
    logger.info("Display GUI")
    w.show()
    sys.exit(app.exec_())