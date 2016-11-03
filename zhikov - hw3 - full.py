import pandas as pd

def tasks (house_prices):
	#1
	quantiles = [0.0, 0.25, 0.5, 0.75, 1.0]
	#2
	grouped = house_prices.groupby(pd.cut(house_prices["SalePrice"], 	
	house_prices["SalePrice"].quantile(quantiles)))
	for name, group in sorted(grouped):
	    print name 
	    print "YearBuilt: ", group['YearBuilt'].mean()
	    print "Kitchen: ", group['KitchenAbvGr'].mean(), '\n'
	#3
	regrouped = house_prices.groupby('Functional')
	print regrouped['SalePrice'].mean()

house_prices = pd.read_csv('house_prices.csv')
house_prices.head()
house_prices.columns.to_series().groupby(house_prices.dtypes).groups

tasks(house_prices)
