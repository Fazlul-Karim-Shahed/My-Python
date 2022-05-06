
import datetime

current = datetime.datetime.now()

anotherCurrent = datetime.date.today()

print(current)
print(anotherCurrent)
print(current.strftime("Date: %Y-%m-%d Time: %H-%M-%S"))