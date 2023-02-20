#1
from datetime import datetime, timedelta
today = datetime.now().replace(microsecond=0)
day = timedelta(1)
time = today - day
dif = today - time
print(dif.total_seconds())

#2
import datetime
date1 = datetime.datetime(2022, 2, 1, 12, 0, 0)
date2 = datetime.datetime(2022, 2, 1, 12, 0, 15)
differ = (date2 - date1).total_seconds()
print(differ)