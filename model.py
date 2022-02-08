import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier
import pickle

training_data=pd.read_csv('./train_set_rain (1).csv')
X_train=training_data.drop(['Day','T','Tm','V','RA_tomor'],axis=1)
y_train=training_data['RA_tomor']

sm=SMOTE(random_state=0)
X_train_res, y_train_res = sm.fit_resample(X_train, y_train)


xg_clf = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
xg_clf.fit(X_train_res,y_train_res)


pickle.dump(xg_clf, open("model_xg.pkl", "wb"))