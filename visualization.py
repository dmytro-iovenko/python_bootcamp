# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### Data Visualization ###
## matplotlib ##

# generate random data
# %%
x = np.random.normal(size=400);
y = np.random.normal(size=400);
#plt.plot(x) # [<matplotlib.lines.Line2D object at 0x000002ABD56BF210>]
# plt.style.available;
# plt.style.use('ggplot');
# plt.plot(x.cumsum(), label='x');
# plt.plot(y.cumsum(), label='y', color='purple');
# plt.legend();
# %%
figure, axes = plt.subplots();
axes.plot(x.cumsum(), label='x');
axes.plot(y.cumsum(), label='y');
axes.legend(loc='upper left');
figure.set_size_inches(6, 2);
# %%
## line graphs ##
brent = pd.read_csv('BrentOilPrices.csv')
print(brent.head(3))
brent.plot(color='purple');
tech = pd.read_csv('tech_giants.csv', index_col=0, parse_dates=True)
fb = tech.loc[tech.name=='FB', 'close'].rename('Facebook')
msft = tech.loc[tech.name=='MSFT', 'close'].rename('Microsoft')
aapl = tech.loc[tech.name=='AAPL', 'close'].rename('Apple')
dfs = pd.concat([fb, msft, aapl], axis=1)
#print(dfs.head(3))
dfs.plot();
dfs.plot(subplots=True, figsize=(13, 6));
# %%
## bar charts ##
boston = pd.read_csv('2017BostonMarathonTop1000.csv')
print(boston.head())

# %%
# marathon runners by age (age - category - numerical value)
#boston.Age.value_counts().plot(kind='bar', figsize=(12,6));
ax = boston.Age.value_counts(sort=False).plot(kind='bar', figsize=(12,6)) # <Axes: >
ax.set_xlabel('Age Group');
ax.set_ylabel('# of runners');
 # %%
ax = boston.Age.value_counts(sort=False).plot(kind='barh', figsize=(12,6)) # <Axes: >
ax.set_xlabel('Age Group');
ax.set_ylabel('# of runners');
# %%
# marathon runners by gender?
boston['M/F'].value_counts(normalize=True).plot(kind='barh');
# %%
## pie plots ##
games = pd.read_csv('games_sales.csv')
# what is the market share for each platform in NA?
games.groupby('Platform').NA_Sales.sum().plot(kind='pie');
# %%
# does PS have a larger market share in JP?
games.loc[:, ['NA_Sales', 'JP_Sales', 'Platform']].groupby('Platform').sum().plot(kind='pie', subplots=True);
# %%
## histograms ##
drinks = pd.read_csv('drinks.csv')
drinks.beer_servings.plot(kind='hist');  
# %%
ax = drinks.beer_servings.plot(kind='hist');
ax.set_xlabel('Beer Servings');
# %%
ax = drinks.beer_servings.plot(kind='hist', bins=15);
ax.set_xlabel('Beer Servings');
# %%
ax = drinks.beer_servings.plot(kind='hist', bins=5, orientation='horizontal');
ax.set_xlabel('Beer Servings');
# %%
drinks.loc[:,'beer_servings':'wine_servings'].plot(kind='hist');
# %%
drinks.loc[:,'beer_servings':'wine_servings'].plot(kind='hist', alpha=0.6);
# %%
drinks.loc[:,'beer_servings':'wine_servings'].plot(kind='hist', subplots=True, alpha=0.6);
# %%
## scatter plots ##
# show the relationship between two numeric values
sat = pd.read_csv('scores.csv')
# is reading and writing more strongly associated than writing and math?
math = sat.loc[sat['SAT Section']=='Math'].Score.reset_index(drop=True)
writing = sat.loc[sat['SAT Section']=='Writing'].Score.reset_index(drop=True)
reading = sat.loc[sat['SAT Section']=='Reading'].Score.reset_index(drop=True)
scores = pd.concat([math, writing, reading], axis=1)
scores.columns = ['Math','Writing', 'Reading']
scores.plot(kind='scatter', x='Math', y='Writing');
# %%
#math.corr(writing) # 0.9341552744743178
scores.plot(kind='scatter', x='Reading', y='Writing');
reading.corr(writing) # 0.9854389581058105
# %%
