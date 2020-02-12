'''
Bagging is an ensemble method involving training the same algorithm many times
using different subsets sampled from the training data. In this chapter, you'll
understand how bagging can be used to create a tree ensemble. You'll also learn
how the random forests algorithm can lead to further ensemble diversity through
randomization at the level of each split in the trees forming the ensemble.
'''


'''
Define the bagging classifier
'''
# Import DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier

# Import BaggingClassifier
from sklearn.ensemble import BaggingClassifier

# Instantiate dt
dt = DecisionTreeClassifier(random_state=1)

# Instantiate bc
bc = BaggingClassifier(base_estimator=dt, n_estimators=50, random_state=1)



'''
Evaluate Bagging performance
'''
# Fit bc to the training set
bc.fit(X_train, y_train)

# Predict test set labels
y_pred = bc.predict(X_test)

# Evaluate acc_test
acc_test = accuracy_score(y_test, y_pred)
print('Test set accuracy of bc: {:.2f}'.format(acc_test))

'Test set accuracy of bc: 0.71'
'A single tree dt would have achieved an accuracy of 63% which is 8% lower than bc'



'''
Prepare the ground

Compare the OOB accuracy to the test set accuracy of a bagging classifier
trained on the Indian Liver Patient dataset.

In sklearn, you can evaluate the OOB accuracy of an ensemble classifier by setting
the parameter oob_score to True during instantiation. After training the classifier,
the OOB accuracy can be obtained by accessing the .oob_score_ attribute from the
corresponding instance.
'''
# Import DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier

# Import BaggingClassifier
from sklearn.ensemble import BaggingClassifier

# Instantiate dt
dt = DecisionTreeClassifier(min_samples_leaf=8, random_state=1)

# Instantiate bc
bc = BaggingClassifier(base_estimator=dt,
            n_estimators=50,
            oob_score=True,
            random_state=1)



'''
OOB Score vs Test Set Score
'''
# Fit bc to the training set
bc.fit(X_train, y_train)

# Predict test set labels
y_pred = bc.predict(X_test)

# Evaluate test set accuracy
acc_test = accuracy_score(y_test, y_pred)

# Evaluate OOB accuracy
acc_oob = bc.oob_score_

# Print acc_test and acc_oob
print('Test set accuracy: {:.3f}, OOB accuracy: {:.3f}'.format(acc_test, acc_oob))

'Test set accuracy: 0.698, OOB accuracy: 0.704'



'''
Train an RF regressor
'''
# Import RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor

# Instantiate rf
rf = RandomForestRegressor(n_estimators=25,
            random_state=2)

# Fit rf to the training set
rf.fit(X_train, y_train)




'''
Evaluate the RF regressor
'''
# Import mean_squared_error as MSE
from sklearn.metrics import mean_squared_error as MSE

# Predict the test set labels
y_pred = rf.predict(X_test)

# Evaluate the test set RMSE
rmse_test = MSE(y_test, y_pred) ** (1/2)

# Print rmse_test
print('Test set RMSE of rf: {:.2f}'.format(rmse_test))



'''
Visualizing features importances

In this exercise, you'll determine which features were the most predictive according
to the random forests regressor rf that you trained in a previous exercise.
'''
# Create a pd.Series of features importances
importances = pd.Series(data=rf.feature_importances_,
                        index= X_train.columns)

# Sort importances
importances_sorted = importances.sort_values()

# Draw a horizontal barplot of importances_sorted
importances_sorted.plot(kind='barh', color='lightgreen')
plt.title('Features Importances')
plt.show()
