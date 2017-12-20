import datetime, time

now = datetime.datetime.now()
print(now.strftime("%d-%m-%Y %H:%M:%S:%f"))
time.sleep(1)
now = datetime.datetime.now()
print(now.strftime("%d-%m-%Y %H:%M:%S:%f"))