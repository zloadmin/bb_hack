import win32api
import datetime
st = win32api.GetSystemTime()
print(st)
dt_obj = datetime.datetime(st[0], st[1], st[3], st[4], st[5], st[6])
print(dt_obj)
dt_obj += datetime.timedelta(days=1)
print(dt_obj)
dt_obj_t = dt_obj.timetuple()
dayOfWeek = dt_obj.isocalendar()[2]
print(dt_obj_t)
print(dt_obj_t[0], dt_obj_t[1], dayOfWeek, dt_obj_t[2], dt_obj_t[3], dt_obj_t[4], dt_obj_t[5], dt_obj_t[6])
win32api.SetSystemTime(dt_obj_t[0], dt_obj_t[1], dayOfWeek, dt_obj_t[2], dt_obj_t[3], dt_obj_t[4], dt_obj_t[5], dt_obj_t[6])
#win32api.SetSystemTime(dt_obj_t)
#print(st)
#print(dt_obj)
#end = datetime.timedelta(days=1)

#print(dt_obj)
#systime = systime + 1000
#print(year)
#win32api.SetSystemTime(1970, 1, 1, 1, 1, 1, 1, 1)
#now = datetime.datetime.now()
