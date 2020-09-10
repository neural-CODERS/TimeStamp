import calender
import time
gmt = time.gmtime()
print(" GMT:- ",gmt)
ts = calender.timegm(gmt)
print(" Timestamp:- ",ts)
