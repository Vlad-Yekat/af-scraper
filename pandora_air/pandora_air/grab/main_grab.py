from grab.spider import Spider, Task
from airports import read_airports
from proxies import ProxyList
from ext_settings import DIRECTION_URL


class MinSpider(Spider):
    def task_generator(self):
        proxy_list = ProxyList()
        # proxy_list.load_proxy()
        # g = Grab()
        # g.proxylist.set_source('file', location='/config/good_proxy.txt')

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
            # next_proxy = "http://" + proxy_list.get_next()
            print(full_len)
            yield Task('parse', url=url)

    def task_parse(self, grab, task):
        print(task.url)
        print(grab.response.code)


bot = MinSpider(thread_number=100)
bot.proxylist_enabled = True
bot.load_proxylist('/home/VladislavRybin/test_projects/af-scraper/pandora_air/pandora_air/grab/config/list_free_proxies.txt', 'text_file')
# bot.proxylist = ['xx.yyy.zz.95:4000', 'xx.yyy.zz.95:4001']
# bot.proxy_auto_change = True
# bot.proxylist.set_source('file', location='/config/good_proxy.txt')
bot.run()
