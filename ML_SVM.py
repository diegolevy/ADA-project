###########################################
# Support Machine Vectors
###########################################
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, mean_squared_error
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import cross_val_score
from matplotlib import pyplot as plt

df_final = pd.read_csv('df_final.csv')
BbAvA = df_final["BbAvA"]
BbAvD = df_final["BbAvD"]
BbAvH = df_final["BbAvH"]
frame = {"BbAvH": BbAvH,"BbAvD": BbAvD, 'BbAvA': BbAvA}

df_odds = pd.DataFrame(frame)
df_odds1 = df_odds.iloc[1615:,:]
y = []
for line in df_final.iloc:
	if line["FTR"] == 0:
		y.append(0)
	if line["FTR"] == 1:
		y.append(1)
	if line["FTR"] == 2:
		y.append(2)


df_ML = pd.read_csv('df_ML.csv')



#df_ML = pd.get_dummies(df_ML, columns = ["FTR"], prefix="result")

X = df_ML.iloc[:,5:24].values
df_ML = pd.get_dummies(df_ML, columns = ["FTR"], prefix="result")
 # scores : AwayWin , Draw, HomeWin

min_max_scaler = MinMaxScaler()
min_max_scaler.fit(X)
X_normalized = min_max_scaler.transform(X)

#min_max_scaler = MinMaxScaler()
#min_max_scaler.fit(X)
#X_normalized_min_max = min_max_scaler.transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size= 0.15, shuffle=False)

svcclassifier = SVC(kernel= 'poly', degree=3, C=1) #'linear', ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
svcclassifier.fit(X_train, y_train)
y_pred = svcclassifier.predict(X_test)

print("Accuracy score for SVM: ", accuracy_score(y_true=y_test, y_pred=y_pred))


cf_mat_svm = confusion_matrix(y_true= y_test, y_pred=y_pred)
print (cf_mat_svm)


scores = cross_val_score(svcclassifier, X_normalized, y, cv=10)
print(scores)


print("%0.2f accuracy with a standard deviation of %0.2f" % (scores.mean(), scores.std()))
y_test = pd.get_dummies(y_test)
y_pred= pd.get_dummies(y_pred)
part1 = y_test[y_pred == 1].fillna(0)
part2 = part1[part1 == 1].fillna(0)

x = np.multiply(part2,df_odds1)
y = x.sum()
z = sum(y)
print(z/(len(df_odds1)))
plt.hist(x.sum(1).values.flatten(),bins=100)
x.clip(0,10).sum(1).mean()
(x > 0).sum(1).describe()
plt.show()



c = [0.1,0.15,0.2,0.25,0.3, 0.35, 0.4,0.5, 0.6, 0.7, 0.8 ,0.9, 1, 10]

acc_score = []
for i in c:
	y = []
	for line in df_final.iloc:
		if line["FTR"] == 0:
			y.append(0)
		if line["FTR"] == 1:
			y.append(1)
		if line["FTR"] == 2:
			y.append(2)
	min_max_scaler = MinMaxScaler()
	min_max_scaler.fit(X)
	X_normalized = min_max_scaler.transform(X)
	X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size= 0.15, shuffle=False)
	svcclassifier = SVC(kernel= 'poly', degree=3, C=i) #'linear', ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
	svcclassifier.fit(X_train, y_train)
	y_pred = svcclassifier.predict(X_test)
	acc = accuracy_score(y_true=y_test, y_pred=y_pred)
	y_test = pd.get_dummies(y_test)
	y_pred = pd.get_dummies(y_pred)
	part1 = y_test[y_pred == 1].fillna(0)
	part2 = part1[part1 == 1].fillna(0)
	x = np.multiply(part2, df_odds1)
	y = x.sum()
	z = sum(y)
	xx = (z / (len(df_odds1)))
	print(f'with a C of: {i}: The Accuracy is : {acc} / The return per dollar is: {xx}')

for i in c:
	y = []
	for line in df_final.iloc:
		if line["FTR"] == 0:
			y.append(0)
		if line["FTR"] == 1:
			y.append(1)
		if line["FTR"] == 2:
			y.append(2)
	min_max_scaler = MinMaxScaler()
	min_max_scaler.fit(X)
	X_normalized = min_max_scaler.transform(X)
	X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size= 0.15, shuffle=True)
	svcclassifier = SVC(kernel= 'poly', degree=3, C=i) #'linear', ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
	svcclassifier.fit(X_train, y_train)
	y_pred = svcclassifier.predict(X_test)
	scores = cross_val_score(svcclassifier, X_normalized, y, cv=10)
	print(f'With a C of : {i}/The average accuracy of the cross validation of the SVM is: {scores.mean()} / The standard deviation is {scores.std()}')