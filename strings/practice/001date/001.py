from datetime import datetime , timedelta

today = datetime.now()
oneday = timedelta(days=1)

yesterday = today - oneday
print("today is :" + str (today))
print("yesterday was : " + str(yesterday))

birthday = input ("enter you birthday ")

birthdaydate = datetime.strptime(birthday , "%d/%m/%Y")

print("birthday :" + str(birthdaydate))