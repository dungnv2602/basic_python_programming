import csv
# common reader writer
# read
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)  # can use  delimiter

    next(csv_reader)  # move cursor to next line; skip first line
    next(csv_reader)  # move cursor to next line; skip second line

    for line in csv_reader:
        print(line)
        print(line[2])

# write
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_name.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')  # \t: tab

        for line in csv_reader:
            csv_writer.writerow(line)

# using dictionary reader and writer
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(
            new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']  # exclude email field
            csv_writer.writerow(line)
