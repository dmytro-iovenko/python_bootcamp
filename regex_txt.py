import pandas as pd
import numpy as np

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
