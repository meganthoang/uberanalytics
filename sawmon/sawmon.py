# Import necessary modules

import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
import glob
import os

%matplotlib inline
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
