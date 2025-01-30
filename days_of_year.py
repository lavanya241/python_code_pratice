def day_of_year(date):
    year, month, day = map(int, date.split('-'))
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check for leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        month_days[1] = 29

    return sum(month_days[:month - 1]) + day #month_days contains the month days and then by slicing month by number of month and add the days to it

# Example usage
date = "2023-01-03"
print(f"The day number for {date} is: {day_of_year(date)}")
