""" here we request rsocks.net for list of fresh proxy """
from datetime import timedelta, datetime
import requests
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

AUTH_ID = "49898798002"
AUTH_KEY = "82184e51fljlkjlkjlkj1c51b9021c5b485a2083495d91a459c33410e165"
URL = "https://something.net/api/v1/file/get-proxy"
REFRESH_INTERVAL = 12000
TEST_TIMEOUT = 10


class ProxyList:
    """ class for storing proxy list """

    def __init__(self):
        self.__main_list = []
        self._current_position = 0
        self._last_refresh = datetime.now()

    def get_next(self):
        """ get next proxy ip address """
        # if self._last_refresh + timedelta(seconds=REFRESH_INTERVAL) < datetime.now():
        #     self.refresh_proxy()  # because we are in pool of shared
        value = self.__main_list[self._current_position]
        if self._current_position == (len(self.__main_list) - 1):
            self._current_position = 0
        else:
            self._current_position += 1
        return value

    def get_all(self):
        """ for admin, perhaps """
        value = self.__main_list
        return value

    def refresh_proxy(self):
        """ request from something.net fresh list of ip """
        headers = {"X-Auth-ID": AUTH_ID, "X-Auth-Key": AUTH_KEY}
        rsocks_answer = requests.post(URL, headers=headers)

        get_dict_proxies = rsocks_answer.json()
        get_packet_proxies = get_dict_proxies["packages"]
        get_dict_ips = get_packet_proxies[list(get_packet_proxies)[0]]
        # get_dict_ips = get_packet_proxies[list(get_packet_proxies)[1]]

        self.__main_list = get_dict_ips["ips"]
        self._current_position = 0
        self._last_refresh = datetime.now()
        # self.test_proxy()

    def load_proxy(self):
        self.__main_list = []
        self._current_position = 0
        self._last_refresh = datetime.now()
        with open("config/good_proxy.txt") as proxy_file:
            for line in proxy_file:
                self.__main_list.append(line)

        self.__correct_proxy_list()

        return self.__main_list

    def __correct_proxy_list(self):
        pass
        #  at every step we correct list of good proxy TODO


if __name__ == "__main__":
    # print(read_end_flights())
    proxy_list = ProxyList()
    proxy_list.refresh_proxy()
    print(proxy_list.get_all(), sep='\n')

