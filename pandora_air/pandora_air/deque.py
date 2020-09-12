#!/usr/bin/python
# -*- coding: utf-8 -*-

from scrapy.crawler import Crawler
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor

# Импортирем пауков
from .spiders.bad_proxy_spider import BadProxySpider
from .spiders.direction_spider import DirectionSpider
from .spiders.schedule_spider import ScheduleSpider
from .spiders.first_spider import FirstSpider

# from spiders.my_settings import options

# Передаем настройки
settings = get_project_settings()
# settings.overrides.update(options)

# Запускаем четыре паука по очереди
crawler = Crawler(settings)
crawler.configure()
crawler.crawl(BadProxySpider())
crawler.start()

crawler = Crawler(settings)
crawler.configure()
crawler.crawl(Mandy())
crawler.start()

crawler = Crawler(settings)
crawler.configure()
crawler.crawl(ProductionHub())
crawler.start()

crawler = Crawler(settings)
crawler.configure()
crawler.crawl(Craiglist())
crawler.start()

# Запускаем реактор
reactor.run()