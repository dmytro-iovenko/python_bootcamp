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
