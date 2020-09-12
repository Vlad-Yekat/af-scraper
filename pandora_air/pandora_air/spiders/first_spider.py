""" spider for crawl pandora_air """
from datetime import date, timedelta, datetime
import re
import time
from dateutil.relativedelta import relativedelta
import json
import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError
from ..airports import read_airports, make_airports_country
from ..proxies import ProxyList
from ..flights import get_schedule
from ..items import FirstItem
from ..ext_settings import PRICE_URL, MIN_DATE_FLIGHT


class FirstSpider(scrapy.Spider):
    """ first attemp to crawl"""

    name = "first"
    list_routes = []
    now = datetime.now()
    ERROR_FIRST_URLS = 'errors/error_first_urls.txt'
    ERROR_FIRST_PROXY = 'errors/error_first_proxy.txt'
    LOG_FIRST_PROXY = 'logs/error_first_proxy.txt'

    ERROR_FIRST_URLS = ERROR_FIRST_URLS + str(now.day) + str(now.hour) + str(now.minute)
    ERROR_FIRST_PROXY = ERROR_FIRST_PROXY + str(now.day) + str(now.hour) + str(now.minute)
    LOG_FIRST_PROXY = LOG_FIRST_PROXY + str(now.day) + str(now.hour) + str(now.minute)

    def upload_error_urls(self, count):
        """ list of urls that had errors """
        bad_urls = []
        with open(self.ERROR_FIRST_URLS) as file_urls:
            for line in file_urls:
                bad_urls.append(line)
        open(self.ERROR_FIRST_URLS, "w").close()

        if count == 1 and len(bad_urls) > 50:
            pass  # TODO send request to admin

        return bad_urls

    def start_requests(self):
        """ need for scrapy framework"""
        if self.route:
            arg_routes = str(self.route).split(",")
            self.list_routes.extend(arg_routes)

        proxy_list = ProxyList()
        # proxy_list.refresh_proxy()
        proxy_list.load_proxy()  # since shared pool
        file_error_urls = open(self.ERROR_FIRST_URLS, 'w')
        file_error_proxy = open(self.ERROR_FIRST_PROXY, 'w')
        file_error_urls.close()
        file_error_proxy.close()

        schedule = get_schedule()

        airports = read_airports()
        airports_country = make_airports_country()
        urls = []

        for airport in airports:
            origin = airport["iataCode"]
            if self.route == "ALL_ROUTE" or airport["iataCode"] in self.list_routes:
                for route in airport["routes"]:
                    type_route = route.split(":")[0]
                    iata_code = route.split(":")[1]
                    if type_route == "airport":
                        list_dates = schedule.get(origin + iata_code, "")
                        # print(list_dates)
                        curr_date = MIN_DATE_FLIGHT  # simple min
                        for dat_item in list_dates:
                            date_var = dat_item
                            if datetime.strptime(date_var, "%Y-%m-%d") > (
                                datetime.strptime(curr_date, "%Y-%m-%d")
                                + timedelta(days=5)
                            ):
                                curr_date = date_var
                                destination = iata_code

                                origin_region = airports_country[origin][0]
                                origin_country = airports_country[origin][1]
                                destination_region = airports_country[destination][0]
                                destination_country = airports_country[destination][1]

                                list_packs = []
                                list_packs.append([1, 1])
                                if (
                                    origin_region in ("UK", "IE")
                                    and destination_region == "EU"
                                ):
                                    list_packs.append([2, 1])
                                    list_packs.append([3, 1])
                                elif origin_region == "EU":
                                    pass

                                if (
                                    origin_region == "EU" or destination_region == "EU"
                                ) and (
                                    origin_country in ("SE", "FI", "NO", "DK")
                                    or destination_country in ("SE", "FI", "NO", "DK")
                                ):
                                    list_packs.append([2, 1])
                                    list_packs.append([3, 1])

                                for packs in list_packs:
                                    adult_count = packs[0]
                                    child_count = packs[1]
                                    list_trip = ["true", "false"]
                                    for round_trip in list_trip:
                                        urls.append(
                                            f"{PRICE_URL}"
                                            f"?ADT={adult_count}"
                                            f"&CHD={child_count}"
                                            f"&DateIn={date_var}"
                                            f"&DateOut={date_var}"
                                            f"&Destination={destination}"
                                            f"&FlexDaysIn=6"
                                            f"&FlexDaysOut=6"
                                            f"&INF=0"
                                            f"&IncludeConnectingFlights=false"  # ?
                                            f"&Origin={origin}"
                                            f"&RoundTrip={round_trip}"
                                            f"&TEEN=0"
                                            f"&ToUs=AGREED"
                                            f"&exists=false"
                                        )

        full_len = len(urls)
        full_len_start = full_len
        # print(full_len)
        # urls = urls[:40]
        # a = 1 / 0
        for url in urls:
            full_len = full_len - 1
            next_proxy = "http://" + proxy_list.get_next()
            print("============", full_len, "=/=", full_len_start, "====", next_proxy)
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                errback=self.err_back,
                meta={"proxy": next_proxy}
            )

        count = 10
        while count > 0:
            print(" * * * * * * *reserved  * * * * * * * *")
            time.sleep(5)
            count = count - 1
            bad_urls = self.upload_error_urls(count)
            if bad_urls:
                urls = bad_urls
                full_len = len(urls)
                full_len_start = full_len
                file_logs = open(self.LOG_FIRST_PROXY, 'a+')
                file_logs.write(full_len + '\n')
                file_logs.close()

                for url in urls:
                    full_len = full_len - 1
                    next_proxy = "http://" + proxy_list.get_next()
                    print("============", full_len, "=/=", full_len_start, "====", next_proxy)
                    yield scrapy.Request(
                        url=url,
                        callback=self.parse,
                        errback=self.err_back,
                        meta={"proxy": next_proxy}
                    )

    def parse(self, response):
        # file_good_urls = open('work/good_last_urls.txt', 'a+')
        # file_good_proxy = open('work/good_last_proxy.txt', 'a+')
        #
        # file_good_proxy.write(response.meta['proxy'] + '\n')
        # file_good_urls.write(response.url + '\n')
        # file_good_urls.close()
        # file_good_proxy.close()

        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        origin_search = re.search(r"Origin=[A-Z][A-Z][A-Z]", response.url)
        origin_airport = origin_search.group(0)[-3:]
        full_answer = response.body
        full_answer_string = full_answer.decode("UTF-8")
        answer_json = json.loads(full_answer_string)

        first_item = FirstItem()

        trips = answer_json["trips"]
        list_flights = []
        for trip in trips:

            dates_out = trip["dates"]

            for date_out in dates_out:
                if date_out["flights"]:
                    flight_dict = {}
                    flight_dict["in/out"] = "out" if trip["origin"] == origin_airport else "in"
                    flight_dict["origin_country_airport"] = origin_airport
                    flight_dict["acquired_at"] = answer_json["serverTimeUTC"]
                    flight_dict["arrival_airport_iata_code"] = trip["destination"]
                    flight_dict["currency_code"] = answer_json["currency"]
                    flight_dict["departure_airport_iata_code"] = trip["origin"]

                    flight_dict["departure_date_time"] = date_out["dateOut"]
                    flight_dict["fight_matching_type"] = "PAIRED_RETURN"
                    # flight_dict["fight_matching_type"] = "ONE_WAY_ONLY​"

                    flights = date_out["flights"]
                    fares = flights[0]["regularFare"]["fares"]
                    adult_fare = 0
                    child_fare = 0
                    for fare in fares:
                        if fare["type"] == "ADT":
                            adult_fare = fare["amount"]
                        if fare["type"] == "CHD":
                            child_fare = fare["amount"]

                    main_segment = {}
                    main_segment["availableSeats"] = 25
                    main_segment["baggage"] = []
                    main_segment["cabinClass"] = "ECONOMY"
                    main_segment["cat35"] = False
                    main_segment["costs"] = [
                        {"baseFare": adult_fare, "passengerType": "ADULT", "taxes": 0},
                        {"baseFare": child_fare, "passengerType": "CHILD", "taxes": 0},
                        {"baseFare": 0, "passengerType": "INFANT", "taxes": 0},
                    ]
                    main_segment["durationMinutes"] = 0
                    main_segment["fareOwner"] = None
                    main_segment["fareType"] = "NO_FRILLS"
                    main_segment["legs"] = []
                    main_segment["maxChildAge"] = 15
                    main_segment["maxInfantAge"] = 2
                    main_segment["numberLegs"] = 1
                    main_segment["numberStops"] = 0
                    main_segment["seatType"] = "SEAT_ONLY"

                    flight_dict["main_segment"] = main_segment
                    flight_dict["paired_return_segment"] = {}
                    flight_dict["return_departure_date_time"] = ""
                    flight_dict["criteria_id"] = (
                        trip["origin"] + "-" + trip["destination"]
                    )

                    list_flights.append(flight_dict)

        first_item["flights"] = list_flights

        yield first_item

    def err_back(self, failure):

        file_error_urls = open(self.ERROR_FIRST_URLS, 'a+')
        file_error_proxy = open(self.ERROR_FIRST_PROXY, 'a+')

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('!!HttpError on %s', response.url)
            file_error_urls.write(response.url + '\n')
            file_error_proxy.write(response.meta['proxy'] + '\n')

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('!!DNSLookupError on %s', request.url)
            file_error_urls.write(request.url + '\n')
            file_error_proxy.write(request.meta['proxy'] + '\n')

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('!!TimeoutError on %s', request.url)
            file_error_urls.write(request.url + '\n')
            file_error_proxy.write(request.meta['proxy'] + '\n')

        file_error_urls.close()
        file_error_proxy.close()

