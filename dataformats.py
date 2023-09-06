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
print(stock_dict) # {'ticker': 'GOOGL', 'shares': 10, 'book_cost': 1540.23}
