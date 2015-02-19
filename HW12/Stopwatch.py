# John M Flaherty HW12

from Tkinter import *
import time

class Stopwatch:
    def __init__(self, entry):
        self.entry = entry
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.entry.insert(0, str(self))
        self.time = 0
        self.holdUP = True 

    def __str__(self):
        return "%d:%02d:%04.1f" %(self.hours, self.minutes, self.seconds)

    def update(self):
        if self.holdUP == False:
            t = time.time() - self.time
            self.hours = t / 3600
            self.minutes = (t / 60) % 60
            self.seconds = t % 60
            self.entry.delete(0, END)
            self.entry.insert(0, str(self))
            self.entry.after(10, self.update)
        
    def start(self):
        self.holdUP = False
        self.time = time.time()
        self.entry.after(10, self.update)
        
    def stop(self):
        self.holdUP = True
        
    def clear(self):
        self.stop()
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.entry.delete(0, END)
        self.entry.insert(0, str(self))

