import warnings
import sklearn.exceptions
warnings.filterwarnings("ignore", category=sklearn.exceptions.UndefinedMetricWarning)

from sklearn.metrics import accuracy_score,recall_score, precision_score, f1_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np 
from sklearn import svm


# load typhoon environmental data
typhoons_df=pd.read_csv('./TED Dataset/All_Typhoons.csv')
typhoons_df=typhoons_df.drop(['YYYYMMDDHH'], axis=1) # drop timestamp column

y_true=typhoons_df['TY'] # clone t
typhoons_df=typhoons_df.drop(['TY'],axis=1)

label_encoder = LabelEncoder()
y_true_encoded=label_encoder.fit_transform(y_true)    

acc_score = []
r_score=[]
p_score=[]
f_score=[]

kf = KFold(n_splits=10)

svm_clf=svm.SVC(gamma='auto')


for train_index, test_index in kf.split(typhoons_df):
  
  X_train, X_test = typhoons_df.iloc[train_index], typhoons_df.iloc[test_index]
  y_train, y_test = y_true_encoded[train_index], y_true_encoded[test_index]

  svm_clf.fit(X_train,y_train)
  predictions = svm_clf.predict(X_test)
  acc_score.append(accuracy_score(predictions, y_test))
  r_score.append(recall_score(y_test, predictions, average='weighted'))
  p_score.append(precision_score(y_test, predictions,  average='weighted'))
  f_score.append(f1_score(y_test, predictions, average='weighted'))

#print average scores of accuracy, precision, recall and F1-score  
print ('Average scores of Accuracy, Precision, Recall and F1-Score: ',np.mean(acc_score),np.mean(p_score), np.mean(r_score), np.mean(f_score))
