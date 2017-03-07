#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

"""
Name: V_CPU (?) -> Not final
Author: Simulacrum
License: WTFPL
Made for educational purpose only.

"""


def assign():
    global counterForInputü
    counterForInput = 0

def regChecker(self, param, register):
    if(param in register):
        return True
    else:
        self.errorBoxContainer.setPlainText(self.errorBoxContainer.toPlainText() + "\nYou are trying to access a memory part not initialized yet")
        return

def inp(self, empty, inpList, empty2):
    global counterForInput
    if(counterForInput < len(inpList)):
        self.akkuContainer.setText(str(inpList[counterForInput]))
        counterForInput += 1

    else:
        self.errorBoxContainer.setPlainText("End of INP reached")


def out(self, empty, empty1, empty2): # Seems to work ?!?
    tmp = self.akkuContainer.text()
    if tmp == "":
        self.errorBoxContainer.setPlainText(self.errorBoxContainer.toPlainText() + "\nNo Akku Value. OUT skipped")
    else:
        current = self.outputContainer.text()
        self.outputContainer.setText(current + tmp + ", ")
    return

def add(self, param, empty, register):
    if (param[0] is "#"):  # Addiere X zum Akku
        currentValue = int(self.akkuContainer.text())
        newAkku = currentValue + int(param[1:])
        self.akkuContainer.setText(str(newAkku))


    elif (param[0] is "("):  # Add Value from indir. Reg
        # Cut Param
        param = param[1:len(param) - 1]
        if regChecker(self, param, register) == True:
            try:
                currentValue = int(self.akkuContainer.text())
                newAkku = currentValue + int(register[str(register[param])])
                self.akkuContainer.setText(str(newAkku))
            except KeyError:
                self.errorBoxContainer.setPlainText(
                    self.errorBoxContainer.toPlainText() + "\nYou are trying to access a memory part not initialized yet")
        return

    else:  # Add value from "register" to akku
        if regChecker(self, param, register) == True:
            currentValue = int(self.akkuContainer.text())
            newAkku = currentValue + int(register[str(param)])
            self.akkuContainer.setText(str(newAkku))
        return

    return


def sub(self, param, empty, register):
    if (param[0] is "#"):  # Addiere X zum Akku
        currentValue = int(self.akkuContainer.text())
        newAkku = currentValue - int(param[1:])
        self.akkuContainer.setText(str(newAkku))


    elif (param[0] is "("):  # Add Value from indir. Reg
        # Cut Param
        param = param[1:len(param) - 1]
        if regChecker(self, param, register) == True:
            try:
                currentValue = int(self.akkuContainer.text())
                newAkku = currentValue - int(register[str(register[param])])
                self.akkuContainer.setText(str(newAkku))
            except KeyError:
                self.errorBoxContainer.setPlainText(
                    self.errorBoxContainer.toPlainText() + "\nYou are trying to access a memory part not initialized yet")

        return

    else:  # Add value from "register" to akku
        if regChecker(self, param, register) == True:
            currentValue = int(self.akkuContainer.text())
            newAkku = currentValue - int(register[param])
            self.akkuContainer.setText(str(newAkku))

    return


def mul(self, param, empty, register):
    if (param[0] is "#"):  # Addiere X zum Akku
        currentValue = int(self.akkuContainer.text())
        newAkku = currentValue * int(param[1:])
        self.akkuContainer.setText(str(newAkku))


    elif (param[0] is "("):  # Add Value from indir. Reg
        # Cut Param
        param = param[1:len(param)-1]
        if regChecker(self, param, register) == True:
            try:
                currentValue = int(self.akkuContainer.text())
                newAkku = currentValue * int(register[str(register[param])])
                self.akkuContainer.setText(str(newAkku))
            except KeyError:
                self.errorBoxContainer.setPlainText(
                    self.errorBoxContainer.toPlainText() + "\nYou are trying to access a memory part not initialized yet")
        return

    else:  # Add value from "register" to akku
        if regChecker(self, param, register) == True:
            currentValue = int(self.akkuContainer.text())
            newAkku = currentValue * int(register[param])
            self.akkuContainer.setText(str(newAkku))

    return


def div(self, param, empty, register):
    if (param[0] is "#"):  # Addiere X zum Akku
        if(int(param[1:]) == 0):
            self.errorBoxContainer.setPlainText(
                self.errorBoxContainer.toPlainText() + "\nYou are trying to devide by 0 - skipped")
        else:
            try:
                currentValue = int(self.akkuContainer.text())
                newAkku = int(currentValue / int(param[1:]))
                self.akkuContainer.setText(str(newAkku))
            except ZeroDivisionError:
                self.errorBoxContainer.setPlainText(
                    self.errorBoxContainer.toPlainText() + "\nYou are trying to devide by 0 - skipped")


    elif (param[0] is "("):  # Add Value from indir. Reg
        # Cut Param
        param = param[1:len(param)-1]
        try:
            if regChecker(self, param, register) == True:
                try:
                    currentValue = int(self.akkuContainer.text())
                    newAkku = int(currentValue / int(register[str(register[param])]))
                    self.akkuContainer.setText(str(newAkku))
                except KeyError:
                    self.errorBoxContainer.setPlainText(
                        self.errorBoxContainer.toPlainText() + "\nYou are trying to access a memory part not initialized yet")
        except ZeroDivisionError:
            self.errorBoxContainer.setPlainText(
                self.errorBoxContainer.toPlainText() + "\nYou are trying to devide by 0 - skipped")

        return

    else:  # Add value from "register" to akku
        if regChecker(self, param, register) == True:
            try:
                currentValue = int(self.akkuContainer.text())
                newAkku = int(currentValue / int(register[param]))
                self.akkuContainer.setText(str(newAkku))
            except ZeroDivisionError:
                self.errorBoxContainer.setPlainText(
                    self.errorBoxContainer.toPlainText() + "\nYou are trying to devide by 0 - skipped")

    return

def lda(self, param, empty, register):

        if (param[0] is "#"):  # Addiere X zum Akku
            self.akkuContainer.setText(param[1:])

        elif (param[0] is "("):  # Add Value from indir. Reg
            param = param[1:len(param) - 1]
            if regChecker(self, param, register) == True:
                try:
                    self.akkuContainer.setText(str(register[str(register[param])]))
                except KeyError:
                    self.errorBoxContainer.setPlainText(
                        self.errorBoxContainer.toPlainText() + "\nYou are trying to access a memory part not initialized yet")

            return
        else:
            if regChecker(self, param, register) == True:
                self.akkuContainer.setText(str(register[param]))
            return


def sta(self, param, empty, register):
    if (param[0] is "("):  # Add Value from indir. Reg
        try:
            param = param[1:len(param) - 1]
            currentValue = self.akkuContainer.text()
            register[str(register[param])] = currentValue
        except KeyError:
            self.errorBoxContainer.setPlainText(
                self.errorBoxContainer.toPlainText() + "\nYou are trying to access a memory part not initialized yet")

        return
    else:
        currentValue = int(self.akkuContainer.text())
        register[param] = currentValue
        return

def jmp(self, param):

    for x in range(0, len(self.comList)):
        if(self.comList[x][0].count(param) == 1):
            jmpComPointer = x
            return jmpComPointer
        if(self.comList[x][0].count(param) > 1):
            self.errorBoxContainer.setPlainText(self.errorBoxContainer.toPlainText() + "\n You have used the same JMP mark more than once")
            return None
    else:
        self.errorBoxContainer.setPlainText(self.errorBoxContainer.toPlainText() + "\n No such JMP mark here")
        return None


def beq(self, param):
    param = param.split(",")
    cond = str(param[0]) # The condition to jump
    to = str(param[1])
    if(str(cond) == str(self.akkuContainer.text())):
        comPointer = int(jmp(self, to))
        return comPointer
    else:
        return "NotReached"

def end(self, param, empty, register):

    tmp = str(self.errorBoxContainer.toPlainText())
    self.errorBoxContainer.setPlainText(tmp + "\nEnd of Programm reached")
    self.isRunning = False

