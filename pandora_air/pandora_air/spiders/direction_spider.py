""" spider for crawl pandora_air. end data of each direction """
from datetime import date, timedelta, datetime
import json
import time
import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

from ..airports import read_airports
from ..proxies import ProxyList
from ..items import DirectionItem
from ..ext_settings import DIRECTION_URL

ERROR_DIRECTION_URLS = "errors/error_direction_urls.txt"
ERROR_DIRECTION_PROXY = "errors/error_direction_proxy.txt"


class DirectionSpider(scrapy.Spider):
    """ direction attemp to crawl"""

    name = "direction"
    now = datetime.now()

    def upload_error_urls(self, count):
        """ list of urls that had errors """
        bad_urls = []
        with open(ERROR_DIRECTION_URLS) as file_urls:
            for line in file_urls:
                bad_urls.append(line)
        open(ERROR_DIRECTION_URLS, "w").close()

        if count == 1 and len(bad_urls) > 10:
            pass  # TODO send request to admin

        return bad_urls

    def start_requests(self):
        """ need for scrapy framework"""
        proxy_list = ProxyList()
        proxy_list.load_proxy()
        file_error_urls = open(ERROR_DIRECTION_URLS, "w")
        file_error_proxy = open(ERROR_DIRECTION_PROXY, "w")
        file_error_urls.close()
        file_error_proxy.close()

        airports = read_airports()
        urls = []
        for airport in airports:
            origin = airport["iataCode"]
            for route in airport["routes"]:
                type_route = route.split(":")[0]
                iata_code = route.split(":")[1]
                if type_route == "airport":
                    destination = iata_code
                    urls.append(
                        f"{DIRECTION_URL}"
                        f"{origin}/"
                        f"{destination}/period"
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

        count = 2
        while count > 0:
            print(" * * * * * * *reserved  * * * * * * * *")
            time.sleep(5)
            count = count - 1
            bad_urls = self.upload_error_urls(count)
            if bad_urls:
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
        """ good request """
        full_answer = response.body
        full_answer_string = full_answer.decode("UTF-8")
        answer_json = json.loads(full_answer_string)
        last_flight_date = answer_json.get('lastFlightDate','')
        if last_flight_date:
            url_list = response.url.split("/")
            origin = url_list[6]
            destination = url_list[7]
            direction_item = DirectionItem()
            direction_item["last_flight_date"] = last_flight_date
            direction_item["origin"] = origin
            direction_item["destination"] = destination
            yield direction_item

    def err_back(self, failure):
        """ bad request, with errors """

        file_error_urls = open(ERROR_DIRECTION_URLS + str(self.now.day) + str(self.now.hour) + str(self.now.minute), 'a+')
        file_error_proxy = open(ERROR_DIRECTION_PROXY + str(self.now.day) + str(self.now.hour) + str(self.now.minute), 'a+')

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error("!!HttpError on %s", response.url)
            file_error_urls.write(response.url + "\n")
            file_error_proxy.write(response.meta["proxy"] + "\n")

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error("!!DNSLookupError on %s", request.url)
            file_error_urls.write(request.url + "\n")
            file_error_proxy.write(request.meta["proxy"] + "\n")

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error("!!TimeoutError on %s", request.url)
            file_error_urls.write(request.url + "\n")
            file_error_proxy.write(request.meta["proxy"] + "\n")

        file_error_urls.close()
        file_error_proxy.close()
