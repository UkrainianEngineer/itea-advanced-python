import calendar
import time

ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:", ticks

localtime = time.localtime(time.time())
print "Local current time :", localtime

print "Local current formatted time: ", time.asctime(localtime)

calendar_ = calendar.month(1990, 7)
print "Here is the calendar:"
print calendar_
