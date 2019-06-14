points = 174  # use this as input for your submission
prize = None
# establish the default prize value to None


# use the points value to assign prizes to the correct prize names


# use the truth value of prize to assign result to the correct prize

if points <= 50:
    prize = 'wooden rabbit'
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    prize = 'wooden rabbit'
else:
    prize = 'wooden rabbit'

if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."
print(result)