import pandas as pd
import numpy as np

#Skill Challenge 1
# 1) randomly select 10 food items and assign the resulting dataframe to a new variable called nutr_mini
df = pd.read_csv('nutrition.csv', index_col='name').drop('Unnamed: 0', axis=1)
nutr_mini = df.sample(10)
# 2) from nutr_mini, extract the total_fat and cholesterol columns for all rows
extracted_two_col = nutr_mini.iloc[:, [2,4]]
# 3) extract all columns from vitamin_b12 to the end, for the first, second, and third rows
col_vb12 = nutr_mini.columns.get_loc('vitamin_b12') # 20
n = nutr_mini.iloc[0:3, col_vb12:]
# 4) get the calories for the third food in nutr_mini using an attribute-based approach that is faster than .loc or .iloc
col_calories = nutr_mini.columns.get_loc('calories') # 1
cal = nutr_mini.iat[2,1] # 185

#Skill Challenge 2
# data preparation
# collect units
units = df.astype(str).replace('[^a-zA-Z]','',regex=True).mode()
# remove columns with empty values
units = units.replace('', np.nan).dropna(axis=1)
# rename labels (columns) to not lose data
# create mapper
mapper = {k : k + '_' + units[k].at[0] for k in units}
nutrition = df.rename(columns=mapper)
# remove units from values
nutrition.replace('[a-zA-Z]','',regex=True,inplace=True)
# cast to float
nutrition = nutrition.astype(float)

# 1) find the 10 foods that have the most Vitamin B12
#nutrition.loc[:, 'vitamin_b12_mcg'].nlargest(10)
#vit_b12 = nutrition.sort_values(by=['vitamin_b12_mcg'],ascending=False).head(10).vitamin_b12_mcg # dataframe in output
vit_b12 = nutrition.vitamin_b12_mcg.nlargest(10) # series in output
# 2) isolate the foods in the dataset that contain, or are based on, eggplant.
eggplant_food = nutrition.filter(regex='(?i)ggplant', axis=0)
# which of them has the most sodium?
#nutrition.filter(regex='(?i)ggplant', axis=0).sodium_mg.nlargest(1)
most_sodium = eggplant_food.sodium_mg.idxmax() # Eggplant, pickled - 1674
# 3) select a slice of the dataframe that contains 4 random rows and 2 random columns
nutrition.sample(4).sample(2,axis=1)

#Skill Challenge 3
# 1) remove all the food items that contain at least one NaN. Do this in a way that modifies the dataframe.
nutrition.dropna(inplace=True)
# How many food items remain after the exclusion?
nutrition.count() # 7199
len(nutrition) # 7199
# 2) from the remaining records, isolate those that have between 20 and 40 mg of Vitamin C per 100g serving.
nutrition[nutrition.vitamin_c_mg.between(20,40)]
# of these foods, which one is the least caloric, i.e. has the minimum calories?
nutrition.nsmallest(1,'calories') # Asparagus
# 3) how many food items in the dataframe have Vitamin C levels of between 2 and 3 standart deviations (inclusive) above the mean?
m = nutrition.vitamin_c_mg.mean() # 5.55
mp2sd = m + nutrition.vitamin_c_mg.std() * 2 # 97.76
mp3sd = m + nutrition.vitamin_c_mg.std() * 3 # 143.87
nutrition[nutrition.vitamin_c_mg.between(mp2sd, mp3sd)].shape # (17,75)

#Skill Challenge 4 - combining conditions
# find the players that meet these criteria:
# 1) they're English (nationality)
players = pd.read_csv('soccer.csv')
english_players = players[players.nationality=='England'] # 158
# 2) and their market value is more than twice the average market value in the league (market_value), and
mean_mv = players.market_value.mean() # 11.125649350649349
players[(players.nationality == 'England') & (players.market_value > mean_mv * 2)]
# 3) they either have more than 4,000 views (page_views) or are a new signing (new_signing) but not both
# x = (players[(players.nationality == 'England') & (players.market_value > mean_mv * 2) & (players.page_views > 4000)]) | \
#     (players[(players.nationality == 'England') & (players.market_value > mean_mv * 2) & (players.new_signing == 1)])
players[(players.nationality == 'England') & (players.market_value > mean_mv * 2) & ((players.page_views > 4000) | (players.new_signing == 1))] 
# result: 3 rows John Stones, Dele Alli, Harry Kane 
### Another approach with XOR ###
english = players.nationality=='England'
above_average = players.market_value > mean_mv * 2
popular_xor_new = (players.page_views > 4000) ^ (players.new_signing == 1)
players.loc[english & above_average & popular_xor_new]

#Skill Challenge 5 - sorting by index/column
# 1) sort the players un the players by the age in ascending order.#
players.sort_values(by='age')
# who is the youngest footballer in the EPL?
players.sort_values(by='age').iat[0,0]  # Ben Woodburn - 17
# another way to find the youngest player w/o sorting index: idxmin() - players.iloc[players.age.idxmin()]
# players.sort_values(by='age').iloc[0] - another approach
# 2) set the club column as the index of the dataframe
# then sort the dataframe index in alphabetical order
players.set_index('club',inplace=True)
players.sort_index(inplace=True)
# 3) sort the dataframe values by club and market_value where the club is alphabetical and the market value is in descending order
players.sort_values(by=['club','market_value'], ascending=[True, False]) # Arsenal     Alexis Sanchez




