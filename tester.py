from scraper import *

#df = query_stocks(['cap_large', 'exch_nasd'])
#df.to_csv('test.csv', index=False)
df = pd.read_csv('test.csv')
print(df.head(5))
print(df.iloc[0][1])
