points = 174  # use this input to make your submission

# write your if statement here
prize_name = ''
result = "Congratulations! You won a {}!"
if(points <= 200):
    if points >= 1 and points <= 50:
        prize_name = 'wooden rabbit'
        result = result.format(prize_name)
    elif points >= 51 and points <= 150:
        result = "Oh dear, no prize this time."
    elif points >= 151 and points <= 180:
        prize_name = 'wafer-thin mint'
        result = result.format(prize_name)
    elif points >= 181 and points <= 200:
        prize_name = 'penguin'
        result = result.format(prize_name)

print(result)
