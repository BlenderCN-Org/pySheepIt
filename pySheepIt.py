#!/usr/bin/env python

from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel, QMainWindow, QProgressBar, QVBoxLayout,
                               QWidget)
import sys


class RenderWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # stack the different panels vertically
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.create_project_section())
        main_layout.addSpacing(15)
        main_layout.addWidget(self.create_global_stats_section())

        self.setLayout(main_layout)

    def create_project_section(self):
        gbox_active_project = QGroupBox('Project')

        lbl_project_name = QLabel('Name:')
        self.lbl_project_name_value = QLabel('')

        lbl_elapsed_time = QLabel('Elapsed Time:')
        self.lbl_elapsed_time_value = QLabel('')

        lbl_remaining_time = QLabel('Remaining time:')
        self.lbl_remaining_time_value = QLabel('')

        lbl_step = QLabel('Current Step:')
        self.lbl_step_value = QLabel('')

        self.pbar_completion = QProgressBar()
        self.pbar_completion.setValue(0)

        # organise the fields in a grid
        layout = QGridLayout()
        layout.addWidget(lbl_project_name, 0, 0, Qt.AlignRight)
        layout.addWidget(self.lbl_project_name_value, 0, 1, 1, 3, Qt.AlignLeft)
        layout.addWidget(lbl_elapsed_time, 1, 0, Qt.AlignRight)
        layout.addWidget(self.lbl_elapsed_time_value, 1, 1, 1, 3, Qt.AlignLeft)
        layout.addWidget(lbl_remaining_time, 2, 0, Qt.AlignRight)
        layout.addWidget(self.lbl_remaining_time_value, 2, 1, 1, 3, Qt.AlignLeft)
        layout.addWidget(lbl_step, 3, 0,Qt.AlignRight)
        layout.addWidget(self.lbl_step_value, 3, 1, 1, 3, Qt.AlignLeft)
        layout.setRowStretch(5, 40)
        layout.addWidget(self.pbar_completion, 6, 0, 1, 4, Qt.AlignCenter)

        self.pbar_completion.setMinimumWidth(gbox_active_project.width() - 200)

        gbox_active_project.setLayout(layout)

        return gbox_active_project

    def create_global_stats_section(self):
        gbox_blobal_stats = QGroupBox('Global Stats')

        lbl_active_projects = QLabel('Active projects:')
        self.lbl_active_projects_value = QLabel('')

        lbl_connected_machines = QLabel('Connected machines:')
        self.lbl_connected_machines_value = QLabel('')

        lbl_remaining_frames = QLabel('Remaining frames:')
        self.lbl_remaining_frames_value = QLabel('')

        lbl_user_points = QLabel('User\'s total points:')
        self.lbl_user_points_value = QLabel('')

        layout = QGridLayout()
        layout.addWidget(lbl_active_projects, 0, 0, Qt.AlignRight)
        layout.addWidget(self.lbl_active_projects_value, 0, 1, 1, 3, Qt.AlignLeft)
        layout.addWidget(lbl_connected_machines, 1, 0, Qt.AlignRight)
        layout.addWidget(self.lbl_connected_machines_value, 1, 1, 1, 3, Qt.AlignLeft)
        layout.addWidget(lbl_remaining_frames, 2, 0, Qt.AlignRight)
        layout.addWidget(self.lbl_remaining_frames_value, 2, 1, 1, 3, Qt.AlignLeft)
        layout.addWidget(lbl_user_points, 3, 0, Qt.AlignRight)
        layout.addWidget(self.lbl_user_points_value, 3, 1, 1, 3, Qt.AlignLeft)

        gbox_blobal_stats.setLayout(layout)

        return gbox_blobal_stats


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

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    main_w = PySheepIt()

    sys.exit(app.exec_())
