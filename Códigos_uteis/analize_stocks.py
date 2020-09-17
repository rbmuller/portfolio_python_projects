import quandl

quandl.ApiConfig.api_key='BDxKWwyY3cp38Yv-ykE2'

petr4 = quandl.get("GOOG/BVMF_PETR4")
print (petr4.index)
print (petr4.head)


import matplotlib.pyplot as plt
(prices/prices.iloc[0]*100).plot(figsize=(15,5))
plt.ylabel('NORMALIZED PRICES')
plt.xlabel('DATE')
plt.show()

quandl.get(help)


import yahoo_finance

