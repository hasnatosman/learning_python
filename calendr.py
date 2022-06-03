# import calendat module

import calendar

# create a plain text calendar

c = calendar.TextCalendar(calendar.SATURDAY)
str = c.formatmonth(2022, 6, 0, 0)
print(str)