def convert_to_24_hour(time_str):
    # Split the input into time and period (AM/PM)
    time, period = time_str.split()
    
    # Split the time into hours and minutes
    hours, minutes = map(int, time.split(':'))
    
    # Convert hours based on the period (AM/PM)
    if period.upper() == "PM" and hours != 12:
        hours += 12
    elif period.upper() == "AM" and hours == 12:
        hours = 0
    
    # Format the hours and minutes into 24-hour format
    return f"{hours:02}:{minutes:02}"

# Example usage
time_12_hour = input()
time_24_hour = convert_to_24_hour(time_12_hour)
print("24-hour format:", time_24_hour)
