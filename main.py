import sys
from typing import List

"""
    Program that calculates the arrival time of a flight

    It receives 4 whole numbers through the command line:
        - #1 Number of hours of flight departure (hours >= 0 && hours <= 23)
        - #2 Number of minutes of flight departure (minutes >= 0 && minutes <= 59)
        - #3 Hours of flight duration >= 0
        - #4 Minutes of flight duration >= 0

    Observations:
        - The provided hours/minutes start time is in 24 hours format


    Output:
        - Hour and minute of arrival


    The idea of the exercise is handle overflowing hours and minutes
"""

# start hour and minute are expected to be in the specified ranges
def main(
    start_hour: int, start_minute: int, duration_hour: int, duration_minute: int
) -> List[int]:
    # calculate arrival hour
    overflowing_arrival_hours = start_hour + duration_hour
    partial_arrival_hours = overflowing_arrival_hours % 24

    # calculate minutes
    overflowing_arrival_minutes = start_minute + duration_minute

    # extract the hours from the minutes
    hours_from_minutes = overflowing_arrival_minutes // 60

    # get remaining minutes
    remaining_minutes = overflowing_arrival_minutes % 60

    # since the added hours could cause the hours to overflow,
    # I have to find the remaining hours after taking days off the total
    # hours
    hours = (partial_arrival_hours + hours_from_minutes) % 24

    # just renaming of the variable
    minutes = remaining_minutes

    # return results
    return [hours, minutes]


if __name__ == "__main__":
    # parse command-line arguments
    args = sys.argv

    try:
        times = [int(args[i]) for i in range(1, 5)]
        main(*times)

    except ValueError:
        print("Please provide valid integers for the values!")

    except IndexError:
        print("All 4 values are required!")
