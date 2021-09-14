# Import necessary modules

# # %% matplotlib inline
# Import all necessary modules & assign aliases
import pandas as pd
import numpy as np

# Visualization modules
from matplotlib import pyplot as plt # import matplotlib.pyplot as plt
import seaborn as sns

# Matplotlib basemap toolkit is a library for plotting 2D data on maps in Python
# from mpl_toolkits.basemap import Basemap # so apparently this shit's been deprecated
from matplotlib import cm #Colormap


# Animation Modules
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

# Directory modules
import glob
import os


# Preprocessing
# Find out what the current directory is
print(os.getcwd())
# prints "C:\Users\megan\OneDrive\Desktop\Analytics\uberanalytics\megan"

# Change the directory to match the location of the data
#os.chdir("c:/Users/megan/OneDrive/Desktop/Analytics/uber_data")
#print(os.getcwd()) # print to verify
# should be set to "C:\Users\megan\OneDrive\Desktop\Analytics\uber_data"
