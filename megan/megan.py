# Megan's Code

# git commit -am "comment"  --- is a shortcut so you can skip the add step
# Import necessary modules
import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
import glob
import os

# # %% matplotlib inline -- for Jupyter Notebook

# Find out the current directory.
os.getcwd()
# print (os.getcwd()) -- prints "C:\Users\megan\OneDrive\Desktop\Analytics\uberanalytics\megan"
os.chdir()
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
# still need to change this directory to match the data folder


