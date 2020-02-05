'''
In this chapter, you'll learn about a dimension reduction technique called
"Non-negative matrix factorization" ("NMF") that expresses samples as combinations
of interpretable parts. For example, it expresses documents as combinations of
topics, and images in terms of commonly occurring visual patterns. You'll also
learn to use NMF to build recommender systems that can find you similar articles
to read, or musical artists that match your listening history!
'''

'''
NMF applied to Wikipedia articles
'''
# Import NMF
from sklearn.decomposition import NMF

# Create an NMF instance: model
model = NMF(n_components=6)

# Fit the model to articles
model.fit(articles)

# Transform the articles: nmf_features
nmf_features = model.transform(articles)

# Print the NMF features
print(nmf_features)



'''
NMF features of the Wikipedia articles
'''
# Import pandas
import pandas as pd

# Create a pandas DataFrame: df
df =  pd.DataFrame(nmf_features, index=titles)

# Print the row for 'Anne Hathaway'
print(df.loc['Anne Hathaway'])

# Print the row for 'Denzel Washington'
print(df.loc['Denzel Washington'])



'''
NMF learns topics of documents
'''
 # Import pandas
import pandas as pd

# Create a DataFrame: components_df
components_df = pd.DataFrame(model.components_, columns=words)

# Print the shape of the DataFrame
print(components_df.shape)

# Select row 3: component
component = components_df.iloc[3]

# Print result of nlargest
print(component.nlargest())




'''
Explore the LED digits dataset
'''
