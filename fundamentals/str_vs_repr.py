import datetime
import pytz

# str - user friendly
# repr - unambiguous
a = datetime.datetime.now(tz=pytz.UTC)
b = str(a)

print('str(a): {}'.format(str(a)))
print('str(b): {}'.format(str(b)))

print

print('repr(a): {}'.format(repr(a)))
print('repr(b): {}'.format(repr(b)))
