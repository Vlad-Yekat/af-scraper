""" spider for crawl pandora_air """
import scrapy
from ..proxies import ProxyList
from ..items import GoodProxy

TEST_URL = "http://ksdjfhs.pythonanywhere.com/timtbl/3/schedules/STN/"
ERROR_ALL_PROXY = 'errors/error_all_proxy.txt'
GOOD_PROXY = 'config/good_proxy.txt'


class BadProxySpider(scrapy.Spider):
    """ first attemp to crawl"""

    name = "bad_proxy"

    def start_requests(self):
        """ need for scrapy framework"""

        proxy_list = ProxyList()
        proxy_list.refresh_proxy()
        file_good_proxy = open(GOOD_PROXY, 'w')
        file_good_proxy.close()
        file_bad_proxy = open(ERROR_ALL_PROXY, 'w')
        file_bad_proxy.close()

        urls = []
        urls.extend(proxy_list.get_all())
        if self.route:
            pass

        full_len = len(urls)
        full_len_start = full_len
        for url in urls:
            full_len = full_len - 1
            next_proxy = "http://" + url
            print("============", full_len, "=/=", full_len_start, "====", next_proxy)
            yield scrapy.Request(
                url=TEST_URL+str(full_len),
                callback=self.parse,
                errback=self.err_back,
                meta={"proxy": next_proxy}
            )

    def parse(self, response):
        # good_proxy = GoodProxy()
        file_good_proxy = open(GOOD_PROXY, 'a+')
        proxy = response.meta['proxy']
        file_good_proxy.write(proxy.split('/')[2] + '\n')
        file_good_proxy.close()

        # good_proxy["proxy_ip"] = proxy.split('/')[2]
        # yield good_proxy

    def err_back(self, failure):
        file_error_proxy = open(ERROR_ALL_PROXY, 'a+')
        proxy = failure.request.meta['proxy']
        file_error_proxy.write(proxy.split('/')[2] + '\n')
        file_error_proxy.close()
