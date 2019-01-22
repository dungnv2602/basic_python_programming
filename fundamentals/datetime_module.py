import datetime
import pytz
# naive date time
today = datetime.date.today()

print(today.weekday())
print(today.isoweekday())

tdelta = datetime.timedelta(days=7)

print('1 week ago from now ', (today-tdelta))

dt = datetime.datetime(2016, 7, 26, 12, 45)
tdelta = datetime.timedelta(hours=12)
print(dt + tdelta)

# localized date time
dt = datetime.datetime(2016, 7, 26, 12, 45, tzinfo=pytz.UTC)
print(dt)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)

dt_mtn = datetime.datetime.now()
mtn_zn = pytz.timezone('US/Mountain')

dt_mtn = mtn_zn.localize(dt_mtn)

print(dt_mtn)

# strftime() = convert Datetime to String
# strptime() = convert String to Datetime
dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
print(dt_mtn.strftime('%B %d, %Y'))