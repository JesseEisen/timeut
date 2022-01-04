import datetime
import time 

def convertToMs(timeStr):
    second, ms = timeStr.split(',')
    dt = datetime.datetime.strptime(second, "%Y-%m-%d %H:%M:%S")
    return time.mktime(dt.timetuple()) + (int(ms)/1000.)

a = convertToMs("2021-01-04 18:22:21,78")
b = convertToMs("2021-01-04 18:22:21,919")
print(round(b-a, 4))
