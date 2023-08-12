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

#Skill Challenge 6 - duplicates & NAs
players = pd.read_csv('soccer.csv')
#print(players.shape)
#print(players.head())
# 1) for players dataframe remove rows labeled 2,10,21 and the market_value column.
# Do not modify the underlying dataframe. Assign the result to df2
df2 = players.drop(index=[2,10,21], columns='market_value')
print(df2.shape)
# 2) does the nationality column in df2 contain only NA values? How many unique nationalities are there?
np.count_nonzero(df2[df2.nationality.isna().values]) # 0
# quick alternative : df2.nationality.isna().sum()
df2.nationality.nunique() # 61
# 3) starting from df2, isolate a datafreame slice of players that contains only the unique age-position for each club.
# Do not include the club column itself.
#x = df2[['club', 'age', 'position']].drop_duplicates().drop(columns='club') # 433,2
df2.drop_duplicates(subset=['age', 'club', 'position'], keep = 'first').loc[:, ['age', 'position']]

#Skill Challenge 7 - apply() function
# 1) create a standalong function that
#    - accepts a single parameter x
#    - returns the string 'relatively unknown' if x < 200 
#    - 'kind of popular' if x >= 200 and x < 600
#    - 'popular' if x >= 600 and x < 2000
#    - 'super-popular' oterwise
def get_popularity(x):
    if x < 200:
        return 'relatively unknown'
    elif x < 600:
        return 'kind of popular'
    elif x < 2000:
        return 'popular'
    else:
        return 'super-popular'

# 2) apply the function from the step1 to the players page_views column. Use a method that supports vectorized operations
players.page_views.apply(get_popularity)
# 3) add the output from the step2 as a new column 'popularity' to the players dataframe
players['popularity'] = players.page_views.apply(get_popularity)
# 4) how many "super-popular" players are there? - 37
len(players[players.popularity =='super-popular'])
#print(players[players.popularity =='super-popular'].name.size)

#Skill Challenge 8 - adding row/column 
# 1) from the players dataframe select 4 rows and 4 columns, of no particular order. Assign the result to df_random
#df_random = players.sample(4).sample(4, axis=1)
df_random = players.loc[[15,451,29,312],['name', 'age', 'page_views', 'club']]
# 2) extend df_random vertically by adding a new row, and horizontally by adding a new column. Do this as 2 separate operations
alex = pd.Series({
    'name': 'Alex',
    'age': 23,
    'page_views': 730,
    'club': 'Arsenal'
}, name = 5)
df_random = df_random.append(alex)
#df_random['goals'] = [1, 3, 2, 1, 1]
df_random = df_random.assign(goals=[1, 3, 2, 1, 1])

### Working With Multiple DataFrames ###

#Skill Challenge 9 - concatenating dataframes 
state = pd.read_csv('state.csv')
liberal = pd.read_csv('liberal_arts.csv')
# 1) concetenate the liberal and state schools into a new dataframe
new_df = pd.concat([liberal, state])
# how many unique school names there?
# new_df.nunique() >> will show all columns
new_df['School Name'].nunique() # 222
# 2) what is the average median starting salary in the dataframe created above?
mean_mms = new_df['Starting Median Salary'].replace('[$, ]','', regex=True).astype(float).mean() # 44469.36936936937 # .replace(r'\$|,','', regex=True)
# 3) create a short dataframe that shows the top3 liberal arts and state schools that produce the highest(mid-career) earning graduates
# show the School Name and Mid-Career Median Salary columns from each dataset side by side, i.e. horizontally
# bonus: nest the column labels within 'Liberal Arts' and 'State' labeles
liberal2 = liberal.sort_values(by='Mid-Career Median Salary', ascending=False)[:3].reset_index(drop=True)
state2 = state.sort_values(by='Mid-Career Median Salary', ascending=False)[:3].reset_index(drop=True)
short_df = pd.concat([liberal2,state2], axis=1, keys=['Liberal Arts', 'State'])  

#Skill Challenge 10 -
# 1) merge liberal arts schools with regions and assign the resulting dataframe to dfm
regions = pd.read_csv('regions.csv')
dfm = pd.merge(liberal, regions, on='School Name')
# what region has the highest number of liberal arts schools?
#dfm.loc[:,'Region'].value_counts() # Northeastern - 25
dfm.Region.value_counts()
# 2) set school_name as the index of the mid_career dataset
mid_career = pd.read_csv('mid_career_salaries.csv')
mid_career.set_index('school_name', inplace=True)
# 3) merge tha dfm and mid_career dataframes. 
pd.merge(dfm, mid_career, left_on='School Name', right_index=True)
# is the join operation one-to-one?
left_key = mid_career.index
right_key = dfm['School Name']
left_key[left_key.isin(right_key)].value_counts() # Randolph-Macon College - 2 1-M






