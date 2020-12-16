import sys
import csv

#  Check for correct cmd line arguments
if len(sys.argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit()


#  Open the database file and save into a list of dicts
database_list = []import sys
import csv

#  Check for correct cmd line arguments
if len(sys.argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit()


#  Open the database file and save into a list of dicts
database_list = []
database = open(sys.argv[1], 'r')
database_file = csv.DictReader(database)
for row in database_file:
    database_list.append(dict(row))


#  Open the sequence file and save into a dict
sequence_file = open(sys.argv[2], 'r')
if sequence_file.mode == 'r':
    sequence = sequence_file.read()
    sequence_len = len(sequence)


#  create a dict to store count of STRs based on the STRs included in the database
DNA_STR = {}
for row in database_list:
    for column in row:
        if column == "name":
            continue
        else:
            DNA_STR[column] = 0
    break


#  Count highest number of repeats for each STR
for key in DNA_STR:
    i = 0
    while i <= len(sequence):
        #  set the start end end markers
        start = i
        end = 0
        while sequence[i: i + len(key)] == key:
            i = i + len(key)
            end = i
        strcount = sequence.count(key, start, end)
        #  compare to value and see if higher
        if strcount > DNA_STR[key]:
            DNA_STR[key] = strcount
        i += 1


#  Compare the DNA to the database and see if there is a match
def dna_check(dna):
    Match = False
    for row in database_list:
        for key, value in DNA_STR.items():
            if int(row[key]) == value:
                Match = True
            else:
                Match = False
                break
        if Match == True:
            return row["name"]

    if Match == False:
        return "No Match"


#  Print the name of the match or declare No Match
print(dna_check(DNA_STR))
database = open(sys.argv[1], 'r')
database_file = csv.DictReader(database)
for row in database_file:
    database_list.append(dict(row))


#  Open the sequence file and save into a dict
sequence_file = open(sys.argv[2], 'r')
if sequence_file.mode == 'r':
    sequence = sequence_file.read()
    sequence_len = len(sequence)


#  create a dict to store count of STRs based on the STRs included in the database
DNA_STR = {}
for row in database_list:
    for column in row:
        if column == "name":
            continue
        else:
            DNA_STR[column] = 0
    break


#  Count highest number of repeats for each STR
for key in DNA_STR:
    for i in range(sequence_len):
        #set the start end end markers
        start = i
        end = 0
        while sequence[i: i + len(key)] == key:
            i = i + len(key)
            end = i
        strcount = sequence.count(key, start, end)
        #compare to value and see if higher
        if strcount > DNA_STR[key]:
            DNA_STR[key] = strcount


#  Compare the DNA to the database and see if there is a match
def dna_check(dna):
    Match = False
    for row in database_list:
        for key, value in DNA_STR.items():
            if int(row[key]) == value:
                Match = True
            else:
                Match = False
                break
        if Match == True:
            return row["name"]

    if Match == False:
        return "No Match"


#  Print the name of the match or declare No Match
print(dna_check(DNA_STR))
