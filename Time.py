__author__ = 'Pneumatic'
import time  # need to import time to use it !!NOT BUILT IN!!
import calendar  # need to import calendar to use it !!NOT BUILT IN!!
print(time.time())  # returns the current system time in ticks since 12:00am, January 1, 1970, 1 tick = 1 second
localtime = time.asctime(time.localtime(time.time()))
t = (2013, 12, 8, 6, 0, 33, 6, 342, 0)
# create variable localtime using the time.localtime function on the ticks format it using time.asctime()
print(localtime)  # prints out the time can be reformatted
cal = calendar.month(2013, 12)  # create a new calender called cal set it for the year 2013, month 12 (december)
print(cal)  # print out the calendar we created, it is already formatted
offset = time.altzone  # sets variable offset to local time in seconds behind utc. !ONLY USE IF DAYLIGHT IS NONZERO!
offset1 = offset/3600  # perform math on offset divide it by 3600(60 seconds * 60 minutes) to get the hours
print(offset1)  # print the offset from utc users localtime is
time.ctime()  # converts a time expressed in seconds since the 1/1/1970 to a string representing local time
time.gmtime()  # converts a time expressed in seconds since the epoch to a struct_time in UTC
# struct_time(tm_year=, tm_mon=, tm_mday=, tm_hour=, tm_min=, tm_sec=, tm_wday=, tm_yday=, tm_isdst=)
time.localtime()  # similar to gmtime() but it converts number of seconds to local time
time.mktime(t)  # converts the arguments in the () to seconds since 1/1/1970
time.sleep(1)  # suspends execution of next command by number of seconds specified in the ()
# converts tuple or struct_time representing a time returned by gmtime(), localtime() as string specified by format args
time.strftime("%b %d %Y %H:%M:%S", time.gmtime())  # %b=abbr. month, %d=day of month, %Y=year, %H:%M:%S= hours:min:secs
# parses a string representing time in a format. The return value is a struct_time as returned by gmtime(), localtime()
structure_time = time.strptime("30 Nov 00", "%d %b %y")  # format is (time, formatting)
time.tzname  # returns the name of the local timezone (est or edt)
calendar.firstweekday()  # returns the setting for first day of week default it is monday, use setfirstweekday to change
calendar.calendar(2013, w=2, l=1, c=6)  # Returns a multiline string with a calendar for year specified
# w = width in characters of each date, l = number of lines for each week, c = number of spaces between columns
calendar.isleap(2013)  # returns true if year specified is a leap year else returns false
calendar.leapdays(2000, 2013)  # Returns the total number of leap days in the years within range(y1,y2)
calendar.month(2013, 1, w=2, l=1)  # Returns a multiline string with a calendar for year/month specified
calendar.monthcalendar(2013, 1)  # returns a list of days in each week for the month specified in the year
calendar.monthrange(2013, 1)  # returns first day (0 is monday - 6 is sunday) of the month and number of days in month
calendar.prcal(2013, w=2, l=1, c=6)  # like print calendar.calendar(year, w, l, c)
calendar.prmonth(2013, 1, w=2, l=1)  # like print calendar.month(year, month, w, l)
# calendar.timegm(tupletime) accepts a time instant in time-tuple form and returns the same instant as number of seconds
calendar.weekday(2013, 1, 21)  # Returns the weekday code for the given date (monday)
