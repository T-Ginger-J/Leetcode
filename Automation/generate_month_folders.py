import os
import sys
import calendar

def generate_month(month_num):
    if month_num < 1 or month_num > 12:
        print("Month must be between 1 and 12")
        return

    month_name = calendar.month_name[month_num]
    days_in_month = calendar.monthrange(2025, month_num)[1]  # non-leap year

    os.makedirs(month_name, exist_ok=True)

    for day in range(1, days_in_month + 1):
        os.makedirs(os.path.join(month_name, str(day)), exist_ok=True)

    print(f"Created {month_name} with {days_in_month} day folders.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_month_folders.py <month_number>")
        sys.exit(1)

    generate_month(int(sys.argv[1]))
