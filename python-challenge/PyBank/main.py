import os
import csv

report_dict = {"total months":0, "total profit":0, "average change":0, "max":["Jan-2000", 0], "min":["Jan-2000", 0]}
tm = 0
tp = 0
sum_changes = 0
last_value = 0

# Set path for file
csvpath = os.path.join("Hw3-Resources", "budget_data.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # loop through entire budget_data file
    for row in csvreader:
        if row[0] != "Date":
            tm = tm + 1
            tp = tp + int(row[1])
            if tm == 1:
                report_dict["max"][0] = row[0]
                report_dict["max"][1] = row[1]
                report_dict["min"][0] = row[0]
                report_dict["min"][1] = row[1]
                last_value = int(row[1])
            else:
                if (int(report_dict["max"][1]) < int(row[1]) ):
                    report_dict["max"][0] = row[0]
                    report_dict["max"][1] = row[1]
                
                if (int(report_dict["min"][1]) > int(row[1]) ):
                    report_dict["min"][0] = row[0]
                    report_dict["min"][1] = row[1]
                
                sum_changes = sum_changes + (int(row[1])-last_value)
                last_value = int(row[1])
        
    report_dict["total months"] = tm
    report_dict["total profit"] = tp 
                

    
# printing report
print("Financial Analysis")
print("----------------------------")
msg1 = "Total Months: " + str(report_dict["total months"])
msg2 = "Total: $" + str(report_dict["total profit"])
msg3 = "Average  Change: ${0:.2f}".format(sum_changes / (int(report_dict["total months"])-1) )
msg4 = "Greatest Increase in Profits: {0} : {1}".format(report_dict["max"][0], report_dict["max"][1])
msg5 = "Greatest Decrease in Profits: {0} : {1}".format(report_dict["min"][0], report_dict["min"][1])
print(msg1)
print(msg2)
print(msg3)
print(msg4)
print(msg5)

# We create file for writing
f = open("pyBankResults.txt","w")
f.write("Financial Analysis\n")
f.write("----------------------------\n")
f.write(msg1+"\n")
f.write(msg2+"\n")
f.write(msg3+"\n")
f.write(msg4+"\n")
f.write(msg5+"\n")
f.close()


