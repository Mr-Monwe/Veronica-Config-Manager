#!/usr/bin/env python3

import sys
import platform
import time
import subprocess
from os import system
from PyQt5 import QtCore, QtGui, QtWidgets
# Main window File
from ui_test import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.checkBox_p1.stateChanged.connect(self.p1)
        # On toolbutton click execute the find_directory function
        self.ui.toolButton.clicked.connect(self.find_directory)
        # On build_button click execute the execute_build function
        # ###self.ui.build_button.clicked.connect(self.execute_build)
        # On reset_button click execute the execute_reset function
        self.ui.reset_button.clicked.connect(self.execute_reset)
        # On execute_button click execute the execute_abort function
        self.ui.abort_button.clicked.connect(self.execute_abort)

    # Function to append the first parameter to the file
    def p1(self, checked):
        if checked:
            statement = "<parameter 1/>"
            self.ui.file_preview.append(statement)
        else:
            pass

    # Function to find the directory to save file
    def find_directory(self):
        print("Searching for directory")
        directory = QtWidgets.QFileDialog.getExistingDirectory()
        self.ui.text_directory_preview.append(directory)
        self.ui.build_button.clicked.connect(self.execute_build)
    # 👁️👄👁️

    def execute_build(self):
        print("File Built")

    def execute_reset(self):
        print("File Reset")

    def execute_abort(self):
        print("File Abort")
        self.close()


"""
# https://www.youtube.com/watch?v=uXlL2PeuLpQ&ab_channel=soumilshah1995
# https://stackoverflow.com/questions/4286036/how-to-have-a-directory-dialog
# https://www.google.com/search?sxsrf=ALeKk039W06kbtUHrBUthiE_uuKJDF0LpQ%3A1614889356949&ei=jEFBYOeYOeK1ggf4-pjAAw&q=how+to+use+path+in+pyqt5&oq=how+to+use+path+in+pyqt5&gs_lcp=Cgdnd3Mtd2l6EAM6BwgAEEcQsAM6BAgjECc6BQgAEJECOgsILhCxAxDHARCjAjoICC4QxwEQowI6BQgAELEDOggIABCxAxCDAToECAAQQzoCCAA6BwgAEIcCEBQ6BggAEBYQHjoICAAQFhAKEB46CAghEBYQHRAeUMqiCFi1kglgxJQJaAJwAngBgAGpA4gBpRySAQo3LjE3LjEuMC4xmAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=gws-wiz&ved=0ahUKEwjnjuPTu5fvAhXimuAKHXg9BjgQ4dUDCA0&uact=5
# https://www.google.com/search?q=user+select+path+in+pyqt5&oq=user+select+path+in+pyqt5&aqs=chrome..69i57.14782j0j4&sourceid=chrome&ie=UTF-8
"""

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
