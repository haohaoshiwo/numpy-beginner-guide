import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

bhp = np.loadtxt('BHP.csv', delimiter=',', usecols=(6,), unpack=True)

print(bhp)


bhp_returns = np.diff(bhp) / bhp[ : -1] #计算了增长率

vale = np.loadtxt('VALE.csv', delimiter=',', usecols=(6,), unpack=True)
print(vale)
vale_returns = np.diff(vale) / vale[ : -1]

covariance = np.cov(bhp_returns, vale_returns) 
print("Covariance", covariance)

print("Covariance diagonal", covariance.diagonal())
print("Covariance trace", covariance.trace())

print("相关系数矩阵",covariance/ (bhp_returns.std(ddof=1) * vale_returns.std(ddof=1)))


print("Correlation coefficient", np.corrcoef(bhp_returns, vale_returns))

difference = bhp - vale
print(difference)
avg = np.mean(difference)
dev = np.std(difference)

print("Out of sync", np.abs(difference[-1] - avg) > 2 * dev )

t = np.arange(len(bhp_returns))
plot(t, bhp_returns, lw=1)
plot(t, vale_returns, lw=2)
show()

