"""
some wraps on flights information
"""
import json
from datetime import date, timedelta, datetime
from collections import OrderedDict


def get_list_month(origin, destination):
    """
    returns
    keys(['2014/months/10', '2014/months/11', ...])

    """
    end_flights = read_end_flights()
    today = datetime.now()
    end_date = end_flights.get(origin + destination, "")
    # end_date = datetime.now() + timedelta(days=15)
    if not end_date:
        return None
    end_date = datetime.strptime(end_flights[origin + destination], "%Y-%m-%d")
    # end_date = datetime.now() + timedelta(days=15)
    return OrderedDict(
        ((today + timedelta(_)).strftime(r"%Y/months/%m"), None)
        for _ in range((end_date - today).days)
    ).keys()


def get_period_flight(origin, destination):
    """
    returns
    end date_of flight
    and today

    """
    end_flights = read_end_flights()
    today = str(date.today())
    end_date = end_flights.get(origin + destination, "")
    return today, end_date


def read_end_flights():
    dict_flights = {}  # key = (origin+dest) for hash access
    with open("config/date_end.txt") as file_end_dates:
        for line in file_end_dates:
            flight = json.loads(line)
            dict_flights[flight["origin"] + flight["destination"]] = flight[
                "last_flight_date"
            ]

    return dict_flights


def get_schedule():
    dict_schedule = {}  # key = (origin+dest) for hash access
    with open("config/schedule_flights.txt") as file_schedule:
        for line in file_schedule:
            flight = json.loads(line)
            dict_schedule[flight["key"]] = flight["days"]

    return dict_schedule


def get_schedule_old():

    dict_schedule = {}  # key = (origin+dest) for hash
    with open("config/schedule_flights.txt") as file_schedule:
        for line in file_schedule:
            flight = json.loads(line)
            key = flight["key"]
            month = str(flight["month"]).zfill(2)

            year = flight["year"]
            new_list = []
            day_list = flight["days"]
            for day_one in day_list:
                day_new = year + '-' + month + '-' + str(day_one).zfill(2)
                new_list.append(day_new)

            prev_list = dict_schedule.get(key, [])
            prev_list.extend(new_list)
            dict_schedule[key] = prev_list

    return dict_schedule


if __name__ == "__main__":
    # print(read_end_flights())
    schedule = get_list_month("STN", "NYO")
    print(schedule)
    # AARDUB
    schedule = get_list_month("AAR", "DUB")
    print(schedule)
