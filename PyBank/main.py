import os
import csv

# List of budget data
budgetList = ["1", "2"]

# Loop through budget datas
for budgetData in budgetList:

    # Grab raw budget data
    budgetCSV = os.path.join('raw_data','budget_data_' + budgetData + ".csv")

    # Create new output CSV
    outputCSV = os.path.join('output','output_' + budgetData + ".csv")

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
        # Skip header
        next(csvReader, None)
        for row in csvReader:
            totalMonths = totalMonths + 1
            totalRevenue = totalRevenue + int(row[1])
            # exclude 1st month for revenue change
            if (totalMonths == 1):
                previousMonthRevenue = int(row[1])
            else:
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
        print("Average Revenue Change: $" + str(int(averageRevenueChange/(totalMonths-1))))
        print("Greatest Increase in Revenue: " + greatestIncreaseDate + " ($" + str(greatestIncreaseAmount) + ")")
        print("Greatest Decrease in Revenue: " + greatestDecreaseDate + " ($" + str(greatestDecreaseAmount) + ")")
        print(" ")
        print(" ")

    # Write analysis into new CSV file
    with open(outputCSV, 'w', newline="") as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=' ')
        csvWriter.writerow(["Financial Analysis"])
        csvWriter.writerow(["-----------------------------"])
        csvWriter.writerow(["Total Months:  "+ str(totalMonths)])
        csvWriter.writerow(["Total Revenue: $" + str(totalRevenue)])
        csvWriter.writerow(["Average Revenue Change: $" + str(int(averageRevenueChange/(totalMonths-1)))])
        csvWriter.writerow(["Greatest Increase in Revenue: " + greatestIncreaseDate + " ($" + str(greatestIncreaseAmount) + ")"])
        csvWriter.writerow(["Greatest Decrease in Revenue: " + greatestDecreaseDate + " ($" + str(greatestDecreaseAmount) + ")"])
          


        
        


        
                
            
            
