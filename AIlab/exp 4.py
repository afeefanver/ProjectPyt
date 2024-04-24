import pandas as pd
import csv
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
df=pd.read_csv(r'C:/Users/PC/Desktop/Afeef/PYTHOn/AIlab/glass.csv')
print(df.head(0))
features=['RI','Na','Mg','Al','Si','K','Ca','Ba','Fe']
x=df[features]
y=df.Type
x_train_x_test,y_train,y_test=train_test_split(x,y,test_size=0.5,random_state=10)
clf=GaussianNB()
clf=clf.fit(x_train,y_train)
y_pred=clf.predict(x_test)

cm=confusion_matrix(y_test,y_pred)
cr=classification_report(y_test,y_pred)
acc=accuracy_score(y_test,y_ped)
print('cm',cm)
print('cr',cr)
print('acc',acc)
