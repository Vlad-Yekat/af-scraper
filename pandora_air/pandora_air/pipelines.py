# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


class PandoraAirPipeline(object):
    def process_item(self, item, spider):
        return item


class DirectionPipeline(object):
    list_spider = ('first', )

    def open_spider(self, spider):
        print('-------------------------------------')
        print('spider.name', spider.name)
        print('spider.route', spider.route[:3])
        print('-------------------------------------')
        if spider.name == 'direction':
            self.file = open('config/date_end.txt', 'w')
        elif spider.name == 'schedule':
            self.file = open('config/schedule_flights.txt', 'w')
        elif spider.name == 'bad_proxy':
             self.file = open('config/good_proxy.txt', 'w')
        elif spider.route:
            self.file = open('config/'+spider.route[:3]+'.flight', 'w')

    def close_spider(self, spider):
        print('2spider.name', spider.name)
        if (spider.name == 'direction') or (spider.name == 'schedule') or (spider.name == 'bad_proxy'):
            self.file.close()
        elif spider.name in self.list_spider:
            self.file.close()

    def process_item(self, item, spider):
        print('process item......................', spider.name)
        if spider.name == 'direction':
            if item.get('last_flight_date'):
                line = json.dumps(dict(item)) + "\n"
                self.file.write(line)
        elif spider.name == 'schedule':
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line)
        elif spider.name == 'bad_proxy':
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line)
        elif spider.name in self.list_spider:
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line)
        return item
