import pandas as pd
import numpy as np

## JSON ##
folks = pd.read_json('folks.json')
## HTML ##
# Q: put together a dataframe of European counties and their population
data_url = 'https://en.wikipedia.org/wiki/List_of_European_countries_by_population'
countries = pd.read_html(data_url, header=1) 
type(countries)  # 'list' len - 2 (2 tables)
countries[0] # dataframe with our data
countries = countries[0].loc[:, ['Country .mw-parser-output .nobold{font-weight:normal}(or territory)', 'Estimate']]
# renaming column labeles
countries.rename({'Country .mw-parser-output .nobold{font-weight:normal}(or territory)' : 'Country'}, axis=1, inplace=True)
# removing [Note x]
countries.replace(r'\[Note \d+\]', '', regex=True, inplace=True)
countries.set_index('Country').iloc[:10].plot(kind='bar');
## Excel ##
hobbies = pd.read_excel('folks.xlsx', sheet_name='hobbies')
## I/O -> Input/Output Creating output to_* ##
# - add a new person to the hobbies dataframe
# - save the resulting df to a csv
hobbies.loc[4] = ['Zoltan Zachary', 'Archery']
hobbies['age'] = np.random.uniform(22, 54, 5)
hobbies.to_csv() # write to csv; to_json(), to_html(), to_excel() 
hobbies.to_csv('hobbies.csv', index=False) # provide name to save it locally
## Pickling ##
# serialization
googl = {'ticker': 'GOOGL', 'shares': 10, 'book_cost': 1540.23}  
import pickle
pickle_output = open('my_stock', 'wb')
pickle.dump(googl, pickle_output)
pickle_output.close() # created  my_stock file. Not readable, so we do read binary
pickle_input = open('my_stock', 'rb')
stock_dict = pickle.load(pickle_input) # load the stream to python dict
#print(stock_dict) # {'ticker': 'GOOGL', 'shares': 10, 'book_cost': 1540.23}

# Slill Challenge 20 - reading/writing formats
# 1) using pandas, read the table directly into a pandas dataframe called positions
data_url = 'https://www.andybek.com/traders'
positions = pd.read_html(data_url)[0]
#   TraderID    Instrument   Amount Trader Location
# 0   MCBIRN     02079K107   150000              EU
# 1    WISEA     1350Z74U5  6400000              EU
# 2    IACOP  GB00B3KJDQ49  2430000              US
# 2) the positions we imported in the step above contain trader aliases
# we have more information on the name and seniority of each trader
# read this data into dataframe called traders
data_url2 = 'https://www.andybek.com/pandas-traders-names'
traders = pd.read_json(data_url2)
#              names    alias  seniority
# 0  Shylah McBirney   MCBIRN  Executive
# 1       Allen Wise    WISEA  Executive
# 2    Iacopo Brivio    IACOP     Junior
# 3   Allison Carter  CARTERA  Mid-level
# 3) combine the two dataframes from the previous steps into a dataframe that combines positions with the full name and seniority
df = pd.merge(positions, traders, left_on='TraderID', right_on='alias').drop('alias', axis=1)
# 4) save the merged dataframe from the previous step into a pickle file called picked_positions
df.to_pickle('picked_positions')
# as well as a csv file called positions.csv
df.to_csv('positions.csv', index=False)
