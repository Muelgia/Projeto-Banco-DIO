from sklearn.datasets import make_regression
import matplotlib.pyplot as plt


x, y = make_regression(n_samples=200, n_features=1, noise=30)

plt.scatter(x,y)
plt.show()