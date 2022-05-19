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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
caller = []
dict = {} # contain all non-target numbers

for call in calls:
    caller.append(call[0])
    if(not dict.get(call[1])):
        dict[call[1]] = 1

for text in texts:
    if(not dict.get(text[0])):
        dict[text[0]] = 1
    if(not dict.get(text[1])):
        dict[text[1]] = 1

# remove duplicated caller
caller = list(set(caller))

# # remove non_targeted numbers in caller
# for number in caller:
#     if (dict.get(number)):
#         caller.remove(number)

# resubmission: should not modify list while accessing it
telemarketer = []
for number in caller:
    if(not dict.get(number)):
        telemarketer.append(number)

telemarketer.sort()
print("These numbers could be telemarketers: ")
for number in telemarketer:
    print(number)


