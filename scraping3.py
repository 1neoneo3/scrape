# -*- coding: utf_8 -*-
import time
import json
import re
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# connection.execute('set max_allowed_packet=67108864')
# connection.connect()
chrome_options = Options()

# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--user-data-dir=tmp')
# chrome_options.add_argument('--enable-logging')
# chrome_options.add_argument('--dump-dom')
# chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--headless')

chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument('--log-level=OFF')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-application-cache')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--verbose")

chrome_options.add_argument('--disable-browser-side-navigation')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--ignore-certificate-errors-spki-list')
# chrome_options.add_argument('--ignore-ssl-errors')
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = chrome_options)

main_url = "https://www.fxprime.com/market/list/rate.html"
driver.get(main_url)

# Getting individual cities url
soup = BeautifulSoup(driver.page_source, 'html.parser')

dt = soup.find("caption").getText()
dt = dt.split()
real_dt = dt[0]

tbody = soup.find("tbody")
trs = tbody.findAll("tr")

# print(trs)
print("=====================================================")
for tr in trs:
	tds = tr.findAll('td')
	currency = tds[0].getText()
	rate = tds[3].getText()

	if currency == "米ドル/円":		
		print(real_dt + " " + currency + " " + rate)
	if currency == "ポンド/円":
		print(real_dt + " " + currency + " " + rate)
	if currency == "豪ドル/円":
		print(real_dt + " " + currency + " " + rate)