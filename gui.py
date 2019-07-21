from tkinter import *
import dac
#import time
#from statistics import mean

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.voltage = ""
        self.warning = str("")
        self.voltageOK = False
        self.currentMeasurementVar = IntVar()
        self.currentMeasurementActivated = False
        self.current = 0

        self.pack()
        self.createWidgets()
        self.pack()

        #self.onUpdate()
        print(self.voltage)

    def createWidgets(self):
        self.voltageLabel = Label(self, text="Enter desired voltage")
        self.voltageLabel.pack()

        self.voltageEntry = Entry(self)
        self.voltageEntry.pack()
        self.voltageEntry.focus_set()

        self.warningStringVar = StringVar()
        self.warningStringVar.set("test")
        self.warning = Label(self, textvariable=self.warningStringVar)
        self.warning.pack()

        self.buttonSubmit = Button(self, text="Set voltage", command=self.setVoltage)
        self.buttonSubmit.pack()

        self.buttonReset = Button(self, text="RESET", fg="#f46e42", command=self.reset)
        self.buttonReset.pack()

        self.QUIT = Button(self, text="QUIT", fg="red", command=quitApp)
        self.QUIT.pack(side="bottom")

    def setVoltage(self):
        self.voltage = self.voltageEntry.get()
        #self.voltageOK = False
        print(self.voltage)
        if self.voltage == "":
            self.warningStringVar.set("Enter a value")
        elif not self.voltage.isdigit():
            self.warningStringVar.set("Enter a real number")
        elif int(self.voltage) > 3.3:
            self.warningStringVar.set("Max 3.3V!")
        else:
            dac.setVoltage(self.voltage)
            print(self.voltage)
            return

"""
    def onUpdate(self):
        
        #Look for voltage to apply
        if self.voltageOK:
            self.setVoltage(self.voltage)
            self.voltageOK = False;
            self.after(1000, self.onUpdate)
        else:
            self.after(1000, self.onUpdate)
"""

def reset(self):
        self.currentMeasurementVar.set(0)

def quitApp():
    root.destroy()


root = Tk()
root.title("Resistivity Measurement")
root.geometry("300x300")
root.protocol("WM_DELETE_WINDOW", quitApp)
app = Application(master=root)
app.pack()
root.mainloop()