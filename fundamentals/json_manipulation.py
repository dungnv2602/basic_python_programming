import json

with open('states.json') as f:
    data = json.load(f)

# read data
for state in data['states']:
    print(state['name'], state['abbreviation'])

# write data to another json
for state in data['states']:
    del state['area_codes']

with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)  # pretty print with indent=2

# If you want to dump the JSON into a file/socket or whatever, then you should go for dump()
# If you only need it as a string (for printing, parsing or whatever) then use dumps() (dump string)
