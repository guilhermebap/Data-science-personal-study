'''
Classification and Regression Trees (CART) are a set of supervised learning
models used for problems involving classification and regression. In this chapter,
you'll be introduced to the CART algorithm.
'''

'''
Train your first classification tree

In this exercise you'll work with the Wisconsin Breast Cancer Dataset from the
UCI machine learning repository. You'll predict whether a tumor is malignant or
benign based on two features: the mean radius of the tumor (radius_mean) and its
mean number of concave points (concave points_mean).

'''
# Import DecisionTreeClassifier from sklearn.tree
from sklearn.tree import DecisionTreeClassifier

# Instantiate a DecisionTreeClassifier 'dt' with a maximum depth of 6
dt = DecisionTreeClassifier(max_depth=6, random_state=SEED)

# Fit dt to the training set
dt.fit(X_train, y_train)

# Predict test set labels
y_pred = dt.predict(X_test)
print(y_pred[0:5])



'''
Evaluate the classification tree
'''
# Import accuracy_score
from sklearn.metrics import accuracy_score

# Predict test set labels
y_pred = dt.predict(X_test)

# Compute test set accuracy
acc = accuracy_score(y_test, y_pred)
print("Test set accuracy: {:.2f}".format(acc))



'''
Logistic regression vs classification tree

A classification tree divides the feature space into rectangular regions. In
contrast, a linear model such as logistic regression produces only a single
linear decision boundary dividing the feature space into two decision regions.
'''
# Import LogisticRegression from sklearn.linear_model
from sklearn.linear_model import LogisticRegression

# Instatiate logreg
logreg = LogisticRegression(random_state=1)

# Fit logreg to the training set
logreg.fit(X_train, y_train)

# Define a list called clfs containing the two classifiers logreg and dt
clfs = [logreg, dt]

# Review the decision regions of the two classifiers
plot_labeled_decision_regions(X_test, y_test, clfs)



'''
Using entropy as a criterion
'''
# Import DecisionTreeClassifier from sklearn.tree
from sklearn.tree import DecisionTreeClassifier

# Instantiate dt_entropy, set 'entropy' as the information criterion
dt_entropy = DecisionTreeClassifier(max_depth=8, criterion='entropy', random_state=1)

# Fit dt_entropy to the training set
dt_entropy.fit(X_train, y_train)



'''
Entropy vs Gini index
'''
# Import accuracy_score from sklearn.metrics
from sklearn.metrics import accuracy_score

# Use dt_entropy to predict test set labels
y_pred = dt_entropy.predict(X_test)

# Evaluate accuracy_entropy
accuracy_entropy = accuracy_score(y_test, y_pred)

# Print accuracy_entropy
print('Accuracy achieved by using entropy: ', accuracy_entropy)

# Print accuracy_gini
print('Accuracy achieved by using the gini index: ', accuracy_gini)



'''
Train your first regression tree

In this exercise, you'll train a regression tree to predict the mpg (miles per
gallon) consumption of cars in the auto-mpg dataset using all the six available
features.
'''
# Import DecisionTreeRegressor from sklearn.tree
from sklearn.tree import DecisionTreeRegressor

# Instantiate dt
dt = DecisionTreeRegressor(max_depth=8,
             min_samples_leaf=0.13,
            random_state=3)

# Fit dt to the training set
dt.fit(X_train, y_train)



'''
Evaluate the regression tree

In this exercise, you will evaluate the test set performance of dt using the
Root Mean Squared Error (RMSE) metric. The RMSE of a model measures, on average,
how much the model's predictions differ from the actual labels. The RMSE of a
model can be obtained by computing the square root of the model's Mean Squared
Error (MSE).
'''
# Import mean_squared_error from sklearn.metrics as MSE
from sklearn.metrics import mean_squared_error as MSE

# Compute y_pred
y_pred = dt.predict(X_test)

# Compute mse_dt
mse_dt = MSE(y_test, y_pred)

# Compute rmse_dt
rmse_dt = mse_dt**(1/2)

# Print rmse_dt
print("Test set RMSE of dt: {:.2f}".format(rmse_dt))



'''
Linear regression vs regression tree

you'll compare the test set RMSE of dt to that achieved by a linear regression model.
'''
# Predict test set labels
y_pred_lr = lr.predict(X_test)

# Compute mse_lr
mse_lr = MSE(y_test, y_pred_lr)

# Compute rmse_lr
rmse_lr = mse_lr**(1/2)

# Print rmse_lr
print('Linear Regression test set RMSE: {:.2f}'.format(rmse_lr))

# Print rmse_dt
print('Regression Tree test set RMSE: {:.2f}'.format(rmse_dt))

'Linear Regression test set RMSE: 5.10'
'Regression Tree test set RMSE: 4.37'
