import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import sklearn
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

boston = load_boston()
print(boston.target)
bos = pd.DataFrame(boston.data)
bos.columns = boston.feature_names
bos['PRICE'] = boston.target

X = bos.drop('PRICE', axis=1)
lm = LinearRegression()
lm.fit(X, bos.PRICE)
coef = pd.DataFrame(zip(X.columns, lm.coef_), columns=['features', 'estimatedCoefficients'])
print(coef)

'''
plt.scatter(bos.RM, bos.PRICE)
plt.xlabel('Average number of rooms per dwelling (RM)')
plt.ylabel('Housing Price')
plt.title('Relationship between RM and Price')
plt.show()
'''

