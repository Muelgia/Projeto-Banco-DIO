import numpy as np

u = np.array([[3, 4, 8]]) 
v = np.array([[10, 12, -1]])
m = u * v
print(m)

w = np.inner(u,v)
print(w)

