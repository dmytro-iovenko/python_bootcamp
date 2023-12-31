import pandas as pd

### Series At A Glance ###
# Skill Challenge 1
# create series
#actor_names = ['Tom Hanks', 'Robert De Niro', 'Tom Cruise', 'Brad Pitt']
#actor_ages = [60, 74, 55, 51]
#actors_series = pd.Series(data=actor_ages, index=actor_names, name='actors')
#actors_series_from_dict = pd.Series(dict(zip(actor_names, actor_ages)))
#print(actors_series_from_dict)

# Skill Challenge 2
# create a series of length 100 containing the squares of integers from 0 to 99
#squares = pd.Series(data=i**2 for i in range(100))
#squares = pd.Series(i**2 for i in range(0,100))
# extract the last 3 items using square bracket indexing
#squares[-3:]
# repeat step 2 using .tail() method
#squares.tail(3)
# verify that the output of steps 2 and 3 is the same using the .equals() method
#print(squares[-3:].equals(squares.tail(3)))

### Series Methods And Handling ###
# Skill Challenge 3
# isolate the non-nulls in the alcohol series and assign them to the variable wine_servings
#alcohol = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country').squeeze('columns')
#wine_servings = alcohol.loc[alcohol.notnull()]
# what is the total wine consumed by countries in wine_servings? -- 8221.0
#total = wine_servings.sum() 
# in the wine_servings dataset, what is the total wine consumed by countries that consumed less than 100 servings? -- 2416.0
#total_less100 = wine_servings[wine_servings<100].sum() 

# Skill Challenge 4
# select all the countries from alcohol that have more then 50 wine servings, and save them in a variable fifty_plus
#fifty_plus = alcohol[alcohol>50]
# from fifty_plus, choose the counties with the smallest 20 wine servings values
#smallest20 = fifty_plus.nsmallest(20)
# what is the mean, median and standart deviation for the sample from step 2?
#smallest20.mean() # 74.25
#smallest20.median() # 73.5
#smallest20.std() #19.07

# Skill Challenge 5
# read the drinks.csv, bringing the beer_servings sequence into a new series 'beers' with country acting as the index.
beers = pd.read_csv('drinks.csv', usecols=['country', 'beer_servings'], index_col='country').squeeze('columns')
# calculate the mean, median, and standart deviation. Is the distribution right or left skewed?
ser_mean = beers.mean() # 102.87078651685393
ser_median = beers.median() # 60.0
ser_std = beers.std() # 100.6457126793478 - Right skewed
# slace the first 10 countries from beers
first_ten = beers[:10]
# are these relatively large or small relative to the rest of the sample? 
a = (beers - ser_mean).apply(lambda x: 'low' if x<0 else 'high').value_counts() # small
# better way - to calculate standart scores (z-scores)
z_scores = first_ten.apply(lambda x: (x-ser_mean)/ser_std)
#z_scores = (beers - beers.mean())/beers.std()
print(z_scores)
#z_scores.abs().max() - take only positive values and then max value or 
# beers.idxmax()
