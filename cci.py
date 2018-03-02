# code for generating CCI indicator


data = BTC2017mean # 1 dimensional array of price data (averaged from 4 exchanges)
data = pd.DataFrame(data)
ndays = 20
BTCCCI = (data - pd.rolling_mean(data, ndays)) / (0.015 * pd.rolling_std(data, ndays))
