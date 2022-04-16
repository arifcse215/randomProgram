md = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print('Enter Date of Birth\n')
dob = {}
dob['year'] = int(input("Year: "))
dob['month'] = int(input("Month: "))
dob['day'] = int(input("Day: "))

print(dob)

print(dob['day'])

print("Enter Present Date\n")
present = {}
present['year'] = int(input("Year: "))
present['month'] = int(input("Month: "))
present['day'] = int(input("Day: "))

if present['day'] < dob['day']:
    i = present['month'] - 1
    day = (present['month']+present['day']) - dob['day']
    present['month'] -= 1
else:
    day = present['day'] - dob['day']

if present['month'] < dob['month']:
    month = present['month'] + 12 - dob['month']
    present['year'] -= 1
else:
    month = present['month'] - dob['month']

year = present['year'] - dob['year']

print("You are ", year, " years", month, "months", day, "days old.")