import statistics
import numpy as np
import tkinter as tk


list = [1,2,3,4,5,6]

median = statistics.median(list)

standev = statistics.stdev(list)

mean =  statistics.mean(list)

print(median)
print(standev)
print(mean)