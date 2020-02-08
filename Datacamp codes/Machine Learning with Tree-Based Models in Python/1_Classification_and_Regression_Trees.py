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