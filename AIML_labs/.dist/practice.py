
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

# Reading the csv file 
df = pd.read_csv(r"C:\Users\sayed\Desktop\Practice_Dataset\Lab-1\business_sales_data.csv")
print(df.head())


# summary of all numeric columns
df.describe()