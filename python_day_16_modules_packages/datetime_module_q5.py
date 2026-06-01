from datetime import datetime

now = datetime.now()

print('Current Date:',now.date())
print('Current Time:',now.time())
print('Current Year:',now.year)
print('Current Month:',now.month)
print('Current Weekday:',now.strftime('%A'))
