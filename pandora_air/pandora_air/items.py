# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PandoraAirItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DirectionItem(scrapy.Item):
    last_flight_date = scrapy.Field()
    origin = scrapy.Field()
    destination = scrapy.Field()


class ScheduleItem(scrapy.Item):
    # origin = scrapy.Field()
    # destination = scrapy.Field()
    # month = scrapy.Field()
    # year = scrapy.Field()
    # month = scrapy.Field()
    key = scrapy.Field()
    days = scrapy.Field()


class GoodProxy(scrapy.Item):
    proxy_ip = scrapy.Field
    proxy_port = scrapy.Field


class FirstItem(scrapy.Item):
    errored_criteria_ids = scrapy.Field()
    flights = scrapy.Field()

    # acquired_at = scrapy.Field()    # now
    # arrival_airport_iata_code = scrapy.Field()
    # currency_code = scrapy.Field()
    # departure_airport_iata_code = scrapy.Field()
    # departure_date_time = scrapy.Field()
    # fight_matching_type = scrapy.Field() # ONE_WAY_ONLY​