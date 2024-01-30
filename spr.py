# Song Power Reader
# James Song 2023-Jan-30

import csv
from datetime import datetime

def calculate_usage(data):
    result_data = {}
    
    for row in data:
        if len(row) != 6:
            continue  # Skip rows that don't have the expected number of columns
        
        type_str, date_str, start_time, end_time, usage_str, cost_str = row
        if date_str == 'DATE':
            continue  # Skip header
        
        # Convert usage and cost to float
        usage = float(usage_str)
        
        # Parse date and time
        datetime_obj = datetime.strptime(date_str + " " + start_time, "%Y-%m-%d %H:%M")
        
        # Assign the usage to the corresponding time range
        if 0 <= datetime_obj.hour < 7:
            time_range = "00:00-06:59"
        elif 7 <= datetime_obj.hour < 12:
            time_range = "07:00-11:59"
        elif 12 <= datetime_obj.hour < 17:
            time_range = "12:00-16:59"
        elif 17 <= datetime_obj.hour < 21:
            time_range = "17:00-20:59"
        else:
            time_range = "21:00-23:59"
        
        # Initialize the dictionary if date is encountered for the first time
        if date_str not in result_data:
            result_data[date_str] = {"Total": 0.0, "DayOfWeek": datetime_obj.strftime("%a")}
        
        # Assign usage to the corresponding time range
        result_data[date_str][time_range] = round(result_data[date_str].get(time_range, 0) + usage, 2)
        
        # Add usage to the total for the day
        result_data[date_str]["Total"] += usage
    
    return result_data

def write_output(result_data):
    with open('output23.csv', 'w', newline='') as csvfile:
        fieldnames = ['Date', 'DayOfWeek', '00:00-06:59', '07:00-11:59', '12:00-16:59', '17:00-20:59', '21:00-23:59', 'Total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header
        writer.writeheader()
        
        # Write data
        for date, values in result_data.items():
            # Round the "Total" value to two significant digits
            values["Total"] = round(values["Total"], 2)
            
            row = {'Date': date}
            row.update(values)
            writer.writerow(row)
    
    print("File written successfully!")

# Read the input CSV file
with open('2023.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

# Calculate usage
result_data = calculate_usage(data)

# Write output to CSV
write_output(result_data)
