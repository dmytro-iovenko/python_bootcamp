import pandas as pd
import numpy as np
from datetime import date, time, datetime
from dateutil import parser

### Handling Date and Time ###
## datetime module ##
# year - month - day
date_A = date(2020, 4, 25)
# the time class - hour - minute - second - microsecond
time_A = time(4, 30, 12, 943212)
time_A.isoformat() # 04:30:12.943212
# the datetime class
dt_A = datetime(2020, 4, 25, 19, 1, 23, 123123)
datetime.now() # 2023-08-18 14:01:08.680767
## parsing dates from text ##
# what if we don't have date objects?
# datetime -> strptime (string parse time)
dt_B = datetime.strptime('2019-10-31', '%Y-%m-%d') # 2019-10-31 00:00:00 # '%Y-%m-%d' - Format Codes
dt_B.year # 2019
try_this = "jan 20 2090 4pm"
datetime.strptime(try_this, '%b %d %Y %I%p')
# best way: use dateutil
parser.parse('Jan 21st 1990') # 1990-01-21 00:00:00
## from datetime to string ##
# strftime (string format time)
dt = datetime.now()
dt.strftime('%Y') # 2023
dt.strftime('Year: %Y; Month: %m; Day: %d;') # Year: 2023; Month: 08; Day: 21;
'My date is {:%c}'.format(dt) # My date is Mon Aug 21 08:59:23 2023
## performant datetimes with numpy ##
a = np.datetime64('2023-07-21') 
b = np.datetime64(datetime.now())
a + 10 # 2023-07-31
## the pandas timestamp ##
# pandas timestamp = python datetime + numpy datetime64
pdts = pd.Timestamp('4th of July 1776') # 1776-07-04 00:00:00
pdts.day_name() #Thursday
pdts.days_in_month # 31
pdts.quarter # 3
pdts.isocalendar() # (year=1776, week=27, weekday=4)
## adding new data ##
brent = pd.read_csv('BrentOilPrices.csv')
brent.Date = brent.Date.astype(np.datetime64) # convert date from string to numpy object
#brent.dtypes
# Date     datetime64[ns]
#Price           float64
#dtype: object
brent.set_index('Date', inplace=True) # get DatetimeIndex 
brent2 = pd.read_csv('BrentOilPrices.csv', index_col=0, parse_dates=True) # for good data quality
# indexing dates by label
# Q: select brent price on Jan 3rd 2017
brent.loc['2017-01-03'] # 55.05
# Q: select brent price from Jan 3rd to Jan 6th 2017
brent.loc['2017-01-03':'2017-01-06']
# Q: select all prices from Jan 2019 - partial string indexing
brent.loc['2019-01']
# Q: select prices from the first two month of 2019
brent.loc['2019-01':'2019-02']

# Skill Challenge 15 - selecting dates
# 1) using the brent time series, create a shorter dataframe that only contains the dates from 1 December 2015 to 31 March 2016
brent.loc['2015-12-01':'2016-03-31'] # 84 rows
# 2) repeat the above, but this time using partial string indexing instead of specifying full dates
df = brent.loc['2015-12':'2016-03'] # 84 rows
# what was the standart deviation of prices during this period?
df_std = brent.Price.std() # 3.9901226782366077
# 3) was the mean price from February 2018 greater or less than the median price from March 2017?
brent.loc['2018-02'].mean() # 65.3175
brent.loc['2017-03'].median() # 50.65
brent.loc['2018-02'].mean() > brent.loc['2017-03'].median() # True

## shifting dates with pd.DateOffset() ##
dob = pd.Timestamp('2020-03-09') # racing pigeon
# Q; when was the egg laid? (need to -18 days)
pd.DateOffset(days=18) # create an object for 18 days
dob - pd.DateOffset(days=18) # 2020-02-20 00:00:00
# DateOffset supports many temporal params
pd.DateOffset(days=4, minutes=10, nanoseconds=2)
pd.DateOffset(year=10)
# reflect closing time 6 PM for each day
brent.set_index(brent.index + pd.DateOffset(hours=18))
# 2019-09-26 18:00:00  62.08
# 2019-09-27 18:00:00  62.48
# 2019-09-30 18:00:00  60.99
## the TimeDelta class ##
pd.Timedelta(days=3, hours=4)
ts = brent.iloc[0].name # 2000-01-04 00:00:00
ts + pd.Timedelta(days=3, hours=4) # 2000-01-07 04:00:00
ts + pd.DateOffset(days=3, hours=4) # 2000-01-07 04:00:00
# key differ: the Timedelta operates on absolute time (day = 24 hours), when DateOffset operates on calendar time
# DateOffset is "calendar aware": takes into consideration thongs like daylight saving time DST (day could be 23-25 hours)
dst = pd.Timestamp('14 march 2021', tz='US/Eastern') # 2021-03-14 00:00:00-05:00
dst + pd.DateOffset(days=1) # 2021-03-15 00:00:00-04:00 only 23 hours added
dst + pd.Timedelta(days=1) # 2021-03-15 01:00:00-04:00 added 24 hours



