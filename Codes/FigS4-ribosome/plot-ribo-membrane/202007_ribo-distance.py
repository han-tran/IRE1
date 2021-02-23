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

# colors = ['#00FFAA', '#45C3B8', '#42C0FB', '#1C86EE', '#6666FF', '#5E2D79', '#FF00FF', '#CC3299', '#DC143C', '#99182C', '#FF5721', '#ff8C00']
colors = ['#ff8C00', '#fff266', '#ff8C00', '#fff266', '#b36200', '#ffec1a' ]

################################################################################
################################################################################
###                      DONT MAKE CHANGES BELOW HERE                        ###
################################################################################
################################################################################


################################################################################
###                             SECTION 1: DATA                              ###
################################################################################


MainDirectoryLoad = "/Users/HanTran/plot-ribo-membrane"
#Use this to plot the ribosome to membrane distances measured. Input file is .txt file where each line is a measurement group and each measurement within group is tab-deliminated. 
#Note that cannot contain text labels. Measurement group label were removed from .txt file. They are as followed from top to bottom: 14-18-ER, 14-18-IRE1, 20-4-ER, 20-4-IRE1
Lines= []
for file in os.listdir(MainDirectoryLoad):
    if file.endswith(".txt"):
        Lines.append(file)
        
        
Lines = sorted(Lines)

AllLines = []
for i in range(len(Lines)):
	with open(MainDirectoryLoad + "/" + Lines[i]) as f:
		reader = csv.reader(f, delimiter=",")
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
colorsbar = [colors[0], colors[1], colors[2], colors[3]]
coloredge = [colors[4], colors[5], colors[4], colors[5]]
plt.rc('font', size=20)
np.random.seed(123)
index = np.arange(4)
w = 0.5
fig, ax = plt.subplots()
ax.bar(index,
       height=[np.mean(yi) for yi in ybar],
       yerr=[np.std(yi) for yi in ybar],    # error bars
       lw=2, capsize=15, # error bar cap width in points
       width=w,    # bar width
       tick_label=["MEFs ER membrane", "MEFs IRE1 subdomain", "U2OS ER membrane", "U2OS IRE1 subdomain"],
       color=colorsbar,
       alpha=0.6,
       edgecolor=coloredge,    
       )      
ybar = np.asarray(ybar)
for i in range(len(index)):
    ax.scatter(index[i] + np.random.random(ybar[i].size) * (w*0.2) - (w*0.2) / 2, ybar[i], s = 20, color=colorsbar[i])
plt.ylabel('Distance (nm)', fontname='Helvetica', fontsize=20)
plt.yticks(fontsize=20, fontname='Helvetica')
plt.xticks(fontsize=20, fontname='Helvetica', rotation=45)
# plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.savefig('ribo-membrane-distance.svg')
plt.savefig('ribo-membrane-distance.png')
plt.show()

