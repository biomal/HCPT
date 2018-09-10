import sys
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
file_path = sys.argv[1]
df = pd.read_csv(file_path,low_memory=False)
kf = KFold(n_splits=10)
i=1
#removable_classes =  df['classification'].value_counts()[(df['classification'].value_counts() < 10)].index
#for classes in removable_classes:
 #       df = df[df.classification!=classes]
#df = df.reset_index(drop=True)

for train_index, test_index in kf.split(df): 
        train = pd.DataFrame(df.iloc[train_index])
        train_x = pd.DataFrame(train.drop(['classification'],axis=1))
        train_y = pd.DataFrame(train['classification'])
        train['classification'] = train_y
        train.to_csv('train' + str(i) + '.csv' , index=False)
        
        test = pd.DataFrame(df.iloc[test_index])
        test_x = pd.DataFrame(test.drop(['classification'],axis=1))
        test_y = pd.DataFrame(test['classification'])
        test['classification'] = test_y
        test.to_csv('test' + str(i) + '.csv' , index=False)
        i+=1
        #break