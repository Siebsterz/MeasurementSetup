import tkinter
from tkinter import Button
from tkinter import Entry
from tkinter import Label
from tkinter import StringVar
import RPi.GPIO
import sys
import dac
RPi.GPIO.setmode(RPi.GPIO.BCM)

## hardware

##GUI DEFINITIONS
root = tkinter.Tk()
root.title("Resistivity Measurement")

##VARIABLES
voltageWarning = StringVar()
voltageON = False
currentON = False

##FUNCTIONS
def setCurrent():
    print("Hello world")
    currentButton.config(text = "ON")

def setVoltage():
    voltage = voltageEntry.get()
    if voltage == "":
        voltageWarning.set("No voltage specified")
    elif not isDigit(voltage):
        voltageWarning.set("Enter a real number")
    elif float(voltage) > 5:
        voltageWarning.set("Voltage capped at 5V")
        dac.DACVoltage(voltage)
        voltageButtonON.config(text = "Voltage ON")
    else:
        voltageWarning.set("")
        dac.DACVoltage(voltage)
        voltageButtonON.config(text = "Voltage ON")

def turnOFFvoltage():
    dac.DACVoltage(0)
    voltageButtonON.config(text = "Set voltage")

def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def quit():
    sys.exit(0)

##WIDGETS
currentButton = Button(root, text = "Set current", command = setCurrent, bg = "red", height = 1, width = 10) 
voltageButtonON = Button(root, text = "Set voltage", command = setVoltage, bg = "green", height = 1, width = 10)
voltageButtonOFF = Button(root, text = "Turn off voltage", command = turnOFFvoltage, bg = "red", height = 1, width = 10)
voltageEntry  = Entry (root)
voltageWarningLabel = Label(root, textvariable = voltageWarning)
quitButton = Button(root, text = "Quit", command = quit, bg = "red", height = 1, width = 10) 

currentButton.grid(row = 0, column = 1)
voltageButtonON.grid(row = 1, column = 1)
voltageButtonOFF.grid(row = 1, column = 3)
voltageEntry.grid (row = 1, column = 2)
voltageEntry.focus_set()
voltageWarningLabel.grid(row= 2, column = 2)
quitButton.grid(row=3, column = 1)






root.mainloop()
