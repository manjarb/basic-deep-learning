import numpy as np
import matplotlib.pyplot as plt

# load the data
X = []
Y = []
for line in open('./data_1d.csv'):
  x, y = line.split(',')
  X.append(float(x))
  Y.append(float(y))

# Turn X and Y into numpy array
X = np.array(X)
Y = np.array(Y)

# Plot to see what it is looks like
# plt.scatter(X, Y)
# plt.show()

# Apply derivative to calculate a, b
denominator = X.dot(X) - X.mean() * X.sum()
a = (X.dot(Y) - Y.mean() * X.sum()) / denominator
b = (Y.mean() * X.dot(X) - X.mean() * X.dot(Y)) / denominator

print(f'a: {a}')
print(f'b: {b}')

# calculated predicted Y
Yhat = a * X + b

# plot it all
# plt.scatter(X, Y)
# plt.plot(X, Yhat)
# plt.show()

# calculate r-squared (how good the model is)
d1 = Y - Yhat
d2 = Y - Y.mean()
r2 = 1 - (d1.dot(d1) / d2.dot(d2))
print(f'r2: {r2} good number if close to 1')