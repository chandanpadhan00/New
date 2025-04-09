#!/usr/bin/env python3
from datetime import datetime
from zoneinfo import ZoneInfo
from dateutil.relativedelta import relativedelta

def main():
    # Prompt the user to enter a timestamp in the required format.
    user_input = input("Enter PST timestamp (MM/DD/YYYY hh:mm:ss AM/PM): ").strip()

    # Parse the input string into a naive datetime object.
    # Expected format: MM/DD/YYYY hh:mm:ss AM/PM (e.g., "04/15/2020 08:30:00 PM")
    try:
        pst_naive = datetime.strptime(user_input, "%m/%d/%Y %I:%M:%S %p")
    except ValueError:
        print("Error: Incorrect format. Please use MM/DD/YYYY hh:mm:ss AM/PM.")
        return

    # Convert the naive datetime to a timezone-aware datetime in the PST zone.
    # Using the "America/Los_Angeles" zone ensures that daylight saving time is handled correctly.
    pst_time = pst_naive.replace(tzinfo=ZoneInfo("America/Los_Angeles"))

    # Obtain the current time in IST (Indian Standard Time).
    current_ist = datetime.now(ZoneInfo("Asia/Kolkata"))

    # Calculate the difference using relativedelta.
    # Determine whether the input time is in the past or future relative to current IST.
    if current_ist >= pst_time:
        delta = relativedelta(current_ist, pst_time)
        suffix = "ago"
    else:
        delta = relativedelta(pst_time, current_ist)
        suffix = "from now"

    # Output the difference in a human-readable format.
    # The output will be of the form:
    # X years, Y months, Z days, P hours, Q minutes <suffix>
    print(f"{abs(delta.years)} years, {abs(delta.months)} months, {abs(delta.days)} days, "
          f"{abs(delta.hours)} hours, {abs(delta.minutes)} minutes {suffix}")

if __name__ == '__main__':
    main()
