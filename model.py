import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df_data=pd.read_csv('/Users/deepakjangid/Desktop/python projrcts/Flask/recession prediction/Data/India_GDP_Data.csv')
print(df_data.head())
