# coding=utf-8
import time
from datetime import datetime

def datetime_to_epoch(d):
    return int(time.mktime(d.timetuple()))


def epoch_to_datetime(epoch):
    return datetime(*time.localtime(epoch)[:6])


now = datetime.now()
# => 2012-10-10 21:12:17.544219

epoch = datetime_to_epoch(now)
print(epoch)
# =>  1349871137

print(epoch_to_datetime(epoch))
# => 2012-10-10 21:12:17
