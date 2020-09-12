"""
second prepare 1/day after proxy or parallel
load airports
"""
import json
import requests

ALL_AIRPORTS = "https://services-api.pandora_air.com/locate/3/common?embedded=airports"
FILE_AIRPORTS = "config/airports.json"
FILE_AIRPORTS_WORLD = "config/airports.dat"
FILE_COUNTRY_WORLD = "config/countries.dat"


def download_airports():
    """ dowload from pandora_air all routes """
    response = requests.get(ALL_AIRPORTS)
    if response.status_code == 200:
        airports_json = response.json()

        with open(FILE_AIRPORTS, "w") as file_airports:
            json.dump(airports_json, file_airports)


def read_airports_world():
    """ for total classification """
    all_world_airports = {}
    with open(FILE_AIRPORTS_WORLD) as dat_file:
        for line in dat_file:
            one_line = line.replace('"', '').split(",")
            airport_code = one_line[4]
            airport_country_name = one_line[3]
            all_world_airports[airport_code] = airport_country_name

    return all_world_airports


def read_countries_world():
    """ for total classification """
    all_country_airports = {}
    with open(FILE_COUNTRY_WORLD) as dat_file:
        for line in dat_file:
            one_line = line.replace('"', '').split(",")
            country_code = one_line[2]
            country_name = one_line[0]
            region_code = one_line[4]
            all_country_airports[country_name] = [country_code, region_code]

    return all_country_airports


def read_airports():
    """ for some purposes in spiders """
    download_airports()

    with open(FILE_AIRPORTS) as json_file:
        data = json.load(json_file)

    airports = data["airports"]

    return airports


def read_airports_country():
    """ manual file with correct country and region """
    with open("config/airports_country.json") as json_file:
        data = json.load(json_file)

    airports = data["airports"]
    airports_country = {}
    for airport in airports:
        airports_country[airport["iataCode"]] = [
            airport["regionName"],
            airport["countryCode"],
        ]
    return airports_country


def make_airports_country():
    """ automatic with correct country and region """
    all_airports = read_airports_world()
    all_countries = read_countries_world()
    pandora_air_airports = read_airports()
    airports_country = {}

    for airport in pandora_air_airports:
        country_name = all_airports[airport["iataCode"]]
        country_code = all_countries[country_name][0]
        region_code = all_countries[country_name][1]
        airports_country[airport["iataCode"]] = [
            region_code,
            country_code
        ]

    return airports_country


if __name__ == "__main__":
    # list_airports = read_airports_country()
    # list_airports = read_airports()
    make_airports_country()
    # print(list_airports)
