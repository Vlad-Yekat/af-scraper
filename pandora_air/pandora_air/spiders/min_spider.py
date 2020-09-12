""" spider for crawl pandora_air. end data of each direction """
import json
import scrapy
import time
from ..airports import read_airports
from ..proxies import ProxyList
from ..items import DirectionItem
from ..ext_settings import DIRECTION_URL


class MinSpider(scrapy.Spider):
    """ direction attemp to crawl"""

    name = "min"

    def start_requests(self):
        """ need for scrapy framework"""
        proxy_list = ProxyList()
        proxy_list.load_proxy()

        airports = read_airports()
        urls = []
        for airport in airports:
            origin = airport["iataCode"]
            for route in airport["routes"]:
                type_route = route.split(":")[0]
                iata_code = route.split(":")[1]
                if type_route == "airport":
                    some_list = [x for x in range(100)]
                    destination = iata_code
                    for some_one in some_list:
                        urls.append(
                            f"{DIRECTION_URL}"
                            f"{origin}/"
                            f"{destination}/period"
                        )
        full_len = len(urls)
        for url in urls:
            full_len = full_len - 1
            next_proxy = "http://" + proxy_list.get_next()
            print(full_len)
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                errback=self.err_parse,
                headers={"content-type": "application/json", "Proxy-Connection": "close"},
                meta={"proxy": next_proxy},
            )

    def parse(self, response):
        """ good request """
        full_answer = response.body
        full_answer_string = full_answer.decode("UTF-8")
        answer_json = json.loads(full_answer_string)
        time.sleep(0.01)
        direction_item = DirectionItem()
        direction_item["last_flight_date"] = "2010-02-02"
        yield direction_item

    def err_parse(self, response):
        """ good request """
        full_answer = response.body


