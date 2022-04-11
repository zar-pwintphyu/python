# %%
import pandas as pd
from datetime import date
from pandas.tseries.holiday import *
from pandas.tseries.offsets import CustomBusinessDay

class myCalendar(AbstractHolidayCalendar):
   rules = [
     Holiday("New Years", month=1, day=1),
     Holiday("Union Day", month=2, day=12, observance=nearest_workday),
     Holiday("Peasants' Day", month=3, day=2, observance=nearest_workday),
     Holiday("	Full Moon Day of Tabaung", month=3, day=9, observance=nearest_workday),
     Holiday("Armed Forces' Day", month=3, day=27, observance=nearest_workday),
     Holiday("Maha Thingyan (Water Festival)", month=4, day=10, observance=nearest_workday),
     Holiday("Maha Thingyan (Water Festival)", month=4, day=13, observance=nearest_workday),
     Holiday("Maha Thingyan (Water Festival)", month=4, day=14, observance=nearest_workday),
     Holiday("Maha Thingyan (Water Festival)", month=4, day=15, observance=nearest_workday),
     Holiday("Maha Thingyan (Water Festival)", month=4, day=16, observance=nearest_workday),
     Holiday("Maha Thingyan (Water Festival)", month=4, day=17, observance=nearest_workday),
     Holiday("Labor Day / May Day", month=5, day=1, observance=nearest_workday),
     Holiday("Full Moon Day of Kasong", month=5, day=6, observance=nearest_workday),
     Holiday("	Martyrs' Day", month=7, day=20, observance=nearest_workday),
     Holiday("Full Moon Day of Waso (Beginning of Buddhist Lent)", month=8, day=3, observance=nearest_workday),
     Holiday("	Full Moon Day of Thadingyut (End of Buddhist Lent)", month=10, day=29, observance=nearest_workday),
     Holiday("	Full Moon Day of Thadingyut (End of Buddhist Lent)", month=10, day=30, observance=nearest_workday),
     Holiday("	Full Moon Day of Thadingyut (End of Buddhist Lent)", month=11, day=2, observance=nearest_workday),
     Holiday("Full Moon Day of Tazaungmone Holiday", month=11, day=27, observance=nearest_workday),
     Holiday("Full Moon Day of Tazaungmone Holiday", month=11, day=30, observance=nearest_workday),
     Holiday("National Day", month=12, day=9, observance=nearest_workday),
     Holiday("Christmas Day", month=12, day=25, observance=nearest_workday),
     Holiday("New Year Holiday", month=12, day=31, observance=nearest_workday),

   ]
# mm-workingday #
#using CustomBusinessDay
cal = CustomBusinessDay(calendar=myCalendar())
#start to end frequency with calling custombusinessday
s = pd.date_range('2020-01-01', '2020-12-31' , freq=cal)
#date format 
smm=s.strftime('%Y-%m-%d')
#extra date (saturday and sunday )

#Calling DataFrame constructor on s
df = pd.DataFrame(smm,columns=['mm'])

#Calling DataFrame constructor on s1

#concatenating df and df1 on  Dataframe
#data= pd.concat([df], ignore_index=True)


# converting to list 
mmdata = {'mm-workingday' : df["mm"].tolist()}
def mm():
  return mmdata

# mm-holiday #
# converting to list 
mmh=df["mm"].tolist()

#start to end frequency
s = pd.date_range(start='2020-01-01',end='2020-12-31' )
#date format
Allday=s.strftime('%Y-%m-%d')
#Calling Dataframe constructor on Allday
df = pd.DataFrame(Allday, columns=['mm'])
#converting to list
Calendar=df["mm"].tolist()


#python for loop and if condition
holiday={'mm-holiday':[date for date in Calendar if not date in mmh]}
mmholiday = pd.DataFrame(holiday)
def mmhol():
    return holiday





