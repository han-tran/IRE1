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
from scipy.integrate import quad

################################################################################
###   READ ME     READ ME     READ ME     READ ME     READ ME     READ ME    ###
################################################################################


# old colors: colors = ['violet', 'navy', 'skyblue', 'green', 'orange', 'red']
# new colors names cold colors[ seagreen #00FFAA, natural turquoise #45C3B8, caribbean #42C0FB,dodgerblue #1C86EE,cobalt #6666FF, medium purple ##9370DB] 
# New color names warm colors [ purple rose #5E2D79, margenta #FF00FF, violetred #CC3299, crimson #DC143C, Bordeaux #99182C, Fleshochre #FF57721, Dark orange #ff8C00]
# bright hex colors: colors = ['#FF9000', '#00FF02', '#00FFF5', '#0D4F8B', '#EA00FF', '#FF0000']

colors = ['#00FFAA', '#45C3B8', '#42C0FB', '#1C86EE', '#6666FF', '#5E2D79', '#FF00FF', '#CC3299', '#DC143C', '#99182C', '#FF5721', '#ff8C00']


################################################################################
################################################################################
###                      DONT MAKE CHANGES BELOW HERE                        ###
################################################################################
################################################################################


################################################################################
###                             SECTION 1: DATA                              ###
################################################################################


MainDirectoryLoad = "/Users/HanTran/Diameter-plot"
#Change "MainDirectoryLoad" to folder containing .py file and .txt file with measurements. The only .txt file in this folder should be that being plottet. Other files should be removed or stored in a subfolder. 
#Diameter measurements .txt file should have each measurement group as one line and each measurement within group tab-deliminated.
#The text file cannot contain group labels (or any text not a data point). The label had been removed. They are, from top to bottom (with code corresponding to Han Tran's experiment number followed by experiment number): Foci14-18, Foci14-17, Foci14-6, Foci14-8, Foci14-16, Foci18-8, Foci20-4, FOci20-5, Foci20-6, Foci20-12, FOci20-13, Foci20-ruby2
Lines= []
for file in os.listdir(MainDirectoryLoad):
    if file.endswith(".txt"):
        Lines.append(file)
        
        
Lines = sorted(Lines)

AllLines = []
for i in range(len(Lines)):
	with open(MainDirectoryLoad + "/" + Lines[i]) as f:
		reader = csv.reader(f, delimiter="\t")
		Start = list(reader)
		for c in range(len(Start)): 
			temptemp = []
			for d in range(len(Start[c])): 
				if Start[c][d] != '':
					temptemp.append(float(Start[c][d]))
				if Start[c] == '':
					temptemp.append(0.0)
			AllLines.append(np.asarray(temptemp))


################################################################################	
###                             SECTION 2: Plots                             ###
################################################################################	

#Font size for scientific x/y ticks 

from scipy.stats import kde
		
ybar = AllLines
colorsbar = [colors[0], colors[1], colors[2], colors[3], colors[4], colors[5], colors[6], colors[7], colors[8], colors[9], colors[10], colors[11]]
plt.rc('font', size=20)
np.random.seed(123)
index = np.arange(12)
w = 0.7
fig, ax = plt.subplots()
ax.bar(index,
       height=[np.mean(yi) for yi in ybar],
       yerr=[np.std(yi) for yi in ybar],    # error bars
       lw=2, capsize=12, # error bar cap width in points
       width=w,    # bar width
       tick_label=["MEFs-mNG-1", "MEFs-mNG-2", "MEFs-mNG-3", "MEFs-mNG-4", "MEFs-mNG-5", "MEFs-mNG-6", "U2OS-mNG-1", "U2OS-mNG-2", "U2OS-mNG-3", "U2OS-mNG-4", "U2OS-mNG-5", "U2OS-mRuby-1"],
       color=colorsbar,
       alpha=0.4,
       edgecolor=colorsbar,    
       )      
ybar = np.asarray(ybar)
for i in range(len(index)):
    ax.scatter(index[i] + np.random.random(ybar[i].size) * (w*0.2) - (w*0.2) / 2, ybar[i], s = 20, color=colorsbar[i])
plt.ylabel('Diameter (nm)', fontname='Helvetica', fontsize=20)
plt.yticks(fontsize=20, fontname='Helvetica')
plt.xticks(fontsize=20, fontname='Helvetica', rotation=45)
# plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.savefig('Diameter-plot-2.svg')
plt.savefig('Diameter-plot-2.png')
plt.show()

