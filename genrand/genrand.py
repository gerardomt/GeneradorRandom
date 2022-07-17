#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import forms
from api.random_facade import genera_entero_random, choose_from_list
import logging.config

logging.config.fileConfig("logger.conf")
logger = logging.getLogger("genrandLogger")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        logger.debug("Setup of form rand_int")
        self.ui = forms.rand_int.Ui_RandomGeneratorWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonNumber.clicked.connect(self.random_int)
        self.ui.pushButtonList.clicked.connect(self.choose_from_list)

    def random_int(self):
        """Slot that reads the values in spinBoxLower and spinBoxUpper and
        display a random generated integer between these values. if the value
        in spinBoxLower is greater than spinBoxUpper, then message box is
        display
        """
        logger.info("random_int method has been called")
        lower = int(self.ui.spinBoxLower.text())
        upper = int(self.ui.spinBoxUpper.text())

        if lower > upper:
            logger.error("The lower limit is greater than the upper limit.")
            return show_warning_messagebox("The Lower limit is greater than the Upper limit")

        logger.info(f"Generating integer between {lower} and {upper}")
        n = genera_entero_random(lower, upper)
        logger.info(f"Number generated: {n}")
        self.ui.labelNumber.setText(str(n))

    def choose_from_list(self):
        """Slot that reads the text in textEditList, split this text by lines and
        display only one line randomly selected.
        """
        logger.info("Calling choose_from_list method")
        text = self.ui.textEditList.toPlainText()
        rows = []
        if text:
            rows = text.split("\n")
            rows = [r.strip() for r in rows]

        logger.info("Choosing a single line...")
        choice = choose_from_list(rows)
        logger.info(f"Line selected: {choice}")
        self.ui.labelList.setText(choice)


def show_warning_messagebox(text):
    """Slot. Display a warning message box with the passed text and
    only the ok button
    """
    logger.info("Displaying warning message box")
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)

    msg.setText(text)
    msg.setWindowTitle("Warning")

    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


if __name__ == "__main__":
    logger.info("Starting...")
    app = QApplication(sys.argv)
    w = MainWindow()
    logger.info("Display GUI")
    w.show()
    sys.exit(app.exec_())
