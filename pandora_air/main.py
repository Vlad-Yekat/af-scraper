from scrapy import cmdline
# cmdline.execute("scrapy crawl bad_proxy".split())
cmdline.execute("scrapy crawl bad_proxy -a route=AAR".split())
