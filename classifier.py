import pandas as pd

#Get the data
df=pd.read_csv('Data/crypto-markets.csv', sep=',',header=0, low_memory=False, dtype=None)

#Für Währung:
##finde weitere Währungen, die mit Handelszeitraum komplett überschneiden
### dependend Währung | Währung | date | open | close | gestiegen(boolean)
####------------------

#Klassifiziere für folgende Währung
curr_name = 'BTC'
curr = df[df['symbol'] == curr_name]['date']

curr_trade_s = curr[0]
curr_trade_e = curr[len(curr)-1]
print('start: ', curr_trade_s)
print('end:   ', curr_trade_e)



