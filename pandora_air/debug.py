from scrapy import cmdline
# cmdline.execute("scrapy crawl bad_proxy".split())
cmdline.execute("scrapy crawl first -a route=ALL_ROUTE".split())
