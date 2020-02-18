'''
In this chapter, you'll use the Keras library to build deep learning models for
both regression and classification. You'll learn about the Specify-Compile-Fit
workflow that you can use to make predictions, and by the end of the chapter,
you'll have all the tools necessary to build deep neural networks.
'''

'''
Specifying a model
'''
# Import necessary modules
import keras
from keras.layers import Dense
from keras.models import Sequential

# Save the number of columns in predictors: n_cols
n_cols = predictors.shape[1]

# Set up the model: model
model = Sequential()

# Add the first layer
model.add(Dense(50, activation='relu', input_shape=(n_cols,)))

# Add the second layer
model.add(Dense(32, activation='relu'))

# Add the output layer
model.add(Dense(1))
