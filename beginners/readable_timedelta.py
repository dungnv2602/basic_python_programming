# write your function here
def readable_timedelta(days=0):
        string = '{} week(s) and {} day(s).'
        weeks = 0
          if days > 7:
            modulo = days % 7
            weeks = days/7
            if modulo != 0:
                days = modulo

    return string.format(weeks,days)
# test your function
print(readable_timedelta(10))                
