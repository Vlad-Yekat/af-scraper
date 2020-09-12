""" spider for crawl pandora_air.
shedule of each direction """
import json

import scrapy
from ..airports import read_airports
from ..proxies import ProxyList
from ..items import ScheduleItem
from ..flights import get_list_month


class ScheduleSpiderOld(scrapy.Spider):
    """ shedule attemp to crawl"""

    name = "schedule_old"

    def start_requests(self):
        """ need for scrapy framework"""
        proxy_list = ProxyList()
        proxy_list.refresh_proxy()

        airports = read_airports()
        urls = []
        for airport in airports:
            if airport["iataCode"] == "STN":  # fot test or for parallel?
                origin = airport["iataCode"]
                for route in airport["routes"]:
                    type_route = route.split(":")[0]
                    iata_code = route.split(":")[1]
                    if type_route == "airport":
                        destination = iata_code
                        ordered_months = get_list_month(origin, destination)
                        if ordered_months:
                            for dat_item in ordered_months:
                                urls.append(
                                    # f"http://jhgkjhgj.pythonanywhere.com/timtbl/3/schedules/"
                                    f"https://services-api.pandora_air.com/timtbl/3/schedules/"
                                    f"{origin}/"
                                    f"{destination}/years/"
                                    f"{dat_item}"
                                )
        # print(urls[:10])
        # urls = urls[:10]
        for url in urls:
            next_proxy = "http://" + proxy_list.get_next()
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                headers={"content-type": "application/json"},
                meta={"proxy": next_proxy},
            )

    def parse(self, response):
        full_answer = response.body
        full_answer_string = full_answer.decode("UTF-8")
        answer_json = json.loads(full_answer_string)
        error_exist = answer_json.get("code", '')
        if error_exist:
            yield
        url_list = response.url.split("/")
        origin = url_list[6]
        destination = url_list[7]
        year = url_list[9]
        month = answer_json["month"]
        all_days = answer_json["days"]
        list_all_days = [one_day["day"] for one_day in all_days]

        schedule_item = ScheduleItem()
        # schedule_item["origin"] = origin
        # schedule_item["destination"] = destination
        schedule_item["year"] = year
        schedule_item["month"] = month
        schedule_item["key"] = origin + destination
        schedule_item["days"] = list_all_days

        yield schedule_item
