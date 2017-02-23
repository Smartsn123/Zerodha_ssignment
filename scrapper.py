from bs4 import BeautifulSoup as BS
import redis
import json
import requests
import urllib2
import pandas as pd
import json
import webbrowser
import time

#Parse json data from the URL
def parse_URL(url):
	
    #mimick the request as browser to have the access permission
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
    
    req=urllib2.Request(url, headers=hdr)
    response = urllib2.urlopen(req)
    table=json.loads(response.read())['data']
    return table


def push_to_redis(data):
	r = redis.StrictRedis(host='localhost', port=6379, db=0)
	r.delete('nifty_data')
	print r.rpush('nifty_data',json.dumps(data))


def scrape():
	site= "https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json"
	data = parse_URL(site)
	print data
	push_to_redis(data)

def worker():
  while 1 :
    try :
      scrape()
      time.sleep(30000)
    except:
      time.sleep(10000)

