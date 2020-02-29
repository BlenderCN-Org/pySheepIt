#!/usr/bin/env python

from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QMainWindow, QCheckBox, QComboBox, QDateTimeEdit,
                             QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                             QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
                             QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
                             QVBoxLayout, QWidget)
import sys


class RenderWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # vertical stacked layone
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.create_authentication_group())

        self.setLayout(main_layout)


    def create_authentication_group(self):
        # build the authentication group in a grid layout
        authentication_group = QGroupBox('Authentication')

        # username
        label_username = QLabel('Username')
        text_username = QLineEdit()

        # password
        label_password = QLabel('Password')
        text_password = QLineEdit()
        text_password.setEchoMode(QLineEdit.Password)

        layout = QGridLayout()
        layout.addWidget(label_username, 0, 0, 1, 1, Qt.AlignRight)
        layout.addWidget(text_username, 0, 1, 1, 4, Qt.AlignLeft)
        layout.addWidget(label_password, 1, 0, 1, 1, Qt.AlignRight)
        layout.addWidget(text_password, 1, 1, 1, 4, Qt.AlignLeft)

        authentication_group.setLayout(layout)

        return authentication_group


class PySheepIt(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # set size/position and App title
        self.setGeometry(1100, 300, 350, 250)
        self.setWindowTitle('PySheep It!')

        # create the status bar
        self.statusBar()

        # create the central widget
        render_widget = RenderWidget()

        self.statusBar().showMessage('Ready')

        self.setCentralWidget(render_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    main_w = PySheepIt()
    main_w.show()

    sys.exit(app.exec_())
