from datetime import datetime, date

# Get start date from user
start_date_str = input("Enter start date (dd/mm/yy): ")
start_date = datetime.strptime(start_date_str, "%d/%m/%y").date()

# Get end date from user (default to today if not provided)
end_date_str = input("Enter end date (dd/mm/yy, press Enter for today): ")
if end_date_str == "":
    end_date = date.today()
else:
    end_date = datetime.strptime(end_date_str, "%d/%m/%y").date()

# Calculate time duration in days
time_duration_days = (end_date - start_date).days

# Calculate time duration in hours, minutes, and seconds
time_duration_hours = time_duration_days * 24
time_duration_minutes = time_duration_hours * 60
time_duration_seconds = time_duration_minutes * 60

# Calculate time duration in weeks and days
time_duration_weeks = time_duration_days // 7
time_duration_remaining_days = time_duration_days % 7

# Calculate current year's start and end dates
current_year = datetime.now().year
current_year_start = date(current_year, 1, 1)
current_year_end = date(current_year, 12, 31)

# Calculate days in current year
days_in_current_year = (current_year_end - current_year_start).days

# Calculate time duration percentage of current year
time_duration_percentage = (time_duration_days / days_in_current_year) * 100

# Display results
print(f"Time duration: {time_duration_days} days")
print(f"Time duration: {time_duration_hours} hours")
print(f"Time duration: {time_duration_minutes} minutes")
print(f"Time duration: {time_duration_seconds} seconds")
print(f"Time duration: {time_duration_weeks} weeks and {time_duration_remaining_days} days")
print(f"Time duration: {time_duration_percentage:.2f}% of current year")

