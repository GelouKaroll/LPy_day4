from datetime import datetime, timedelta
#<<<<<<<<<<<<<<<< как использовать синтаксис 'as' при импорте нескольких модулей?

sep = '_____________________'

msg = 'Yesterday'
date = datetime.now() - timedelta(days=1)

print(msg + '\n' + date.strftime('%Y-%m-%d') + '\n' + sep)

msg = 'Today'
date = datetime.now()
print(msg + '\n' + date.strftime('%Y-%m-%d') + '\n' + sep)

msg = '30 days ago'
date = datetime.now() - timedelta(days=30)

print(msg + '\n' + date.strftime('%Y-%m-%d') + '\n' + sep)

datestr = '01/01/25 12:10:03.234567'
date = datetime.strptime(datestr, '%d/%m/%y %H:%M:%S.%f')

print(date, type(date))
print(sep)