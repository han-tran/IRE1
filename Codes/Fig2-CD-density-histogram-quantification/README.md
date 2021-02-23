#Usage of "Cluster-analysis.py"
- Code used to extract and plot immunogold particle density histograms 

##Data input:
- Immunogold micrographs of HEK293T cells expressing IRE1 tagged with GFP and processed  for immunogold detection of GPF epitope. Cells were either non-treated or treated with Tunicamycin to induce stress. 
- Raw data were scans of developed films provided by Klumpermann lab
- For each image, place an ROI on each gold particle and "measure" to extract XY coordinate for each particle. 
- Export list of coordinate for all particles from one image as an .txt file. 

##Code usage:
- Make a new folder with copy of analysis code and place all .txt file from which a plot should be generated. 
- Modify file path of "MainDirectoryLoad" to current folder
- Name Axis label
- Set appropriate "num_bins" for dataset. (close to square root of N) 
- Name output files
- Save and run. 	
