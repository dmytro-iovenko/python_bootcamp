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
