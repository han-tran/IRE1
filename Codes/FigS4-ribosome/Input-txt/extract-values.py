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


MainDirectoryLoad = "/Users/HanTran/Py-extract-values"
#Use this to extract .txt values from measurement output .txt files, which contain raw readings from 3dmod

Lines= []
for file in os.listdir(MainDirectoryLoad):
    if file.endswith(".txt"):
        Lines.append(file)
              
Lines = sorted(Lines)

for i in range(len(Lines)):
	with open(MainDirectoryLoad + "/" + Lines[i]) as f:
		reader = csv.reader(f, delimiter=",")
		Start = list(reader)

del Start[0]
del Start[0]
del Start[0]
	
AllValues = []		
for i in range(int(len(Start)/2)):
	value = Start[(i*2)+1][1].split(" ")	
	AllValues.append(float(value[1]))

print(AllValues)	
print("Average: " + str(np.mean(AllValues)) + " nm")
print("Standard deviation: " + str(np.std(AllValues)) + " nm")
	

