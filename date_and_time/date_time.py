import calendar
import datetime
import time

ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:", ticks

localtime = time.localtime(time.time())
print "Local current time :", localtime

print "Local current formatted time: ", time.asctime(localtime)

calendar_ = calendar.month(1990, 7)
print "Here is the calendar:"
print calendar_

today_ = datetime.datetime.now()
print "Today is: ", today_

now_ = datetime.datetime.time(datetime.datetime.now())
print "Now is: ", now_

now_ = datetime.datetime.now()

print "Current year: %d" % now_.year
print "Current month: %d" % now_.month
print "Current day: %d" % now_.day
print "Current hour: %d" % now_.hour
print "Current minute: %d" % now_.minute
print "Current second: %d" % now_.second
print "Current microsecond: %d" % now_.microsecond

print "Current date and time using strftime:"
print now_.strftime("%Y-%m-%d %H:%M")

day_in_10_days = now_ + datetime.timedelta(days=10)
print "In 10 days from today will be: ", day_in_10_days

day_in_50_days = now_ + datetime.timedelta(days=50)
print "In 50 days from today will be: ", day_in_50_days
