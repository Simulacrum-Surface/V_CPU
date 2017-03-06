#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

"""
Name: V_CPU (?) -> Not final
Author: Simulacrum
License: WTFPL
Made for educational purpose only.

"""

import Core
import sys
import re
import random

from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.QtCore import QTimer
from PyQt5 import QtWidgets, QtCore


class GUI_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(736, 544)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.commandContainer = QtWidgets.QTextEdit(self.centralwidget)
        self.commandContainer.setObjectName("commandContainer")
        self.verticalLayout_2.addWidget(self.commandContainer)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setObjectName("runButton")
        self.horizontalLayout_3.addWidget(self.runButton)
        self.pauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout_3.addWidget(self.pauseButton)
        #self.testButton = QtWidgets.QPushButton(self.centralwidget)
        #self.testButton.setObjectName("testButton")
        #self.horizontalLayout_3.addWidget(self.testButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.outputContainer = QtWidgets.QLineEdit(self.centralwidget)
        self.outputContainer.setObjectName("outputContainer")
        self.verticalLayout.addWidget(self.outputContainer)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.inputContainer = QtWidgets.QLineEdit(self.centralwidget)
        self.inputContainer.setObjectName("inputContainer")
        self.verticalLayout.addWidget(self.inputContainer)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.generateButton = QtWidgets.QPushButton(self.centralwidget)
        self.generateButton.setObjectName("generateButton")
        self.horizontalLayout.addWidget(self.generateButton)
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.akkuContainer = QtWidgets.QLineEdit(self.centralwidget)
        self.akkuContainer.setObjectName("akkuContainer")
        self.horizontalLayout_2.addWidget(self.akkuContainer)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.errorBoxContainer = QtWidgets.QTextEdit(self.centralwidget)
        self.errorBoxContainer.setObjectName("errorBoxContainer")
        self.verticalLayout_3.addWidget(self.errorBoxContainer)
        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setObjectName("registerButton")
        self.verticalLayout_3.addWidget(self.registerButton)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 736, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOption = QtWidgets.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        self.menuSpeed = QtWidgets.QMenu(self.menuOption)
        self.menuSpeed.setObjectName("menuSpeed")
        self.menuGenerate = QtWidgets.QMenu(self.menuOption)
        self.menuGenerate.setObjectName("menuGenerate")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSlow = QtWidgets.QAction(MainWindow)
        self.actionSlow.setCheckable(True)
        self.actionSlow.setObjectName("actionSlow")
        self.actionNormal = QtWidgets.QAction(MainWindow)
        self.actionNormal.setCheckable(True)
        self.actionNormal.setObjectName("actionNormal")
        self.actionFast = QtWidgets.QAction(MainWindow)
        self.actionFast.setCheckable(True)
        self.actionFast.setObjectName("actionFast")
        self.actionFastest = QtWidgets.QAction(MainWindow)
        self.actionFastest.setCheckable(True)
        self.actionFastest.setObjectName("actionFastest")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.action10 = QtWidgets.QAction(MainWindow)
        self.action10.setCheckable(True)
        self.action10.setObjectName("action10")
        self.action20 = QtWidgets.QAction(MainWindow)
        self.action20.setCheckable(True)
        self.action20.setObjectName("action20")
        self.action100 = QtWidgets.QAction(MainWindow)
        self.action100.setCheckable(True)
        self.action100.setObjectName("action100")
        self.actionTill0 = QtWidgets.QAction(MainWindow)
        self.actionTill0.setCheckable(True)
        self.actionTill0.setObjectName("actionTill0")
        self.actionReport = QtWidgets.QAction(MainWindow)
        self.actionReport.setObjectName("actionReport")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuSpeed.addAction(self.actionSlow)
        self.menuSpeed.addAction(self.actionNormal)
        self.menuSpeed.addAction(self.actionFast)
        self.menuSpeed.addSeparator()
        self.menuSpeed.addAction(self.actionFastest)
        self.menuGenerate.addAction(self.action10)
        self.menuGenerate.addAction(self.action20)
        self.menuGenerate.addAction(self.action100)
        self.menuGenerate.addAction(self.actionTill0)
        self.menuOption.addAction(self.menuSpeed.menuAction())
        self.menuOption.addAction(self.menuGenerate.menuAction())
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addAction(self.actionReport)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        """
        The Actions Slots/Connects
        """
        # Define Button-Slots
        self.runButton.clicked.connect(self.run)
        #self.testButton.clicked.connect(self.test)
        self.generateButton.clicked.connect(self.generate)
        self.clearButton.clicked.connect(self.clear)
        self.pauseButton.clicked.connect(self.paused)
        self.registerButton.clicked.connect(self.showRegister)

        # Define the Menu-Slots
        self.actionExit.triggered.connect(self.exit)
        self.actionNew.triggered.connect(self.newFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionLoad.triggered.connect(self.loadFile)
        self.actionHelp.triggered.connect(self.about)
        self.actionReport.triggered.connect(self.report)

        self.action20.setChecked(True) # Make 20 psRand Ints the standard amount
        self.actionNormal.setChecked(True) # Make normal Speed the default


        # Adding the SubMenu entries to groups to check them excludingly
        self.groupSpeed = QtWidgets.QActionGroup(self.menuSpeed)
        self.groupRandom = QtWidgets.QActionGroup(self.menuGenerate)

        self.action10.setActionGroup(self.groupRandom)
        self.action20.setActionGroup(self.groupRandom)
        self.action100.setActionGroup(self.groupRandom)
        self.actionTill0.setActionGroup(self.groupRandom)

        self.actionFast.setActionGroup(self.groupSpeed)
        self.actionFastest.setActionGroup(self.groupSpeed)
        self.actionNormal.setActionGroup(self.groupSpeed)
        self.actionSlow.setActionGroup(self.groupSpeed)

        # Fill the Textfields
        self.akkuContainer.setText("0")
        self.inputContainer.setText("0")

        # States
        self.isPaused = False
        self.isRunning = False
        self.comCounter = 1
        self.register = {"0": 0}


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "V_CPU"))
        self.label_3.setText(_translate("MainWindow", "Output:"))
        self.outputContainer.setToolTip(_translate("MainWindow", "The Output will appear here"))
        self.label_2.setText(_translate("MainWindow", "Input:"))
        self.inputContainer.setToolTip(
            _translate("MainWindow", "The Input Channel. Feel free to Type own Values or generate some."))
        self.generateButton.setToolTip(
            _translate("MainWindow", "Generate random values. Check the options for the possibilities."))
        self.generateButton.setText(_translate("MainWindow", "Generate"))
        self.clearButton.setToolTip(_translate("MainWindow", "Clear Input & Output."))
        self.clearButton.setText(_translate("MainWindow", "Clear I/O"))
        self.label_4.setText(_translate("MainWindow", "Current Akku:"))
        self.akkuContainer.setToolTip(_translate("MainWindow", "The Current Akku Value"))
        self.label_5.setText(_translate("MainWindow", "ErrorBox"))
        self.errorBoxContainer.setToolTip(_translate("MainWindow", "Errors appear here."))
        self.registerButton.setToolTip(_translate("MainWindow",
                                                  "<html><head/><body><p>Show the Register</p><p>The Code needs to Run first!</p></body></html>"))
        self.registerButton.setText(_translate("MainWindow", "Show Register"))
        self.label.setText(_translate("MainWindow", "Your Commands:"))
        self.commandContainer.setToolTip(_translate("MainWindow", "Your Code here..."))
        self.runButton.setToolTip(_translate("MainWindow", "Run the Code"))
        self.runButton.setText(_translate("MainWindow", "Run"))
        self.pauseButton.setToolTip(_translate("MainWindow", "Stop/Resume the running Code"))
        self.pauseButton.setText(_translate("MainWindow", "Stop"))
        #self.testButton.setToolTip(_translate("MainWindow", "Test the Code for common Errors"))
        #self.testButton.setText(_translate("MainWindow", "Test"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuOption.setTitle(_translate("MainWindow", "Opt&ion"))
        self.menuSpeed.setTitle(_translate("MainWindow", "&Speed"))
        self.menuGenerate.setTitle(_translate("MainWindow", "&Generate"))
        self.menuAbout.setTitle(_translate("MainWindow", "&About"))
        self.actionSave.setText(_translate("MainWindow", "&Save"))
        self.actionSave.setIconText(_translate("MainWindow", "Save"))
        self.actionLoad.setText(_translate("MainWindow", "&Load"))
        self.actionExit.setText(_translate("MainWindow", "&Exit"))
        self.actionSlow.setText(_translate("MainWindow", "&Slow"))
        self.actionNormal.setText(_translate("MainWindow", "&Normal"))
        self.actionFast.setText(_translate("MainWindow", "&Fast"))
        self.actionFastest.setText(_translate("MainWindow", "Fast&est"))
        self.actionHelp.setText(_translate("MainWindow", "&Help"))
        self.actionNew.setText(_translate("MainWindow", "&New"))
        self.action10.setText(_translate("MainWindow", "&10"))
        self.action20.setText(_translate("MainWindow", "&20"))
        self.action100.setText(_translate("MainWindow", "1&00"))
        self.actionTill0.setText(_translate("MainWindow", "&Till a 0 appears"))
        self.actionReport.setText(_translate("MainWindow", "&Report an Error"))

    def loadFile(self):
        filename = QFileDialog.getOpenFileName(parent=None, caption="Open File")
        if len(filename[0]) == 0:
            return
        else:
            fname = open(filename[0])
            data = fname.read()
            self.commandContainer.setPlainText(data)
            fname.close()
            data = ""
            return
        return

    def saveFile(self):
        filename = QFileDialog.getSaveFileName(parent=None, caption="Save File")
        if len(filename[0]) == 0:
            return
        else:
            fname = open(filename[0], "w")
            data = str(self.commandContainer.toPlainText())
            fname.write(data)
            fname.close()
            data = ""
            return
        return

    def newFile(self): # Clear all Textfields
        self.commandContainer.setPlainText("")
        self.akkuContainer.setText("0")
        self.outputContainer.setText("")
        self.inputContainer.setText("0")
        self.errorBoxContainer.setPlainText("")
        return

    def exit(self): #Terminates the Programm ...
        exit(self)

    def about(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("About this Programm")
        msgBox.setText("Dear User\nThis Programm was made to get a better understanding of what happens when you use Assembly.\n\n\n"
                       "\nThe Syntax is:\n\n"
                       "jumpmark[TAB]command[TAB]argument[//]comment\n\n"
                       "For Example\n\n"
                       "ABC\tLDA\t#1 // Loads 1 to Akku\n\n"
                       "to Load the Value 1 in the Akku\n\n\nJesus Christ i should hire a texter...")
        msgBox.exec()
        return

    def report(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Error-Report")
        msgBox.setText(
            "ERROR (haha): Sorry, this is not available yet")
        msgBox.exec()
        return

    def clear(self): # Clears inp & outp channel
        self.outputContainer.setText("")
        self.inputContainer.setText("0")
        return

    def generate(self): # generates a various number of random integers for the input channel
        rnd = ""
        quant = 0 # how many numbers will be generatet
        if(self.action10.isChecked()):
            quant = 10
        if(self.action20.isChecked()):
            quant = 20
        if(self.action100.isChecked()):
            quant = 100
        if(self.actionTill0.isChecked()):
            x = random.randint(0, 100) # Amount of numbers till a 0 gets added
            for i in range(0, x):
                tmp = random.randint(0, 200)
                rnd = rnd + str(tmp) + " "
            rnd = rnd + " 0"

        for i in range(0, quant-1):
            tmp = random.randint(0, 200)
            rnd = rnd + str(tmp) + " "
        self.inputContainer.setText(rnd)
        return

    def makeInpList(self):
        tmp = self.inputContainer.text()
        inputList = tmp.split(" ")
        return inputList

    def showRegister(self): # Thisplay the Register after Running
        tmp = str(self.register)
        msgBox = QMessageBox()
        if len(self.register) == 0:
            msgBox.setText("The Register is empty, run first!\n\n")
        else:
            msgBox.setText(tmp)
        msgBox.setWindowTitle("Register")
        msgBox.exec()
        return

    def getSpeed(self):
        if (self.actionSlow.isChecked()):
            return  1
        elif (self.actionNormal.isChecked()):
            return 0.5
        elif (self.actionFast.isChecked()):
            return 0.1
        elif (self.actionFastest.isChecked()):
            return 0

    def paused(self):
        if (self.isRunning == True):
            if (self.isPaused == False):
                self.isPaused = True
                self.pauseButton.setText("Resume")
            else:
                self.isPaused = False
                self.pauseButton.setText("Stop")
                self.execCommand()
        else:
            msg = str(self.errorBoxContainer.toPlainText())
            self.errorBoxContainer.setPlainText(msg + "\nThe Programm is not Running yet")

    def run(self): # Runs the programm (no shit)

        self.inputCommands = self.commandContainer.toPlainText()  # Get the Text from the commandContainer
        self.comList = self.inputCommands.splitlines()  # Now we have a String for each line in the received CommandList
        if(len(self.comList) == 0):
            tmp = str(self.errorBoxContainer.toPlainText())
            self.errorBoxContainer.setPlainText(tmp + "\n Commands are missing")
        elif(self.inputContainer.text() == ""):
            self.errorBoxContainer.setPlainText(self.errorBoxContainer.toPlainText() + "\nNo Input available")
        else:
            self.comPointer = 0
            self.comCounter = 1
            self.isPaused = False
            self.isRunning = True
            Core.assign()
            self.errorBoxContainer.setPlainText("")
            self.pauseButton.setText("Stop")

            if str(self.outputContainer.text()) != "":
                self.outputContainer.setText("")
            if(str(self.akkuContainer.text()) != "0"):
                self.akkuContainer.setText("0")



            self.commandInterpreter = {"INP": Core.inp, "OUT": Core.out, "ADD": Core.add,
                                  "SUB": Core.sub, "MUL": Core.mul, "DIV": Core.div,
                                  "LDA": Core.lda, "STA": Core.sta, "END": Core.end
                                       }


            GUI_MainWindow.execCommand(self)


    def execCommand(self): # Executes the commands line by line
        if self.isPaused != True:
            self.inpList = self.makeInpList()  # Read InputChannel
            self.inputCommands = self.commandContainer.toPlainText()  # Get the Text from the commandContainer
            self.comList = self.inputCommands.splitlines()  # Makes lines from text to elements of list

            for x in range(0, len(self.comList)):
                if (self.comList[x].count("//") > 0):  # Removes Comments
                    self.comList[x] = self.comList[x].split("//")[0]
            for x in range(0, len(self.comList)):  # Splits jumpmarks, commands, params
                self.comList[x] = (self.comList[x].split("\t"))

                for y in range(0, len(self.comList[x])):
                    self.comList[x][y] = self.comList[x][y].replace(" ", "")

            for x in range(0, len(self.comList)):  # Give all "lines" the same amount of elements
                while (len(self.comList[x]) < 3):  # with comments
                    self.comList[x].append('')

            if (len(self.comList[self.comPointer]) < 2):
                self.errorBoxContainer.setPlainText("No Param for JMP / BEQ")
            else:
                param = self.comList[self.comPointer][2]
                if self.comList[self.comPointer][1] == "JMP":
                    p = re.compile(r"[\S]{,3}")
                    m = p.match(param)
                    if (m):
                        if (Core.jmp(self, param) is not None):
                            self.comPointer = int(Core.jmp(self, param))
                        else:
                            self.comPointer += 1
                            return
                    else:
                        self.errorBoxContainer.setPlainText(
                            str(
                                self.errorBoxContainer.toPlainText()) + "\nYou've set an invalid Jump mark, Command skipped")
                        self.comPointer += 1


                elif self.comList[self.comPointer][1] == "BEQ":
                    if (param != ""):
                        p = re.compile(r"[0-9]+,[\S]{,3}")
                        m = p.match(param)
                        if (m):
                            tmpComPointer = Core.beq(self, param)
                            if tmpComPointer != "NotReached":
                                self.comPointer = tmpComPointer
                            else:
                                self.comPointer += 1
                        else:
                            tmp = str(self.errorBoxContainer.toPlainText())
                            self.errorBoxContainer.setPlainText(tmp + "\nThe param for BEQ is incorret")
                            self.comPointer += 1
                    else:
                        tmp = self.errorBoxContainer.toPlainText()
                        self.errorBoxContainer.setPlainText(tmp + "\nYou forgot the BEQ param, Command skipped")
                        self.comPointer += 1

                elif self.comList[self.comPointer][1] in self.commandInterpreter:
                    tmp = self.comList[self.comPointer][1]
                    noParam = ["INP", "OUT", "END"]

                    if tmp not in noParam:
                        tmp = self.comList[self.comPointer][2]
                        p = re.compile(r"[#(]?[0-9]+")
                        s = p.match(tmp)
                        if s:
                            self.commandInterpreter[self.comList[self.comPointer][1]](self, param, self.inpList,
                                                                                      self.register)
                            self.comPointer += 1
                        else:
                            self.errorBoxContainer.setPlainText(
                                self.errorBoxContainer.toPlainText() + "\nError on a Param")
                            self.comPointer += 1

                    else:
                        self.commandInterpreter[self.comList[self.comPointer][1]](self, param, self.inpList,
                                                                                  self.register)
                        self.comPointer += 1
                else:
                    self.errorBoxContainer.setPlainText(
                        self.errorBoxContainer.toPlainText() + "\nCommand in Line " + str(
                            self.comPointer + 1) + " is unknown")
                    self.comPointer += 1
                if (self.comPointer < len(self.comList)):
                    self.comCounter += 1
                    tmp = ui.getSpeed() * 1000
                    QTimer.singleShot(tmp, self.execCommand)
                else:
                    tmp = str(self.errorBoxContainer.toPlainText())
                    self.errorBoxContainer.setPlainText(tmp + "\nTried/Executed Commands: " + str(self.comCounter))

        else:
            return



if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUI_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

