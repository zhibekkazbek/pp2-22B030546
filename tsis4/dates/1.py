from datetime import datetime, timedelta
now = datetime.now()
five_days_ago = now - timedelta(days=5)
a = five_days_ago
print(a.strftime("%y-%m-%d"))