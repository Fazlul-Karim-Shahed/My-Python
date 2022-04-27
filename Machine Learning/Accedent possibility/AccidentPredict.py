
import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def plot(data_set, x, y):
    plt.scatter(data_set[x], data_set[y])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()

data_set = pandas.read_csv('car driving risk analysis.csv')
# print(data_set)

# plot(data_set, "speed", "risk")

x = data_set[['speed']]
y = data_set[['risk']]

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.3, random_state=1)

reg = LinearRegression()
reg.fit(xtrain, ytrain)

res = reg.predict(xtest)

plt.scatter(data_set['speed'], data_set['risk'])
plt.plot(data_set['speed'], reg.predict(data_set[['speed']]))
plt.show()