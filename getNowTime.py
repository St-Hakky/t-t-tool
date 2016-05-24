# coding=utf-8

from datetime import datetime

now = datetime.now()

time = {}
for i in range(24) :
    time[str(i).zfill(2)] = 0

for k, v in time.items():
    print (k, '-->', v)

# datetimeオブジェクト
print now.strftime('%Y/%m/%d %H:%M:%S')

print now.strftime('%Y')              #	yyyy 年
print now.strftime('%y')	            #  yy	年(下2桁)
print now.strftime('%m')	#  mm	月
print now.strftime('%d')	#	dd  日
print now.strftime('%H')	#  hh	時 (24時間表記)
print now.strftime('%I')	#  hh	時 (12時間表記)
print now.strftime('%M')	#  mm	分
print now.strftime('%S')	#  ss	秒
print now.strftime('%b')	#  mon	短縮月名 'Jan'
print now.strftime('%B')	#  month	月名 'January'
print now.strftime('%a')	#  短縮曜日名 'Mon'
print now.strftime('%A')	# 	曜日名   'Monday'
print now.strftime('%p')	#  AM or PM
print now.isoformat()	    #  yyyy-mm-ddThh:mm:ss	ISO 8601 形式
print now.ctime()	        #  Thu Jan 2 03:04:05 2014	%a %b %d %X %Y
print now.strftime('%c')	#  Thu Jan 2 03:04:05 2014	%a %b %d %X %Y
print now.strftime('%x')	#  01/02/14	%m/%d/%y
print now.strftime('%X')	# 03:04:05	%H:%M:%S
print now.strftime('%s')	# 1388599445
