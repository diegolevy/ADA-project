###########################
# Transform the data for ML
###########################

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RepeatedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
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
# Let's put the betting odds in a separate dataframe for now
df_ML = pd.read_csv('df_ML.csv')


# Our benchmark for the market predictions will be BetBrain (overs 185 bookmakers included)

df_ML = pd.get_dummies(df_ML, columns = ["FTR"], prefix="result")

X = df_ML.iloc[:,4:24].values
y = df_ML.iloc[:,24:].values # scores : AwayWin , Draw, HomeWin

min_max_scaler = MinMaxScaler()
min_max_scaler.fit(X)
X_normalized = min_max_scaler.transform(X)

######################################
# kNN --> used to test the techniques
######################################

# 1) Classical cross validation (then try forward cross validation)

X_train,X_test,y_train,y_test = train_test_split(X_normalized, y, test_size= 0.15, shuffle= False)


knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_predicted = knn.predict(X_test)

print("Accuracy score: ", accuracy_score(y_true=y_test, y_pred=y_predicted))
print("f1 score: ", f1_score(y_true = y_test, y_pred = y_predicted, average= "weighted"))



y_test = pd.DataFrame(y_test)
y_predicted = pd.DataFrame(y_predicted)
part1 = y_test[y_predicted == 1].fillna(0)
part2 = part1[part1 == 1].fillna(0)

x = np.multiply(part2,df_odds1)
y = x.sum()
z = sum(y)
xx = z/len(df_odds1)
print(f'The return per dollar in the KNN is: {xx}')
plt.hist(x.sum(1).values.flatten(),bins=100)
x.clip(0,10).sum(1).mean()
(x > 0).sum(1).describe()
plt.show()

X = df_ML.iloc[:,4:24].values
y = df_ML.iloc[:,24:].values
X_train,X_test,y_train,y_test = train_test_split(X_normalized, y, test_size= 0.15, shuffle= True)


knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_predicted = knn.predict(X_test)
scores = cross_val_score(knn, X_normalized, y, cv=10)

print(f'The average accuracy of the cross validation of the KNN is {scores.mean()}  and the standard deviation is {scores.std()}')
