import pandas as pd
import matplotlib as plt
import numpy as np
from sklearn import datasets

df = pd.read_csv('../datasets/house-votes-84')
plt.style.use('ggplot')

'''
EDA
'''
df.head()
df.shape
df.info()
df.describe()

plt.figure()
sns.countplot(x='education', hue='party', data=df, palette='RdBu')
plt.xticks([0,1], ['No', 'Yes'])
plt.show()

plt.figure()
sns.countplot(x='satellite', hue='party', data=df, palette='RdBu')
plt.xticks([0,1], ['No', 'Yes'])
plt.show()

plt.figure()
sns.countplot(x='missile', hue='party', data=df, palette='RdBu')
plt.xticks([0,1], ['No', 'Yes'])
plt.show()
