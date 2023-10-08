import statistics
import numpy as np
from tkinter import *


list = [1,2,3,4,5,6]

median = statistics.median(list)

standev = statistics.stdev(list)

mean =  statistics.mean(list)

print(median)
print(standev)
print(mean)

root = Tk()

mylabel = Label(root, text="hello world")

mylabel.pack()

root.mainloop()