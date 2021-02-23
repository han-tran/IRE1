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
import re

#Area in nm where you want to align. For rings, 20-26 works well to align min value.
alingmentbeginleft = 5
alingmentendleft = 10
alingmentbeginright = 33
alingmentendright = 38

#Set MinOrMax to 1 if you are looking for the maximum before inversion, if you are looking for the minimum set to 0
MinOrMax = 1

MainDirectoryLoad = "/Users/HanTran/average-of-average"
#Change "MainDirectoryLoad" to folder containing .py file and .txt file with measurements. The only .txt file in this folder should be that being plottet. Other files should be removed or stored in a subfolder. 

Lines= []
for file in os.listdir(MainDirectoryLoad):
    if file.endswith(".txt"):
        Lines.append(file)
        
        
Lines = sorted(Lines)


AllLines = []
for i in range(len(Lines)):
	with open(MainDirectoryLoad + "/" + Lines[i]) as f:
		reader = csv.reader(f)
		Start = list(reader)
		temp = []
		for c in range(len(Start)): 
			temptemp = []
			for d in range(len(Start[c])): 
				value = re.split(' +', Start[c][d])
				temptemp.append(float(value[0]))
				temptemp.append(float(value[1]))
			temp.append(temptemp)
		AllLines.append(temp)

AllIntensityLines = []
Allxvalues = []
for i in range(len(AllLines)):
	temx = []
	temint = []
	for j in range(len(AllLines[i])):
		temint.append(AllLines[i][j][1])		
		temx.append(AllLines[i][j][0])
	AllIntensityLines.append(temint)
	Allxvalues.append(temx)


startleft = []
endleft = []
startright = []
endright = []
for j in range(len(AllLines)):
	for i in range(len(Allxvalues[j])):
		if Allxvalues[j][i] >= alingmentbeginleft:
			startleft.append(i)
			break
	for i in range(len(Allxvalues[j])):
		if Allxvalues[j][i] >= alingmentendleft:
			endleft.append(i)
			break
	for i in range(len(Allxvalues[j])):
		if Allxvalues[j][i] >= alingmentbeginright:
			startright.append(i)
			break
	for i in range(len(Allxvalues[j])):
		if Allxvalues[j][i] >= alingmentendright:
			endright.append(i)
			break		
		
maxpositionforeachleft = []
for i in range(len(AllIntensityLines)):
	temp = []
	for j in range(endleft[i]-startleft[i]):
		currentpos = j + startleft[i]
		temp.append(AllIntensityLines[i][currentpos])
	if MinOrMax == 1:
		maxvalue = max(temp)
	if MinOrMax == 0:
		maxvalue = min(temp)	
	temptemp = []
	for j in range(endleft[i]-startleft[i]):
		currentpos = j + startleft[i]
		if AllIntensityLines[i][currentpos] == maxvalue:
			temptemp.append(Allxvalues[i][currentpos])
	maxpositionforeachleft.append(temptemp[0])

maxpositionforeachright = []
for i in range(len(AllIntensityLines)):
	temp = []
	for j in range(endright[i]-startright[i]):
		currentpos = j + startright[i]
		temp.append(AllIntensityLines[i][currentpos])
	if MinOrMax == 1:
		maxvalue = max(temp)
	if MinOrMax == 0:
		maxvalue = min(temp)	
	temptemp = []
	for j in range(endright[i]-startright[i]):
		currentpos = j + startright[i]
		if AllIntensityLines[i][currentpos] == maxvalue:
			temptemp.append(Allxvalues[i][currentpos])
	maxpositionforeachright.append(temptemp[0])

middelbetweenpeaks = int(round((np.mean(maxpositionforeachleft) + np.mean(maxpositionforeachright)) / 2.0))

maxpositionforeachbetweentwopeaks = []
for i in range(len(maxpositionforeachleft)):
	maxpositionforeachbetweentwopeaks.append(int(round((maxpositionforeachleft[i] + maxpositionforeachright[i]) / 2.0)))

AlignedIntensityLines = []
for i in range(len(maxpositionforeachleft)):
	temp = AllIntensityLines[i]
	if maxpositionforeachbetweentwopeaks[i] > middelbetweenpeaks:
		for j in range(round((maxpositionforeachbetweentwopeaks[i] - middelbetweenpeaks) / Allxvalues[i][1])):
			temp.insert(len(temp), np.nan)
			del temp[0]
	if maxpositionforeachbetweentwopeaks[i] < middelbetweenpeaks:
		for j in range(round(middelbetweenpeaks - maxpositionforeachbetweentwopeaks[i] / Allxvalues[i][1])):
			temp.insert(0, np.nan)
			del temp[-1]	
	AlignedIntensityLines.append(temp)

AvgAlignedIntensityLines = []
StdAlignedIntensityLines = []
xvaluesforaverage = np.arange(0, 45.5, 0.5)

for k in range(len(xvaluesforaverage)- 1):
	temp = []
	for i in range(len(AllIntensityLines)):
		for j in range(len(Allxvalues[i])):
			if xvaluesforaverage[k] <= Allxvalues[i][j] < xvaluesforaverage[k+1]:
				temp.append(AlignedIntensityLines[i][j])
	AvgAlignedIntensityLines.append(np.nanmean(temp))
	StdAlignedIntensityLines.append(np.nanstd(temp))
AvgAlignedIntensityLines.append(np.nanmean(temp))
StdAlignedIntensityLines.append(np.nanstd(temp))

AlignedIntensityLinesInverted = []
for i in range(len(AlignedIntensityLines)):
	temp = []
	for j in range(len(AlignedIntensityLines[i])):
		temp.append(AlignedIntensityLines[i][j] * (-1) + 250)
	AlignedIntensityLinesInverted.append(temp)


#Next two line is optional: for printing x-y value. Remove if not final
for i in range(len(AvgAlignedIntensityLines)):
	print(xvaluesforaverage[i], AvgAlignedIntensityLines[i])

for i in range(len(AllIntensityLines)):
	plt.plot(Allxvalues[i], AllIntensityLines[i], linestyle='-', lw=1.0, color = 'orange') 
plt.plot(xvaluesforaverage, AvgAlignedIntensityLines, linestyle='-', lw=2.0, color = 'blue') 
c2timearray = np.asarray(xvaluesforaverage)
c2precissionarray = np.asarray(StdAlignedIntensityLines)
c2xfitarray = np.asarray(AvgAlignedIntensityLines)
plt.fill_between(c2timearray, c2xfitarray-c2precissionarray, c2xfitarray+c2precissionarray, alpha=0.2, edgecolor='blue', facecolor='blue')

plt.xlabel('Distance (nm)', fontsize=20, fontname='Helvetica')
plt.ylabel('Intensity (a.u.)', fontsize=20, fontname='Helvetica')
plt.yticks(fontsize=20, fontname='Helvetica')	
plt.xticks(fontsize=20, fontname='Helvetica')
plt.xlim([0,45])
plt.savefig("MEFs-lineplot-all-2peaks-3-5-10-33-38.svg")
plt.savefig("MEFs-lineplot-all-2peaks-3-5-10-33-38.png")
plt.show()
	
	
#Change output format and names accordingly. 		
	

