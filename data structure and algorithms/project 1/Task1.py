"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
numbers = []
for item in texts:
    numbers.append(item[0])
    numbers.append(item[1])

for item in calls:
    numbers.append(item[0])
    numbers.append(item[1])

numbers_undup = set(numbers)
print("There are %s different telephone numbers in the records." % len(numbers_undup))
