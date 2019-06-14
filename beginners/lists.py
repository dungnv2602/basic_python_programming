list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things[0])
print(list_of_random_things[-1])
print(list_of_random_things[-2])

print(list_of_random_things[1:2])

# from start to index
print(list_of_random_things[:3])
# from index to last
print(list_of_random_things[2:])

print(2 not in list_of_random_things, 3.4 in list_of_random_things)

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']


# TODO: Modify this line so it prints the last three elements of the list
eclipse_dates = eclipse_dates[-3:]
print(eclipse_dates)

print(max(eclipse_dates))
print(min(eclipse_dates))

sorted(eclipse_dates, reverse=True)

print(sorted(eclipse_dates))
