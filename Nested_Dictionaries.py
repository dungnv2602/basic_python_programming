elements = {
    'hydrogen':{
        'number':1,
        'weight': 1.00794,
        'symbol': 'H'
    },
    'helium':{
        'number':2,
        'weight':4.002602,
        'symbol':'He'
    }
}
elium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight

oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # create a new oxygen dictionary 
elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary

print('elements = ', elements)
