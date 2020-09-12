"""
Here we transfer our raw files to client_side formats etc
"""
import os
import json
from airports import read_airports, read_airports_country

CONFIG_FOLDER = 'config/'
CONSUMER_FOLDER = 'ready_data/'


def main_transfer():
    """
    Look all raw flight files
    :return:
    """
    for the_file in os.listdir(CONFIG_FOLDER):
        file_path = os.path.join(CONFIG_FOLDER, the_file)
        if os.path.isfile(file_path):
            file_name, file_extension = os.path.splitext(the_file)
            if file_extension == '.flight':
                prepare_flight(the_file)


def prepare_flight(the_file):
    """
    Work with one flight file
    :param the_file:
    :return:
    """
    with open(CONFIG_FOLDER + the_file) as flight_file:
        for line in flight_file:
            flight = json.loads(line)
            for one_flight in flight["flights"]:
                move_flight(one_flight)


def move_flight(one_flight):
    """
    move one flight into another file
    :param one_flight:
    :return:
    """
    departure = one_flight["departure_airport_iata_code"]
    currency = one_flight["currency_code"]
    arrival = one_flight["arrival_airport_iata_code"]
    origin_country_airport = one_flight["origin_country_airport"]
    airports_country = read_airports_country()

    origin_region = airports_country[departure][0]
    origin_country = airports_country[departure][1]
    main_origin_country = airports_country[origin_country_airport][1]
    destination_region = airports_country[arrival][0]
    destination_country = airports_country[arrival][1]
    if origin_region == 'UK' and destination_region == 'EU':
        origin_country = origin_country + '_TYPE'

    file_new_origin = open(CONSUMER_FOLDER + main_origin_country + '.fly', 'a+')
    file_new_origin.write(json.dumps(one_flight) + '\n')
    file_new_origin.close()


if __name__ == "__main__":
    main_transfer()
