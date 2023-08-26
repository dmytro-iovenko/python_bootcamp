import pandas as pd
import numpy as np
import re

### Regex and Text Manipulation ###

boston = pd.read_csv('2017BostonMarathonTop1000.csv')

## string methods in Python: len(), center(), startswith(), endswith(), 'in' operator ##
s = 'Welcome to the text manipulation section'
len(s) # 40
s.center(100, '*')
#******************************Welcome to the text manipulation section******************************
s.endswith('tion') # True
s.startswith('W') # True
# how about icludes? -- use 'in' operator
'text' in s # True
# text transform within list comprehensions
names = ['Alanah', 'Albion', 'Andrew', 'Brian']
[len(name) for name in names]   # [6, 6, 6, 5]
[name.startswith('A') for name in names] # [True, True, True, False]
## vectorized string operations in Pandas ##
boston.Name.str.len()  # str - accesser to vectorized string operations
# 1    14
# 2    15
## case operations ##
boston.City.str.upper()
boston.City.str.lower()
boston.City.str.swapcase()
boston.City.str.capitalize()
## finding characters and words: find(), rfind() ##
# find()
s.find('x') # 17 - character position in the string (the first occurence)
s.find('text') # look for part of the string; 15 - start position for substring; -1 - not found
boston.Name.str.find('Andy').value_counts()
# -1     998
#  8       1
#  12      1
# rfind() - from the right
p = 'pandas numpy numpy pandas'
p.find('pandas')  # 0
p.rfind('pandas') # 19 - pos of substring
## strips and whitespace: isspace(), lstrip(), rstrip(), strip() ##
'\n'.isspace() # True
left_spaced = '   this is a pandas course'
right_spaced = 'we cover python too!   '
spaced = '  the name is: BOND \t JAMES BOND \n\n'
left_spaced.lstrip()
right_spaced.rstrip()
spaced.strip() # the name is: BOND        JAMES BOND -> still have \t
boston.Name = boston.Name.str.strip()
## splitting and concatenation: split(), get(), cat() ##
s.split() # ['Welcome', 'to', 'the', 'text', 'manipulation', 'section']
# Kirui, Geoffrey -> need to remove ','
boston.Name.str.split(', ') # [Kirui, Geoffrey]
# to extract the first item use str.get() method
boston['First Name'] = boston.Name.str.split(', ').str.get(1) # Geoffrey
boston['Last Name'] = boston.Name.str.split(', ').str.get(0) # Kirui
# to combine age ('Age')& gender('M/F') use str.cat()
boston['M/F'].str.cat(boston.Age.astype(str), sep='_') # M_43
## more split parameters ##
# drop previously created columns
boston.drop(['First Name', 'Last Name'], axis=1, inplace=True)
# the expand param
boston.Name.str.split(', ', expand=True) # result - a dataframe
# 997       Mccue  Daniel T
# 998      Larosa      John
# 999     Sanchez     Sam R
boston.Name.str.split(expand=True) # result - 5 columns
# 997       Mccue,    Daniel     T  None  None
# 998      Larosa,      John  None  None  None
# 999     Sanchez,       Sam     R  None  None
boston.Name.str.split(expand=True).count(axis=1)
# 997    3
# 998    2
# 999    3
boston.Name.str.split(expand=True).count(axis=1) == 5
# 998    False
# 999    False
boston.Name[boston.Name.str.split(expand=True).count(axis=1) == 5] # 5 names that have all 5 components
# 203    Cifuentes Fetiva, Miguel Angel Sr. 
# 467      Martinez Solano, Juan Manuel Jr.
# 678        Melendez, Carlos Manuel M. Sr.
# 733        Castano Gonzalez, Angel U. Sr.
# to control namber of columns, specify n parameter
boston.Name.str.split(expand=True, n=1) # n=2 -> 2 col, n=2 -> 3 col
# 998      Larosa,      John
# 999     Sanchez,     Sam R
# [1000 rows x 2 columns]
boston.Name.str.split(', ', expand=True, n=1)
#        0         1
# 0  Kirui  Geoffrey
# 1   Rupp     Galen
# setting with enlargement: if the columns exist - they will be overwritten, otherwise - created new
boston[['First Name', 'Last Name']] = boston.Name.str.split(', ', expand=True, n=1)
#               Name  Age M/F      City State Country Official Time  Overall  Gender Years Ran First Name Last Name
# 0  Kirui, Geoffrey   24   M  Keringet   NaN     KEN       2:09:37        1       1       NaN      Kirui  Geoffrey
# 1      Rupp, Galen   30   M  Portland    OR     USA       2:09:58        2       2       NaN       Rupp     Galen

# Skill Challenge 17 - selecting string
# 1) how many runners have 'James' as a Last Name
boston['Last Name'].str.find('James').value_counts() # 12
# -1    988
#  0     12
# 2) split all the City names in the dataset by the hyphen character "-", 
# and create a dataframe (city_parts) containing each split component of the split name
city_parts = boston.City.str.split('-', expand=True)
# 3) how many cities in the boston dataframe have more than 1 component?
boston[city_parts.count(axis=1) > 1].City.count() # 13
boston[city_parts.count(axis=1) > 1].City
# 2                    Machida-City
# 35                 Sao Paulo - Sp
# 188                  Baie-St-Paul
# 201            Houghton-Le-Spring
# 371          Boulogne-Billancourt
# 420                    Mont-Royal
# 585                Gif-Sur-Yvette
# 615        Fossambault-Sur-Le-Lac
# 724         Wiesbaden-Breckenheim
# 727                    Saint-Tite
# 794                   Marica - Rj
# 820    Sainte-Catherine-De-Hatley
# 830                    Pont-Rouge

## slicing substrings ##
# s = 'Welcome to the text manipulation section'
# Python:
s[slice(0, 7, 1)] # Welcome
s[slice(7)] # Welcome -> start=0 and step=1 - default values
s[0:7:1] # Welcome
s[:7:] # Welcome
# Pandas:
boston.Country.str.slice(0, 2, 1) # US
boston.Country.str.slice(-2, None, 1) # SA - slicing from the right
## masking with string methods ## 
# - create sequence of booleans
# - use sequence to select from dataframe (or series)
# Q: select all the Italian runners
boston.Country.str.match('ITA') # sequens of booleans
boston.loc[boston.Country.str.match('ITA')]
# Q: how about all the "Will"s? (contains)
wills = boston.Name.str.contains('Will') # sequens of booleans
boston[wills]
forty5_plus = boston.Age >= 45
boston[wills & forty5_plus]
## parsing indicators with get_dummies()
boston[boston['Years Ran'].notnull()] # values in output : 2015, 2015:2016, 2016
# for analysis better to have 2 separate columns. Use get_dummies() method with separator sep=':'
dummies = boston['Years Ran'].str.get_dummies(sep=':') # dataframe of indicator variables
#      2015  2016
# 0       0     0
# 1       0     0
# 2       0     0
# 3       0     0
# 4       1     0
# the df.insert() to add those column to our dataset next to 'Years Ran'
boston.insert(boston.columns.get_loc('Years Ran'), 'Ran 2015', dummies['2015'])
boston.insert(boston.columns.get_loc('Years Ran'), 'Ran 2016', dummies['2016']) # Ran 2015  Ran 2016 Years Ran
# Q: which top runners from 2017 also ran in the previous two Boston marathons
boston[(boston['Ran 2015'] == 1) & (boston['Ran 2016'] == 1)]
# Q: which top runners from 2017 also ran in 2015
boston['Ran 2015'].sum() # 190
## text replacement ##
s += '. This section is about text.'
s = s.replace('text', 'string')
boston['M/F'] = boston['M/F'].str.replace('F', 'Female').str.replace('M', 'Male') # Pandas
# case-insensitive replacements
boston.Country.str.replace('USA', 'United States', case=False)
## Regex: is this a valid email? ##
# the re module, email regex, pitfalls, additional resource: https://emailregex.com/
# define the pattern for email: \w\S*@.*\w
pattern = r'\w\S*@.*\w' # r - raw string
re.findall(pattern, 'andy@howto pandas.com') # ['andy@howto pandas.com']
# masking: andy@gmail.com -> ****@gmail.com
# - start with an actually valid email
# - capture the domain part of the email
# - replace everything except the captured group
email = 'andy@howto pandas.com'
pattern = r'\w\S*(@.*\w)'
print(re.sub(pattern, r'*****\1', email )) # \1 -> refer to the first captured group
# *****@howto pandas.com
# for production projects use compile() to get pattern object
robust_pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
# re.compile('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$)')
## pandas str contains(), split(), and replace() with regex
# contains()
boston.Name[boston.Name.str.contains('Will')] # we can use regex:
boston.Name[boston.Name.str.contains(r'Will', regex=True)] # the same output 
# isolate first name Wills
boston.Name[boston.Name.str.contains(r',\s[wW]ill', regex=True)]
# isolate first name exact Will
boston.Name[boston.Name.str.contains(r',\s[wW]ill$', regex=True)] # Will -> $ - indicates end of the string
# or use \b : r',\s[wW]ill\b' to get names like Will J.
# split()
boston.Name.str.split(r'\s', expand=True)
# replace()
boston['Official Time'] # 2:09:58
boston['Official Time'].str.replace(r'(\d+):(\d+):(\d+)', r'\1 hours, \2 minutes, and \3 seconds') #2 hours, 09 minutes, and 58 seconds

