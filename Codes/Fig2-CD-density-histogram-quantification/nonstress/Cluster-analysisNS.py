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


MainDirectoryLoad = "/Users/HanTran/nonstress"
#Change "MainDirectoryLoad" to folder containing .py file and .txt file with measurements. The only .txt file in this folder should be that being plotted. Other files should be removed or stored in a subfolder. 

Clusters= []
for file in os.listdir(MainDirectoryLoad):
    if file.endswith(".txt"):
        Clusters.append(file)
        
        
Clusters = sorted(Clusters)

AllClustersX = []
AllClustersY = []
for i in range(len(Clusters)):
	tempX = []
	tempY = []
	with open(MainDirectoryLoad + "/" + Clusters[i]) as f:
		reader = csv.reader(f, delimiter="\t")
		Start = list(reader)
		del Start[0]
		for c in range(len(Start)): 
			Start[c] = list(map(float, Start[c]))
			tempX.append(Start[c][5]*0.001)
			tempY.append(Start[c][6]*0.001)
	AllClustersX.append(tempX)
	AllClustersY.append(tempY)
	

distances = []
for i in range(len(AllClustersX)):
	for j in range(len(AllClustersX[i])):
		for k in range(len(AllClustersX[i])-j):
			l = j+k
			if j != l:
				distances.append(math.sqrt((AllClustersX[i][j]-AllClustersX[i][l])**2 + (AllClustersY[i][j]-AllClustersY[i][l])**2))


num_bins = np.linspace(0, max(distances), 20)
n, bins, patches = plt.hist(distances, num_bins, facecolor="#80bfff", alpha=1, edgecolor='white', linewidth = 1, label=" N = %.0f, d = %.3f $\pm$ %.3f nm" %(len(distances), np.mean(distances), np.std(distances)))
plt.xlabel('Distance (μm)', fontsize=20, fontname='Helvetica')
plt.ylabel('Count', fontsize=20, fontname='Helvetica')
plt.xticks(fontsize=20, fontname='Helvetica')
plt.xlim(0, 2.6)
plt.yticks(fontsize=20, fontname='Helvetica')
plt.savefig(MainDirectoryLoad + "/replot-NS2-bin20.svg")
plt.legend(fontsize=18, frameon=False, loc='best')
plt.savefig(MainDirectoryLoad + "/replot-NS2-bin20.png")
plt.show()