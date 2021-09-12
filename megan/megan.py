# Megan's Code -- last updated 9/11/2021

'''
Notes:  
    git commit -am "comment"  --- is a shortcut so you can skip the add step
    ctrl + KT is to change themes in vscode
    ctrl + D is to select future instances of text selected
    # #%% matplotlib inline -- for Jupyter Notebook
'''

# first, let's import all necessary modules & assign aliases
import pandas as pd
import numpy as np

# visualization modules
from matplotlib import pyplot as plt # import matplotlib.pyplot as plt
import seaborn as sns

# matplotlib basemap toolkit is a library for plotting 2D data on maps in Python
from mpl_toolkits.basemap import Basemap
from matplotlib import cm #Colormap

#Animation Modules
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

# directory modules
import glob
import os


# Find out what the current directory is
print(os.getcwd())
# prints "C:\Users\megan\OneDrive\Desktop\Analytics\uberanalytics\megan"

# change the directory to match the location of the data
os.chdir(r"C:\Users\megan\OneDrive\Desktop\Analytics\uber_data")
print(os.getcwd()) # print to verify
# should be set to "C:\Users\megan\OneDrive\Desktop\Analytics\uber_data"

# print names of files in the directory
# for dirname, _, filenames in os.walk(".", topdown = False):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))


