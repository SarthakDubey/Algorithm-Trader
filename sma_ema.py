# code for calculating simple (50 day)  & exponential (200 day)  weighted averages


# Simple Moving Average
def SMA(data, ndays):
 SMA = pd.Series(pd.rolling_mean(data['Close'], ndays), name = 'SMA')
 data = data.join(SMA)
 return data

# Exponentially-weighted Moving Average
def EWMA(data, ndays):
 EMA = pd.Series(pd.ewma(data['Close'], span = ndays, min_periods = ndays - 1),
 name = 'EWMA_' + str(ndays))
 data = data.join(EMA)
 return data

 # Compute the 50-day SMA for BTC
n = 50
SMA_BTC = SMA(data,n)
SMA_BTC = SMA_BTC.dropna()
SMA = SMA_BTC['SMA']

# Compute the 200-day EWMA for BTC
ew = 200
EWMA_BTC = EWMA(data,ew)
EWMA_BTC = EWMA_BTC.dropna()
EWMA = EWMA_BTC['EWMA_200']
