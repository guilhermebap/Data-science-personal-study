import pandas as pd
import matplotlib.pyplot as plt


'''
Correlated data in nature

You are given an array grains giving the width and length of samples of grain.
You suspect that width and length will be correlated. To confirm this, make
scatter plot of width vs length and measure their Pearson correlation.

pearsonr - Calculates a Pearson correlation coefficient and the p-value for testing non-correlation.
'''
from scipy.stats import pearsonr

# Assign the 0th column of grains: width
width = grains[:, 0]

# Assign the 1st column of grains: length
length = grains[:, 1]

# Scatter plot width vs length
plt.scatter(width, length)
plt.axis('equal')
plt.show()

# Calculate the Pearson correlation
correlation, pvalue = pearsonr(width, length)

# Display the correlation
print(correlation)



'''
Decorrelating the grain measurements with PCA
'''
# Import PCA
from sklearn.decomposition import PCA

# Create PCA instance: model
model = PCA()

# Apply the fit_transform method of model to grains: pca_features
pca_features = model.fit_transform(grains)

# Assign 0th column of pca_features: xs
xs = pca_features[:,0]

# Assign 1st column of pca_features: ys
ys = pca_features[:,1]

# Scatter plot xs vs ys
plt.scatter(xs, ys)
plt.axis('equal')
plt.show()

# Calculate the Pearson correlation of xs and ys
correlation, pvalue = pearsonr(xs, ys)

# Display the correlation
print(correlation)



'''
Principal components
'''
