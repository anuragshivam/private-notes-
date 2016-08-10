# the rossmand store competition was for predicting the sales by store ID 

import pandas as pd 
train = pd.read_csv("trainpandas.csv")
output_file = 'anuragkaggle1994.csv'
test = pd.read_csv("testpandas.csv")
# i found some days where sales was zero so it was useless to use it. 
train = train.loc[train.Sales > 0 ]
print(train.head())


mean_by_week = train.groupby(['DayOfWeek' , 'Store' , 'Promo'])['Sales'].mean()
# convert it into DataFrame using reset.index()

median_by_week = median_by_week.reset_index()

test_02 = pd.merge( test , median_by_week , on = ['DayOfWeek' , 'Store' , 'Promo'], how = 'left')

#print(test2.head())
test2[['Id' , 'Sales']].to_csv(output_file , index = False)
#print(test.head())


# this type of analysis is very new to me and i am still learning 
THe pandas tutorial on kaggle was the reason i made this . I could not test it on kaggle but in data validation gave a score of 79
