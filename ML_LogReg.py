###########################################
# Logistic Regression
###########################################
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import cross_val_score

df_ML = pd.read_csv('df_ML.csv')
df_final = pd.read_csv('df_final.csv')
BbAvA = df_final["BbAvA"]
BbAvD = df_final["BbAvD"]
BbAvH = df_final["BbAvH"]
frame = {"BbAvH": BbAvH,"BbAvD": BbAvD, 'BbAvA': BbAvA}

df_odds = pd.DataFrame(frame)
df_odds1 = df_odds.iloc[1615:,:]

X = df_ML.iloc[:,5:24].values
y = df_ML.iloc[:,4].values # scores : AwayWin , Draw, HomeWin


min_max_scaler = MinMaxScaler()
min_max_scaler.fit(X)
X_normalized_min_max = min_max_scaler.transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_normalized_min_max, y, test_size= 0.15, shuffle=False)

logreg = LogisticRegression(multi_class='ovr', solver= 'lbfgs') # different solver:‘newton-cg’, ‘lbfgs’, ‘liblinear’, ‘sag’, ‘saga’
logreg.fit(X_train, y_train)
y_predicted = logreg.predict(X_test)

acc_log_reg = accuracy_score(y_true = y_test, y_pred= y_predicted)

print(f'Accuracy: {acc_log_reg}')

cf_mat_logreg = confusion_matrix(y_true= y_test, y_pred=y_predicted)
print (cf_mat_logreg)

scores = cross_val_score(logreg, X_normalized_min_max, y, cv=10)

y_test = pd.get_dummies(y_test)
y_pred= pd.get_dummies(y_predicted)
part1 = y_test[y_pred == 1].fillna(0)
part2 = part1[part1 == 1].fillna(0)

x = np.multiply(part2,df_odds1)
y = x.sum()
z = sum(y)
xx = z/len(df_odds1)
print(f'The return per dollar in the logistic regression is: {xx}')


X = df_ML.iloc[:,5:24].values
y = df_ML.iloc[:,4].values
X_train, X_test, y_train, y_test = train_test_split(X_normalized_min_max, y, test_size= 0.15, shuffle=True)

logreg = LogisticRegression(multi_class='ovr', solver= 'lbfgs') # different solver:‘newton-cg’, ‘lbfgs’, ‘liblinear’, ‘sag’, ‘saga’
logreg.fit(X_train, y_train)
y_predicted = logreg.predict(X_test)
scores = cross_val_score(logreg, X_normalized_min_max, y, cv=10)


print(f'The average accuracy of the cross validation of the logistic regression is {scores.mean()} and the standard deviation is {scores.std()}')
