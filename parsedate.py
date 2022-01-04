import datetime
import time 

def convertToMs(timeStr):
    second, ms = timeStr.split(',')
    dt = datetime.datetime.strptime(second, "%Y-%m-%d %H:%M:%S")
    return time.mktime(dt.timetuple()) + (int(ms)/1000.)

def convertToMs2(timeStr):
    dt = datetime.datetime.strptime(timeStr, "%Y-%m-%d %H:%M:%S,%f")
    epoch = datetime.datetime.fromtimestamp(0)
    return (dt-epoch).total_seconds()


a = convertToMs("2021-01-04 18:22:21,78")
b = convertToMs("2021-01-04 18:22:21,919")
diff1 = b-a

a = convertToMs2("2021-01-04 18:22:21,078")
b = convertToMs2("2021-01-04 18:22:21,919")
diff2 = b-a
print(f"{diff1:^15.3f}\n{diff2:^15.3f}")
