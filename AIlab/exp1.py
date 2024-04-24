import numpy as np
import statistics as stat
import random
a=[]
for i in range(0,10):
    a=[random.randint(0,10)]
    a.append(random.randint(0,10))

print(a)

mean=np.mean(a)
stdev=stat.stdev(a)
print(mean)
print(stdev)


