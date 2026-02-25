import numpy as np
a=np.array([1,3,5])
print(a)

#2 dim------
b=np.array([[1,3,4],[4,5,6]])
print(b)

#3 dim------
c=np.array([[[1,2,3],[5,6,7],[8,6,3]]])
print(c)

#Shape---------
print(a.shape)
print(b.shape)
print(c.shape)
print(c.dtype)
print(c.ndim)

d=np.zeros((2,3))
print(d)
e=np.ones((3,3))
print(e)
f=np.arange(0,10)
print(f)

g=np.eye(3)
print(g)
h=np.diag([1,3,6])
print(h)
