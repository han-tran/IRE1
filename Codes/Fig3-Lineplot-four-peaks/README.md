#Usage of "alignmentLfindpeaks.py"
- Code used to find peaks intensity line plots, align plots and average intensity plots.
- Used in Fig 3C to reveal the 4 intensity peaks corresponding to two membrane and two protein densities. 

##Data input:
### Line plots for individual cross-sections:
1. Using Fiji or imageJ: For each cross section, either longitudinal or end-on, draw lines perpendicular to membrane densities, taking care to have lines of same length and with the center of the line roughly intersecting the center of the membrane tube. (See Fig. S9 for examples of how lines were drawn). 
2. Extract the line plots as .csv and .txt files

### Line plots for average-of-average
- Copy the .txt outputs for each individual line plot generated above into a new input folder. They are the input files.
- Copy alignmentLfindpeaks.py file into folder

## Code usage: 
1. Create a folder for each section with a copy of the .py file and .txt file
2. Change directory accordingly
3. CHange "MinOrMax" value to either 0 or 1. Set MinOrMax to one if you are looking for the maximum before inversion, if you are looking for the minimum set to 0
4.  Change "alingmentbegin" and "alingmentend" values to emcompass alignment region (where expect peak or trough; in distance unit from start of plot). This will take some optimization depending on the particular plots. For the dataset shown, some plots were aligned using the center trough where others wre aligned by first finding where the most pronounced membrane peaks (outer) are and then aligned by the center of this. 
5. Set output files names and whether printing .txt output. .txt file is used as input files for next iteration: "average-of-average" and for determining distances between peaks. 
6. Name Axis labels etc 
7. Save and run py command. 


