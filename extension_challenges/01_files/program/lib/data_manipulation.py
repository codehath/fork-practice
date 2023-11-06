import os
import csv
# == INSTRUCTIONS ==
#
# Below, you'll find lots of incomplete functions.
#
# Your job: Implement each function so that it does its job effectively.
#
# Tips:
# * Use the material, Python Docs and Google as much as you want
#
# * A warning: the data you are using may not contain quite what you expect;
#   cleaning data (or changing your program) might be necessary to cope with
#   "imperfect" data

# == EXERCISES ==

# Purpose: return a boolean, False if the file doesn't exist, True if it does
# Example:
#   Call:    does_file_exist("nonsense")
#   Returns: False
#   Call:    does_file_exist("AirQuality.csv")
#   Returns: True
# Notes:
# * Use the already imported "os" module to check whether a given filename exists
def does_file_exist(filename):
    path = f"/Users/farhath/desktop/projects/python_foundations/extension_challenges/01_files/program/{filename}"
    if os.path.exists(path):
        return True
    return False

# Purpose: get the contents of a given file and return them; if the file cannot be
# found, return a nice error message instead
# Example:
#   Call: get_file_contents("AirQuality.csv")
#   Returns:
#     Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);[...]
#     10/03/2004;18.00.00;2,6;1360;150;11,9;1046;166;1056;113;1692;1268;[...]
#     [...]
#   Call: get_file_contents("nonsense")
#   Returns: "This file cannot be found!"
# Notes:
# * Learn how to open file as read-only
# * Learn how to close files you have opened
# * Use readlines() to read the contents
# * Use should use does_file_exist()
def get_file_contents(filename):
    if does_file_exist(filename):
        path = f"/Users/farhath/desktop/projects/python_foundations/extension_challenges/01_files/program/{filename}"
        with open(path, 'r') as file:
            fileContents = [line.strip() for line in file]
            return(fileContents)
    return("This file cannot be found!")

# Purpose: fetch Christmas Day (25th December) air quality data rows, and if
# boolean argument "include_header_row" is True, return the first header row
# from the filename as well (if it is False, omit that row)
# Example:
#   Call: christmas_day_air_quality("AirQuality.csv", True)
#   Returns:
#     Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);[...]
#     25/12/2004;00.00.00;5,9;1505;-200;15,6;1168;567;525;169;1447;[...]
#     [...]
#   Call: christmas_day_air_quality("AirQuality.csv", False)
#   Returns:
#     25/12/2004;00.00.00;5,9;1505;-200;15,6;1168;567;525;169;1447;[...]
#     [...]
# Notes:
# * should use get_file_contents() - N.B. as should any subsequent
# functions you write, using anything previously built if and where necessary
def christmas_day_air_quality(filename, include_header_row):
    data = get_file_contents(filename)
    christmasData = []

    # Could be a list comprehension
    for row in data:
        if row[:5] == "25/12":
            christmasData.append(row)
    
    if include_header_row:
        header = data[0]
        christmasData.insert(0, header)
    
    return christmasData

# Purpose: fetch Christmas Day average of "PT08.S1(CO)" values to 2 decimal places
# Example:
#   Call: christmas_day_average_air_quality("AirQuality.csv")
#   Returns: 1439.21
# Data sample:
# Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);NOx(GT);PT08.S3(NOx);NO2(GT);PT08.S4(NO2);PT08.S5(O3);T;RH;AH;;
# 10/03/2004;18.00.00;2,6;1360;150;11,9;1046;166;1056;113;1692;1268;13,6;48,9;0,7578;;
def christmas_day_average_air_quality(filename):
    christmasData = christmas_day_air_quality(filename, False)
    data = []
    readings = []
    for row in christmasData:
        data.append(row.split(';'))
    #print(data)
    
    for row in data:
        readings.append(int(row[3]))
    print(readings)

    average = sum(readings)/len(readings)
    return float("{:.2f}".format(average))


# Purpose: scrape all the data and calculate average values for each of the 12 months
#          for the "PT08.S1(CO)" values, returning a dictionary of keys as integer
#          representations of months and values as the averages (to 2 decimal places)
# Example:
#   Call: get_averages_for_month("AirQuality.csv")
#   Returns: {1: 1003.47, [...], 12: 948.71}
# Notes:
# * Data from months across multiple years should all be averaged together
def get_averages_for_month(filename):
    data = get_file_contents(filename)[1:]
    separatedData = []
    PT08Vals = {key: [] for key in range(1, 13)}
    for row in data:
        separatedData = row.split(';')
        # print(separatedData[0][3:5])
        if separatedData[0] != "":
            key = int(separatedData[0][3:5])
            PT08Vals[key].append(int(separatedData[3]))
    return {key: float("{:.2f}".format(sum(value)/len(value))) for (key, value) in PT08Vals.items()}


# Purpose: write only the rows relating to March (any year) to a new file, in the same
# location as the original, including the header row of labels
# Example
#   Call: create_march_data("AirQuality.csv")
#   Returns: nothing, but writes header + March data to file called
#            "AirQualityMarch.csv" in same directory as "AirQuality.csv"
def create_march_data(filename):
    # Get all Rows
    data = get_file_contents(filename)
    header = data[0]
    data = data[1:]
    marchData = []
    # Insolate March Rows
    for row in data:
        if row[3:5] == "03":
            marchData.append(row)
    marchData.insert(0, header)

    # open/create "AirQualityMarch.csv"
    # Add rows to csv , include header
    with open("AirQualityMarch.csv", "w") as file:
        for line in marchData:
            file.write(f"{line}\n")


# Purpose: write monthly responses files to a new directory called "monthly_responses",
# in the same location as AirQuality.csv, each using the name format "mm-yyyy.csv",
# including the header row of labels in each one.
# Example
#   Call: create_monthly_responses("AirQuality.csv")
#   Returns: nothing, but files such as monthly_responses/05-2004.csv exist containing
#            data matching responses from that month and year
def create_monthly_responses(filename):
    pass
