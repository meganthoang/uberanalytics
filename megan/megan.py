# Megan's Code -- last updated 9/11/2021

'''
Notes:  
    git commit -am "comment"  --- is a shortcut so you can skip the add step
    ctrl + KT is to change themes in vscode
    ctrl + D is to select future instances of text selected
    # #%% matplotlib inline -- for Jupyter Notebook
'''

# # %% matplotlib inline
# first, let's import all necessary modules & assign aliases
import pandas as pd
import numpy as np

# visualization modules
from matplotlib import pyplot as plt # import matplotlib.pyplot as plt
import seaborn as sns

# matplotlib basemap toolkit is a library for plotting 2D data on maps in Python
# from mpl_toolkits.basemap import Basemap # so apparently this shit's been deprecated
from matplotlib import cm #Colormap

#Animation Modules
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

# directory modules
import glob
import os


# Preprocessing
# Find out what the current directory is
print(os.getcwd())
# prints "C:\Users\megan\OneDrive\Desktop\Analytics\uberanalytics\megan"

# change the directory to match the location of the data
os.chdir("c:/Users/megan/OneDrive/Desktop/Analytics/uber_data")
print(os.getcwd()) # print to verify
# should be set to "C:\Users\megan\OneDrive\Desktop\Analytics\uber_data"

# print names of files in the directory
# for dirname, _, filenames in os.walk(".", topdown = False):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))

path = "c:/Users/megan/OneDrive/Desktop/Analytics/uber_data"

# Load the datasets
df_apr14 = pd.read_csv(os.path.join(path, "uber-raw-data-apr14.csv"))
df_may14 = pd.read_csv(os.path.join(path, "uber-raw-data-may14.csv"))
df_jun14 = pd.read_csv(os.path.join(path, "uber-raw-data-jun14.csv"))
df_jul14 = pd.read_csv(os.path.join(path, "uber-raw-data-jul14.csv"))
df_aug14 = pd.read_csv(os.path.join(path, "uber-raw-data-aug14.csv"))
df_sep14 = pd.read_csv(os.path.join(path, "uber-raw-data-sep14.csv"))

# append all the datasets together
df = df_apr14.append([df_may14,df_jun14,df_jul14,df_aug14,df_sep14], ignore_index=True)

# print a summary to see how the data looks
# df.head() # returns the first 5 rows of the dataframe
# df.info() # prints a summary of df

# format Date/Time data
# df = df.rename(columns={'Date/Time': 'Date_time'})
df['Date/Time'] = pd.to_datetime(df['Date/Time'])
df['Month'] = df['Date/Time'].dt.month_name()
df['Weekday'] = df['Date/Time'].dt.day_name()
df['Day'] = df['Date/Time'].dt.day
df['Hour'] = df['Date/Time'].dt.hour
df['Minute'] = df['Date/Time'].dt.minute

print("\nHead:___________________________________________")
print(df.head())
print("\nInfo:___________________________________________") 
print(df.info())
print("\nDescribe:_______________________________________")
print(df.describe(include = 'all', datetime_is_numeric=True))
print("\nShape:__________________________________________")
print(df.shape) 
rows = df.shape[0]
cols = df.shape[1]
# df.shape prints the shape of the df in the form (rows, columns)

# Show the memory usage in megabytes of every column
print("\nMemory Usage:___________________________________")
print(df.memory_usage(deep=True) * 1e-6)
print("\nTotal: ", df.memory_usage(deep=True).sum() * 1e-6)

# Cross-Analysis

# function that counts the rows
def count_rows(rows):
    return len(rows)

# now, instantiate a new dataframe that stores the data by hour and day
'''
.groupby() - a groupby operation involves some combination of splitting the object, 
    applying a function, and combining the results. This can be used to group large 
    amounts of data and compute operations on these groups.
.split() - splits a string into a list where each word is a list item
.apply() - takes in a function to be applied 
.unstack() - Returns a DataFrame having a new level of column labels whose inner-most 
    level consists of the pivoted index labels.
'''
df_hd = df.groupby('Hour Day'.split()).apply(count_rows).unstack()
print("\nHead:___________________________________________")
print(df_hd.head())
plt.figure(figsize = (12,8))

#Using the seaborn heatmap function 
ax = sns.heatmap(df_hd, cmap=cm.YlGnBu, linewidth = .5)
ax.set(title="Trips by Hour and Day");
print(ax)

