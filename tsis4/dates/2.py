from datetime import datetime, timedelta
today = datetime.now()
day = timedelta(1)
print((today - day).strftime("%d-%m-%y"))
print(today.strftime("%d-%m-%y"))
print((today + day).strftime("%d-%m-%y"))