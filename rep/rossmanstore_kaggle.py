import pandas as pd 
train = pd.read_csv("trainpandas.csv")
output_file = 'anuragkaggle1994.csv'
test = pd.read_csv("testpandas.csv")
train = train.loc[train.Sales > 0 ]
print(train.head())
median_by_week = train.groupby(['DayOfWeek' , 'Store' , 'Promo'])['Sales'].mean()
median_by_week = median_by_week.reset_index()
test2 = pd.merge( test , median_by_week , on = ['DayOfWeek' , 'Store' , 'Promo'], how = 'left')
assert(len(test2) == len(test))
#print(test2.head())
test2[['Id' , 'Sales']].to_csv(output_file , index = False)
#print(test.head())