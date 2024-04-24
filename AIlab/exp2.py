import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import statistics as stat

df=pd.read_csv(r'C:/Users/PC/Desktop/Afeef/PYTHOn/AIlab/lois_continuous.csv')
df_new=df[df['ID']=='S1']
t=df_new['Temperature water continuous']
o=df_new['Oxygen dissolved continuous']

fig,ax=plt.subplots(figsize=(10,7))
plt.hist(t,7)
#plt.hist(o,7)
plt.title('histo')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

mean=np.mean(t)
print(mean)
med=stat.median(o)
print(med)
