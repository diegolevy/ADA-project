import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import multilabel_confusion_matrix
import numpy as np
df_final = pd.read_csv('df_final.csv')
df_total = pd.read_csv('df_total.csv')
df_total = pd.get_dummies(df_total,columns=['FTR'])
BbAvA = df_final["BbAvA"]
BbAvD = df_final["BbAvD"]
BbAvH = df_final["BbAvH"]
frame = {"BbAvH": BbAvH,"BbAvD": BbAvD, 'BbAvA': BbAvA}

df_odds = pd.DataFrame(frame)
y_pred_market = np.zeros((1900,3))
y_pred_market1 = pd.DataFrame(y_pred_market,columns=['HomeW','Draw','AwayW'])

y_pred_market1['HomeW']= ((df_odds['BbAvH'] <= df_odds['BbAvA']) & (df_odds['BbAvH'] <= df_odds['BbAvD']))*1
y_pred_market1['AwayW']= ((df_odds['BbAvA'] <= df_odds['BbAvH']) & (df_odds['BbAvA'] <= df_odds['BbAvD']))*1
y_pred_market1['Draw']= ((df_odds['BbAvD'] <= df_odds['BbAvA']) & (df_odds['BbAvD'] <= df_odds['BbAvH']))*1



y_true = df_total[['FTR_H', 'FTR_D', 'FTR_A']]

y_true.rename(columns={'FTR_H': 'HomeW', 'FTR_D': 'Draw','FTR_A':'AwayW' }, inplace=True)

print("Accuracy score for Market: ", accuracy_score(y_true=y_true, y_pred=y_pred_market1))


cf_mat_svm = multilabel_confusion_matrix(y_true= y_true, y_pred=y_pred_market1)
print (cf_mat_svm)

part1 = y_true[y_pred_market1 == 1]
part2 = part1[part1 == 1].fillna(0)

x = np.multiply(part2,df_odds)
y = x.sum()
z = sum(y)
print(z/(len(df_odds)))

y_pred_market1.sum()


