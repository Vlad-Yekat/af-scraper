# -*- coding: utf-8 -*-

# Scrapy settings for pandora_air project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'pandora_air'

SPIDER_MODULES = ['pandora_air.spiders']
NEWSPIDER_MODULE = 'pandora_air.spiders'

# ROTATING_PROXY_LIST_PATH = 'spiders/list_free_proxies.txt'
ROTATING_PROXY_LIST_PATH = 'config/rsocks.txt'

DOWNLOADER_MIDDLEWARES = {
     # 'pandora_air.middlewares.CustomProxyMiddleware': 350,
     #'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,  # very slow library * 100
     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 100,
     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
     'scrapy_useragents.downloadermiddlewares.useragents.UserAgentsMiddleware': 500,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pandora_air (+http://www.yourdomain.com)'
#USER_AGENT = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'

USER_AGENTS = [
    ('Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/41.0.2272.96 Mobile '
     'Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'),
    ('Googlebot/2.1 '
     '(+http://www.google.com/bot.html)'),
    ('Mozilla/5.0 '
     'AppleWebKit/537.36 (KHTML, like Gecko; compatible; '
     'Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36'),
    ('Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) '
     'AppleWebKit/600.1.4 (KHTML, like Gecko) '
     'Version/8.0 Mobile/12F70 '
     'Safari/600.1.4 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'),
    ('Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) '
     'AppleWebKit/536.26 (KHTML, like Gecko) '
     'Version/6.0 Mobile/10A5376e '
     'Safari/8536.25 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'),
    ('OnPageBot (compatible; Googlebot 2.1;  '
     '+https://bot.onpage.org/) '),
    ('Mozilla/5.0 (compatible; Googlebot/2.1;  '
     'http://www.google.com/bot.html) '),
]

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 99

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docsclear
DOWNLOAD_DELAY = 0.005
# DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 99
CONCURRENT_REQUESTS_PER_IP = 99

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'pandora_air.middlewares.PandoraAirSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'pandora_air.middlewares.PandoraAirDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'pandora_air.pipelines.PandoraAirPipeline': 300,
    'pandora_air.pipelines.DirectionPipeline': 800,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


RETRY_ENABLED = False
RETRY_TIMES = 1
DOWNLOAD_TIMEOUT = 20

HTTPCACHE_ENABLED = False

# AUTOTHROTTLE_ENABLED = True
# AUTOTHROTTLE_TARGET_CONCURRENCY = 100
# AUTOTHROTTLE_START_DELAY = 0
# AUTOTHROTTLE_MAX_DELAY = 0