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
