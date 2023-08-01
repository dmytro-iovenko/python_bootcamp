import pandas as pd
import numpy as np

#Skill Challenge 1
# randomly select 10 food items and assign the resulting dataframe to a new variable called nutr_mini
df = pd.read_csv('nutrition.csv', index_col='name').drop('Unnamed: 0', axis=1)
nutr_mini = df.sample(10)
# from nutr_mini, extract the total_fat and cholesterol columns for all rows
extracted_two_col = nutr_mini.iloc[:, [2,4]]
# extract all columns from vitamin_b12 to the end, for the first, second, and third rows
col_vb12 = nutr_mini.columns.get_loc('vitamin_b12') # 20
n = nutr_mini.iloc[0:3, col_vb12:]
# get the calories for the third food in nutr_mini using an attribute-based approach that is faster than .loc or .iloc
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

# find the 10 foods that have the most Vitamin B12
#nutrition.loc[:, 'vitamin_b12_mcg'].nlargest(10)
#vit_b12 = nutrition.sort_values(by=['vitamin_b12_mcg'],ascending=False).head(10).vitamin_b12_mcg # dataframe in output
vit_b12 = nutrition.vitamin_b12_mcg.nlargest(10) # series in output
# isolate the foods in the dataset that contain, or are based on, eggplant.
eggplant_food = nutrition.filter(regex='(?i)ggplant', axis=0)
# which of them has the most sodium?
#nutrition.filter(regex='(?i)ggplant', axis=0).sodium_mg.nlargest(1)
most_sodium = eggplant_food.sodium_mg.idxmax() # Eggplant, pickled - 1674
# select a slice of the dataframe that contains 4 random rows and 2 random columns
nutrition.sample(4).sample(2,axis=1)


