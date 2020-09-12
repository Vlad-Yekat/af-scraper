""" spider for crawl pandora_air.
shedule of each direction """
from datetime import date, timedelta, datetime
import json
import time
import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

from ..airports import read_airports
from ..proxies import ProxyList
from ..items import ScheduleItem
from ..flights import get_list_month, get_period_flight


class ScheduleSpider(scrapy.Spider):
    """ shedule attemp to crawl"""

    name = "schedule"
    now = datetime.now()
    ERROR_SCHEDULE_URLS = 'errors/error_schedule_urls.txt'
    ERROR_SCHEDULE_PROXY = 'errors/error_schedule_proxy.txt'
    LOG_SCHEDULE_PROXY = 'logs/error_schedule_proxy.txt'

    ERROR_SCHEDULE_URLS = ERROR_SCHEDULE_URLS + str(now.day) + str(now.hour) + str(now.minute)
    ERROR_SCHEDULE_PROXY = ERROR_SCHEDULE_PROXY + str(now.day) + str(now.hour) + str(now.minute)
    LOG_SCHEDULE_PROXY = LOG_SCHEDULE_PROXY + str(now.day) + str(now.hour) + str(now.minute)

    def upload_error_urls(self, count):
        """ list of urls that had errors """
        bad_urls = []
        with open(self.ERROR_SCHEDULE_URLS) as file_urls:
            for line in file_urls:
                bad_urls.append(line)
        open(self.ERROR_SCHEDULE_URLS, "w").close()

        if count == 1 and len(bad_urls) > 50:
            pass  # TODO send request to admin

        return bad_urls

    def start_requests(self):
        """ need for scrapy framework"""
        proxy_list = ProxyList()
        #proxy_list.refresh_proxy()
        proxy_list.load_proxy()
        file_error_urls = open(self.ERROR_SCHEDULE_URLS, 'w')
        file_error_proxy = open(self.ERROR_SCHEDULE_PROXY, 'w')
        file_error_urls.close()
        file_error_proxy.close()

        airports = read_airports()
        urls = []
        for airport in airports:
            # if airport["iataCode"] == "STN":  # fot test or for parallel?
                origin = airport["iataCode"]
                for route in airport["routes"]:
                    type_route = route.split(":")[0]
                    iata_code = route.split(":")[1]
                    if type_route == "airport":
                        destination = iata_code
                        begin_flight, end_flight = get_period_flight(
                            origin, destination
                        )
                        if end_flight:
                            urls.append(
                                # f"http://vladrybin.pythonanywhere.com/farfnd/3/roundTripFares/"
                                f"https://services-api.pandora_air.com/farfnd/3/roundTripFares/"
                                f"{origin}/"
                                f"{destination}/cheapestPerDay?outboundDateFrom="
                                f"{begin_flight}&outboundDateTo="
                                f"{end_flight}"
                            )
        full_len = len(urls)
        full_len_start = full_len
        for url in urls:
            full_len = full_len - 1
            next_proxy = "http://" + proxy_list.get_next()
            print("============", full_len, "=/=", full_len_start, "====", next_proxy)
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                errback=self.err_back,
                headers={"content-type": "application/json"},
                meta={"proxy": next_proxy},
            )

        count = 10
        while count > 0:
            print(" * * * * * * *reserved  * * * * * * * *")

            time.sleep(5)
            count = count - 1
            bad_urls = self.upload_error_urls(count)
            if bad_urls:
                file_logs = open(self.LOG_SCHEDULE_PROXY, 'a+')
                file_logs.write(len(bad_urls) + '\n')
                file_logs.close()
                urls = bad_urls
                for url in urls:
                    next_proxy = "http://" + proxy_list.get_next()
                    yield scrapy.Request(
                        url=url,
                        callback=self.parse,
                        errback=self.err_back,
                        headers={"content-type": "application/json"},
                        meta={"proxy": next_proxy},
                    )

    def parse(self, response):
        full_answer = response.body
        full_answer_string = full_answer.decode("UTF-8")
        answer_json = json.loads(full_answer_string)
        error_exist = answer_json.get("code", "")
        if error_exist:
            yield
        url_list = response.url.split("/")
        origin = url_list[6]
        destination = url_list[7]
        # year = url_list[9]
        fares = answer_json["outbound"]["fares"]
        list_all_days = []
        for one_day in fares:
            if one_day["unavailable"] == False:
                day_exist = one_day["day"]
                list_all_days.append(day_exist)

        schedule_item = ScheduleItem()
        # schedule_item["origin"] = origin
        # schedule_item["destination"] = destination
        # schedule_item["year"] = year
        # schedule_item["month"] = month
        schedule_item["key"] = origin + destination
        schedule_item["days"] = list_all_days

        yield schedule_item

    def err_back(self, failure):

        file_error_urls = open(self.ERROR_SCHEDULE_URLS, 'a+')
        file_error_proxy = open(self.ERROR_SCHEDULE_PROXY, 'a+')

        # file_error_urls = open(ERROR_SCHEDULE_URLS, 'a+')
        # file_error_proxy = open(ERROR_SCHEDULE_PROXY, 'a+')

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

