from datetime import datetime

def calculate_age(birth_date_str):
    # Convert string to date object
    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
    today = datetime.now().date()

    # Calculate difference
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    # Adjust if needed
    if days < 0:
        months -= 1
        previous_month = today.month - 1 or 12
        year = today.year if previous_month != 12 else today.year - 1

        start = datetime(year, previous_month, 1)
        end = datetime(year, previous_month + 1, 1)
    
        days += (end - start).days

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

# User input
dob = input("Enter your birthdate (YYYY-MM-DD): ")
years, months, days = calculate_age(dob)

print(f"You are {years} years, {months} months, and {days} days old.")
