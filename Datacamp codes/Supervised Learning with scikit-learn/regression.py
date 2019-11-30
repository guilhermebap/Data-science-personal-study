import pandas as pd
import matplotlib as plt
import numpy as np
from sklearn import datasets

'''
Importing data for supervised learning

Since the target variable here is quantitative, this is a regression problem.
To begin, you will fit a linear regression with just one feature: 'fertility'
'''
df = pd.read_csv('../gapminder.csv')
