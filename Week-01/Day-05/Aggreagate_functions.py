#Aggregrate Functions
import numpy as np
c=np.array([[1,2,3],[6,7,8]])
b=np.array([[5,6,5],[8,7,6]])

#Sum----
print(np.sum(c))
print(np.sum(c, axis=0))

#mean---
print(np.mean(b))

#maximum---
a = 10
b = 21
print(np.maximum(a, b))

#minimum----
print(np.minimum(a, b))
