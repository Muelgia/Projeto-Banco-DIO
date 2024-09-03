from scipy.interpolate import *

x = [0, 12, 20]
y = [-47500, 22000, 20450]
p = lagrange(x, y)
print (p)
