import os
import csv

# List of budget data
budgetList = ["1", "2"]

# Loop through budget datas
for budgetData in budgetList:

    # Grab raw budget data
    budgetCSV = os.path.join('raw_data','budget_data_' + budgetData + ".csv")

    # Create new output txt file
    outputTXT = os.path.join('output','output_' + budgetData + ".txt")

    # Open current budget data CSV
    with open(budgetCSV, 'r', encoding = 'utf-8') as csvFile:
        csvReader = csv.reader(csvFile, delimiter = ',')
        # Set initial variables
        totalMonths = 0
        totalRevenue = 0
        averageRevenueChange = 0
        greatestIncreaseDate = ""
        greatestIncreaseAmount = 0
        greatestDecreaseDate = ""
        greatestDecreaseAmount = 0
        previousMonthRevenue = 0
        # Skip header
        next(csvReader, None)
        for row in csvReader:
            totalMonths = totalMonths + 1
            totalRevenue = totalRevenue + int(row[1])
            # exclude 1st month for revenue change
            # if (totalMonths == 1):
            #     previousMonthRevenue = int(row[1])
            # else:
            revenueChange = int(row[1]) - int(previousMonthRevenue)
            averageRevenueChange = averageRevenueChange + revenueChange
            if (revenueChange >= 0 and revenueChange > greatestIncreaseAmount):
                greatestIncreaseAmount = revenueChange
                greatestIncreaseDate = row[0]
            elif (revenueChange < 0 and revenueChange < greatestDecreaseAmount):
                greatestDecreaseAmount = revenueChange
                greatestDecreaseDate = row[0]
            previousMonthRevenue = row[1]
        print("Financial Analysis")
        print("-----------------------------")
        print("Total Months: " + str(totalMonths))
        print("Total Revenue: $" + str(totalRevenue))
        print("Average Revenue Change: $" + str(int(averageRevenueChange/totalMonths)))
        print("Greatest Increase in Revenue: " + greatestIncreaseDate + " ($" + str(greatestIncreaseAmount) + ")")
        print("Greatest Decrease in Revenue: " + greatestDecreaseDate + " ($" + str(greatestDecreaseAmount) + ")")
        print(" ")
        print(" ")

    # Write analysis into new txt file
    with open(outputTXT, 'w',) as txtFile:
        txtFile.write("Financial Analysis")
        txtFile.write("\n-----------------------------")
        txtFile.write("\nTotal Months:  "+ str(totalMonths))
        txtFile.write("\nTotal Revenue: $" + str(totalRevenue))
        txtFile.write("\nAverage Revenue Change: $" + str(int(averageRevenueChange/totalMonths)))
        txtFile.write("\nGreatest Increase in Revenue: " + greatestIncreaseDate + " ($" + str(greatestIncreaseAmount) + ")")
        txtFile.write("\nGreatest Decrease in Revenue: " + greatestDecreaseDate + " ($" + str(greatestDecreaseAmount) + ")")
          


        
        


        
                
            
            
