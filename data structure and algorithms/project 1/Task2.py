"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

dict = {}
for call in calls:
    user1 = call[0]
    user2 = call[1]
    time = call[3]

    # check user1
    if(dict.get(user1)):
        dict[user1] += int(time)
    else:
        dict[user1] = int(time)

    # check user2, resubmission: change typo
    if (user2 in dict.keys()):
        dict[user2] += int(time)
    else:
        dict[user2] = int(time)
    
max_time = max(list(dict.values()))
max_index = list(dict.values()).index(max_time)
user = list(dict.keys())[max_index]

print("%s spent the longest time, %d seconds, on the phone during September 2016." % (user, max_time))