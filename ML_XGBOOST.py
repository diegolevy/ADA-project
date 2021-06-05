###########################
# Transform the data for ML
###########################

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, f1_score
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import xgboost as xgb
from xgboost import XGBClassifier
from sklearn.model_selection import cross_val_score

#######################
# Transform the data
#######################

df_final = pd.read_csv('df_final.csv')

BbAvA = df_final["BbAvA"]
BbAvD = df_final["BbAvD"]
BbAvH = df_final["BbAvH"]
frame = {"BbAvH": BbAvH,"BbAvD": BbAvD, 'BbAvA': BbAvA}

df_odds = pd.DataFrame(frame)
df_odds1 = df_odds.iloc[1615:,:]
df_ML = pd.read_csv('df_ML.csv')

y = []
for line in df_final.iloc:
	if line["FTR"] == 0:
		y.append(0)
	if line["FTR"] == 1:
		y.append(1)
	if line["FTR"] == 2:
		y.append(2)




X = df_ML.iloc[:,5:24].values
min_max_scaler = MinMaxScaler()
min_max_scaler.fit(X)
X_normalized = min_max_scaler.transform(X)




X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size= 0.15, random_state=False, shuffle=False)
# fit model no training data
model = XGBClassifier()
model.fit(X_train, y_train)
# make predictions for test data
y_pred = model.predict(X_test)
#predictions = [round(value) for value in y_pred]
# evaluate predictions
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: %.2f%%" % (accuracy * 100.0))


cf_mat_xgboost = confusion_matrix(y_true= y_test, y_pred=y_pred)
print (cf_mat_xgboost)




y_test = pd.get_dummies(y_test)
y_pred= pd.get_dummies(y_pred)
part1 = y_test[y_pred == 1].fillna(0)
part2 = part1[part1 == 1].fillna(0)

x = np.multiply(part2,df_odds1)
y = x.sum()
z = sum(y)
xx = z/len(df_odds1)
print(f'The return per dollar of the XGBoost is: {xx}')

y = []
for line in df_final.iloc:
	if line["FTR"] == 0:
		y.append(0)
	if line["FTR"] == 1:
		y.append(1)
	if line["FTR"] == 2:
		y.append(2)

X = df_ML.iloc[:,5:24].values
X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size= 0.15, random_state=False, shuffle=True)
# fit model no training data
model = XGBClassifier()
model.fit(X_train, y_train)
# make predictions for test data
y_pred = model.predict(X_test)
scores = cross_val_score(model, X_normalized, y, cv=20)
print(f'The average accuracy of the cross validation of the XGBoost is {scores.mean()}  and the standard deviation is {scores.std()}')
