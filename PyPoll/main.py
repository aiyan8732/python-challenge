import os
import csv
import operator

# List of election data
electionDataList = ["1", "2"]

# Loop through election datas
for electionData in electionDataList:

    # Grab raw election data
    electionDataCSV = os.path.join('raw_data','election_data_' + electionData + ".csv")

    # Create new output CSV
    outputCSV = os.path.join('output','output_' + electionData + ".csv")

    # Open current election data CSV
    with open(electionDataCSV, 'r', encoding = 'utf-8') as csvFile:
        csvReader = csv.reader(csvFile, delimiter = ',')
        # Set initial variables
        totalVotes = 0
        candidatesList = {}
      
        # Skip header
        next(csvReader, None)
        for row in csvReader:
            totalVotes = totalVotes + 1
            if row[2] in candidatesList.keys():
                candidatesList[row[2]] = candidatesList[row[2]] + 1
            else:
                candidatesList[row[2]] = 1
               
        print("Election Results")
        print("-----------------------------")
        print("Total Votes: " + str(totalVotes))
        print("-----------------------------")
        for key,value in candidatesList.items():
            print(key + ": " + str(round(value/totalVotes*100,1)) + "% (" + str(value) + ")")        
        print("-----------------------------")
        print("Winner: " + max(candidatesList.items(), key=operator.itemgetter(1))[0])
        print("-----------------------------")
        print(" ")
        print(" ")

    # Write analysis into new CSV file
    with open(outputCSV, 'w', newline="") as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=' ')
        csvWriter.writerow(["Election Results"])
        csvWriter.writerow(["-----------------------------"])
        csvWriter.writerow(["Total Votes: " + str(totalVotes)])
        csvWriter.writerow(["-----------------------------"])
        for key,value in candidatesList.items():
            csvWriter.writerow([key + ": " + str(round(value/totalVotes*100,1)) + "% (" + str(value) + ")"])        
        csvWriter.writerow(["-----------------------------"])
        csvWriter.writerow(["Winner: " + max(candidatesList.items(), key=operator.itemgetter(1))[0]])
        csvWriter.writerow(["-----------------------------"])
            

        
        


        
                
            
            
