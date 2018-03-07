import os
import csv
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# List of employee data
employeeDataList = ["1", "2"]

# Loop through employee datas
for employeeData in employeeDataList:

    # Grab raw employee data
    employeeDataCSV = os.path.join('raw_data','employee_data' + employeeData + ".csv")

    # Create new output CSV
    outputCSV = os.path.join('output','output_' + employeeData + ".csv")

    # Open current employee data CSV
    with open(employeeDataCSV, 'r', encoding = 'utf-8') as csvFile:
        csvReader = csv.reader(csvFile, delimiter = ',')
        # Set initial list
        empID = []
        firstName = []
        lastName = []
        DOB = []
        SSN = []
        state = []
        # Skip header
        next(csvReader, None)
        for row in csvReader:
            empID.append(row[0])
            firstName.append(row[1].split()[0])
            lastName.append(row[1].split()[1])
            DOB.append(row[2].split('-')[1] + "/" + row[2].split('-')[2] + "/" + row[2].split('-')[0])
            SSN.append("***-**-" + row[3].split('-')[2])
            state.append(us_state_abbrev[row[4]])       

    # zip all lists into tuple
    wholeTuple = zip(empID,firstName,lastName,DOB,SSN,state)

    # Export into new CSV file
    with open(outputCSV, 'w', newline="") as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=' ')
        csvWriter.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
        csvWriter.writerows(wholeTuple)

        
        


        
                
            
            
