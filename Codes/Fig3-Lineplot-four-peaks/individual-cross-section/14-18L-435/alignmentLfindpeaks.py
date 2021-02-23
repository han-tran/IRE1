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

#Area in nm where you want to align. For rings, 20-26 works well to align min value.
alingmentbeginleft = 5
alingmentendleft = 10
alingmentbeginright = 33
alingmentendright = 38

#Set MinOrMax to one if you are looking for the maximum before inversion, if you are looking for the minimum set to 0
MinOrMax = 0

MainDirectoryLoad = "/Users/HanTran/14-18L-435"

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
			AllLines.append(temptemp)

AllIntensityLines = []
for i in range(len(AllLines)):
	if i % 2 == 1:
		AllIntensityLines.append(AllLines[i])		
xvalues = AllLines[0]

for i in range(len(xvalues)):
	if xvalues[i] >= alingmentbeginleft:
		startleft = i
		break
for i in range(len(xvalues)):
	if xvalues[i] >= alingmentendleft:
		endleft = i
		break

for i in range(len(xvalues)):
	if xvalues[i] >= alingmentbeginright:
		startright = i
		break
for i in range(len(xvalues)):
	if xvalues[i] >= alingmentendright:
		endright = i
		break		
		
maxpositionforeachleft = []
for i in range(len(AllIntensityLines)):
	temp = []
	for j in range(endleft-startleft):
		currentpos = j + startleft
		temp.append(AllIntensityLines[i][currentpos])
	if MinOrMax == 1:
		maxvalue = max(temp)
	if MinOrMax == 0:
		maxvalue = min(temp)	
	temptemp = []
	for j in range(endleft-startleft):
		currentpos = j + startleft
		if AllIntensityLines[i][currentpos] == maxvalue:
			temptemp.append(currentpos)
	maxpositionforeachleft.append(temptemp[0])

maxpositionforeachright = []
for i in range(len(AllIntensityLines)):
	temp = []
	for j in range(endright-startright):
		currentpos = j + startright
		temp.append(AllIntensityLines[i][currentpos])
	if MinOrMax == 1:
		maxvalue = max(temp)
	if MinOrMax == 0:
		maxvalue = min(temp)	
	temptemp = []
	for j in range(endright-startright):
		currentpos = j + startright
		if AllIntensityLines[i][currentpos] == maxvalue:
			temptemp.append(currentpos)
	maxpositionforeachright.append(temptemp[0])

middelbetweenpeaks = int(round((np.mean(maxpositionforeachleft) + np.mean(maxpositionforeachright)) / 2.0))

print(maxpositionforeachleft)
print(maxpositionforeachright)

maxpositionforeachbetweentwopeaks = []
for i in range(len(maxpositionforeachleft)):
	maxpositionforeachbetweentwopeaks.append(int(round((maxpositionforeachleft[i] + maxpositionforeachright[i]) / 2.0)))

AlignedIntensityLines = []
for i in range(len(maxpositionforeachleft)):
	temp = AllIntensityLines[i]
	if maxpositionforeachbetweentwopeaks[i] > middelbetweenpeaks:
		for j in range(maxpositionforeachbetweentwopeaks[i] - middelbetweenpeaks):
			temp.insert(len(temp), np.nan)
			del temp[0]
	if maxpositionforeachbetweentwopeaks[i] < middelbetweenpeaks:
		for j in range(middelbetweenpeaks - maxpositionforeachbetweentwopeaks[i]):
			temp.insert(0, np.nan)
			del temp[-1]	
	AlignedIntensityLines.append(temp)

AvgAlignedIntensityLines = []
StdAlignedIntensityLines = []

for i in range(len(AlignedIntensityLines[0])):
	temp = []
	for j in range(len(AlignedIntensityLines)):
		temp.append(AlignedIntensityLines[j][i] * (-1) + 250)
	AvgAlignedIntensityLines.append(np.nanmean(temp))
	StdAlignedIntensityLines.append(np.nanstd(temp))

AlignedIntensityLinesInverted = []
for i in range(len(AlignedIntensityLines)):
	temp = []
	for j in range(len(AlignedIntensityLines[i])):
		temp.append(AlignedIntensityLines[i][j] * (-1) + 250)
	AlignedIntensityLinesInverted.append(temp)
	
for i in range(len(AlignedIntensityLinesInverted)):
	plt.plot(xvalues, AlignedIntensityLinesInverted[i], linestyle='-', lw=1.0, color = 'orange', alpha = 0.2) 

#Next two line is optional: for printing x-y value. Remove if not final
for i in range(len(AvgAlignedIntensityLines)):
	print(xvalues[i], AvgAlignedIntensityLines[i])
	
plt.plot(xvalues, AvgAlignedIntensityLines, linestyle='-', lw=2.0, color = 'blue') 
c2timearray = np.asarray(xvalues)
c2precissionarray = np.asarray(StdAlignedIntensityLines)
c2xfitarray = np.asarray(AvgAlignedIntensityLines)
plt.fill_between(c2timearray, c2xfitarray-c2precissionarray, c2xfitarray+c2precissionarray, alpha=0.2, edgecolor='blue', facecolor='blue')

plt.xlabel('Distance (nm)', fontsize=20, fontname='Helvetica')
plt.ylabel('Intensity (a.u.)', fontsize=20, fontname='Helvetica')
plt.yticks(fontsize=20, fontname='Helvetica')	
plt.xticks(fontsize=20, fontname='Helvetica')
plt.xlim([0,45])
plt.savefig("LinePlot-ring_two-peaks-5-10-33-38.svg")
plt.savefig("LinePlot-ring_two-peaks-5-10-33-38.png")
plt.show()
	
	
		
	

