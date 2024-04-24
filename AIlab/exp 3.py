import pandas as pd
import numpy as np
df = pd.read_csv("C:/Users/PC/Desktop/Afeef/PYTHOn/AIlab/diabetes.csv")
print(df.head())
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
feature_col=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']
x=df[feature_col]
y=df.Outcome
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.3,random_state=1)
clf=DecisionTreeClassifier()
clf=clf.fit(x_train,y_train)
yPred=clf.predict(x_test)
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
result=confusion_matrix(y_test,yPred)
rslt=classification_report(y_test,yPred)
acc=accuracy_score(y_test,yPred)
print('Result 1\n',result)
print('Result 2\n',rslt)
print('Accuracy\n',acc)
