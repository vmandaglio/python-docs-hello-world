import numpy as np

a = np.array([[6,1,1],[4,-2,5],[2,8,7]])
print(a)
print(np.linalg.det(a))

b = np.array([1,1,3])
c = np.array([4,10,6])
k = np.array([0,8,9])
d = np.array([b,c,k])
print(d)
print(np.linalg.det(d))