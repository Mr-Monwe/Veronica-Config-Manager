#!/usr/bin/env python3

import sys
import time
import platform
import subprocess
from os import system, path
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
        # On append_button click execute the execute_append function
        self.ui.append_button.clicked.connect(self.execute_append)
        # On reset_button click execute the execute_reset function
        self.ui.reset_button.clicked.connect(self.execute_reset)
        # On execute_button click execute the execute_abort function
        self.ui.abort_button.clicked.connect(self.execute_abort)

    # Function to append the first parameter to the file
    def p1(self, checked):
        statement = "<launch> parameter 1 placeholder</launch>"
        if checked:
            self.ui.file_preview.append(statement)
            self.ui.file_preview.append("")
        else:
            self.ui.file_preview.undo()
            #self.ui.file_preview.append(string.replace(statement, ""))
            # pass

    # Function to append file to preview
    def execute_append(self):
        # Select all the text in the file editor
        self.ui.file_editor.selectAll()
        # Cut all the selected text in the file editor
        self.ui.file_editor.cut()
        # Append an empty line in the file preview
        self.ui.file_preview.append("")
        # Move to the beginning of the next empty block
        self.ui.file_preview.moveCursor(QtGui.QTextCursor.NextBlock)
        # Paste all the copied text into the file preview
        self.ui.file_preview.paste()
        # Append an empty line in the file preview
        self.ui.file_preview.append("")

    # Function to find the directory to save file
    def find_directory(self):
        # Pop open file explorer so user can select the directory they want to use
        directory = QtWidgets.QFileDialog.getExistingDirectory()
        # Preview the directory in the File Path window
        self.ui.text_directory_preview.setText(directory)
        self.ui.text_directory_preview.home(True)
        # On build_button click execute the execute_build function
        self.ui.build_button.clicked.connect(self.execute_build)

    # Function to build the file and save it to the specified directory
    def execute_build(self):
        # If filename is modified then allow the build to execute
        if (self.ui.file_name_input.isModified() == True):
            # Read the users input for File Name
            fileName = self.ui.file_name_input.text()
            # File Path where the file will be saved
            fileDir = self.ui.text_directory_preview.text()
            # Append the File Name to the File Path
            completeName = path.join(fileDir, fileName)
            # Create & open the writable output file
            outFile = open(completeName, "w")
            # Write the contents of the File Preview into the created file
            outFile.write(str(self.ui.file_preview.toPlainText()))
            # Close the file
            outFile.close()
            print("File Name: " + fileName)
            print("Is Saved In Directory:" + fileDir)

    # Function to (Reset) the Config Manager
    def execute_reset(self):
        # Uncheck all check boxes
        self.ui.checkBox_p1.setChecked(False)
        self.ui.checkBox_p2.setChecked(False)
        self.ui.checkBox_p3.setChecked(False)
        self.ui.checkBox_p4.setChecked(False)
        self.ui.checkBox_p5.setChecked(False)
        self.ui.checkBox_p6.setChecked(False)
        self.ui.checkBox_p7.setChecked(False)
        self.ui.checkBox_p8.setChecked(False)
        self.ui.checkBox_p9.setChecked(False)
        self.ui.checkBox_p10.setChecked(False)
        self.ui.checkBox_p11.setChecked(False)
        self.ui.checkBox_p12.setChecked(False)
        self.ui.checkBox_p13.setChecked(False)
        self.ui.checkBox_p14.setChecked(False)
        self.ui.checkBox_p15.setChecked(False)
        self.ui.checkBox_p16.setChecked(False)
        # Clear all the text in the file editor
        self.ui.file_editor.clear()
        # Clear all the text in the file preview
        self.ui.file_preview.clear()
        # Clear the filename being displayed
        self.ui.file_name_input.clear()
        # Clear the current directory being displayed
        self.ui.text_directory_preview.clear()

    # Function to (Close) the Config Manager
    def execute_abort(self):
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
