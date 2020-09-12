# af-scraper

Scraper for Pandora Airlines website

How We scrape

<h5>1. execute bd_proxy_spider.sh </h5> 
We can run it 1/day or 1/hour independently
As a result config/good_proxy.txt includes proxies that answered us by 200
We use this list for future requests<br>
TODO: as a good decision - we can remake it into some db with 24/7 refreshing
<br>
<h5>2. execute direction_spider.sh </h5>
Receive all airports and routes.
As a result we have 
1)config/airports.json
There are config/airports_country.json file.
It is very important file where we divide all routes between countries.
I made it manually. TODO - reload this automatically from some correct wikies(?)

2)config/date_end.txt
this file contains last date flight/direction
it is nessesary for next spider to limit access for schedules
<br><br>
spider use file errors/error_direction_urls.txt for re-request /twice/ through list of urls
<br> 
<h5>3. execute schedule_spider.sh </h5>
Receive all schedules between airports till end dates
As a result we have config/schedule_flights.
We must know about schedule before we request prices.
<br>
<h5>4. execute main_spider.sh </h5>
Receive all prices for all schedules
Good answers move to config/*.flight
bad answers move to config/error.flights
<br>
<h5>5. execute bad_url_spider.py </h5>
Re-run answers from prev that have 404, 503 etc
from config/error.flights
<br> 
<h5>6. execute transfer.py </h5>
transfer all raw flights into client format
<br>