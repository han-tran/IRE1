#!/usr/bin/python
import os
import shutil
import os.path
import time
import numpy as np
from optparse import OptionParser
import csv
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib import colors
from scipy.stats import norm
from scipy.optimize import curve_fit
import math
from matplotlib.pyplot import figure
from scipy import optimize
import pylab as py
import random
from matplotlib.colors import ListedColormap
import matplotlib.pylab as pl
import matplotlib.transforms as mtransforms
import matplotlib
from scipy import special


MainDirectoryLoad = "/Users/HanTran/curvature-bin/"
x= []
for file in os.listdir(MainDirectoryLoad):
    if file.endswith(".txt"):
        x.append(file)

Radius = []
for i in range(len(x)):
	with open(MainDirectoryLoad + "/" + x[i]) as f:
		reader = csv.reader(f, delimiter="\t")
		Start = list(reader)
		for c in range(len(Start)): 
			Start[c] = list(map(float, Start[c]))
			Radius.append(Start[c])
Radius = Radius[0]

bins = [0, 25, 75, 125, 175, 700]

column1 = 0
column2 = 0
column3 = 0
column4 = 0
column5 = 0

for i in range(len(Radius)):
	if bins[0] <= Radius[i] < bins[1]:
		column1 = column1 + 1 
	if bins[1] <= Radius[i] < bins[2]:
		column2 = column2 + 1
	if bins[2] <= Radius[i] < bins[3]:
		column3 = column3 + 1
	if bins[3] <= Radius[i] < bins[4]:
		column4 = column4 + 1
	if bins[4] <= Radius[i] < bins[5]:
		column5 = column5 + 1

colorsbar = ['#80bfff', '#96caff', '#208eff', '#004a96', '#002348']

bars = ('< 25', '25-75', '75-125', '125-175', '> 175')
y_pos = np.arange(len(bars))
plt.bar(y_pos, [column1, column2, column3, column4, column5], alpha=1, color = colorsbar, edgecolor='gray', linewidth = 2)

plt.xticks(y_pos, bars, fontsize=20, fontname='Helvetica', rotation=45)
plt.xlabel('Radius of Curvature (nm)', fontsize=20, fontname='Helvetica')
plt.ylabel('Count', fontsize=20, fontname='Helvetica')
plt.yticks(fontsize=20, fontname='Helvetica')
# plt.grid(True)
plt.savefig(MainDirectoryLoad + "barplot-curvature4bins-50each-175-cutoff.svg")
plt.savefig(MainDirectoryLoad + "barplot-curvature4bins-50each-175-cutoff.png")
plt.show()







        