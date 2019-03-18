import os
import csv

report_list = []
tvc = 0  # Total votes counted
title = "Election Results"
line = "-------------------------"
win = ""
max = 0



# Set path for file
csvpath = os.path.join("Hw3-Resources", "election_data.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # loop through entire election datafile
    for row in csvreader:
        # No matter the header
        if row[2] == "Candidate":
            continue 
        valor = row[2] 
        exist_in_csv = False
        for i in range(len(report_list)):
            if valor in report_list[i]:
                exist_in_csv = True
                report_list[i][1] = report_list[i][1] + 1
                break
            
        if not exist_in_csv:
            report_list.append([valor, 1])

# printing report

# # We create file for writing
f = open("pyPollResults.txt","w")


for l in report_list:
    tvc = tvc + l[1]    
msg1 = "Total Votes: " + str(tvc)
print(title)
print(line)
print(msg1)
print(line)

f.write(title + "\n")
f.write(line + "\n")
f.write(msg1+"\n")
f.write(line + "\n")

for l in report_list:
    msg2 = "{0}: {1:5.2f}% ({2})".format( l[0], (l[1]/tvc)*100 , l[1] )    
    print( msg2 )
    f.write(msg2+"\n")
    if (max < l[1]):
        max = l[1]
        win = l[0]
print(line)
win = "Winner: " + win
print(win) 
print(line)

f.write(line+ "\n")
f.write(win+ "\n")
f.write(line+ "\n")
f.close()