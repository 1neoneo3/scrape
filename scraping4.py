# -*- coding: utf_8 -*-
import time
import json
import re
import datetime
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

# chrome_options.add_argument("--disable-infobars")
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument('--log-level=OFF')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-application-cache')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--start-maximized')
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--verbose")

# chrome_options.add_argument('--disable-browser-side-navigation')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--ignore-certificate-errors-spki-list')
# chrome_options.add_argument('--ignore-ssl-errors')
# prefs = {"profile.managed_default_content_settings.images": 2}
# chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = chrome_options)



links = ["https://www.rakuten-sec.co.jp/web/market/data/usd.html","https://www.rakuten-sec.co.jp/web/market/data/gbp.html","https://www.rakuten-sec.co.jp/web/market/data/cad.html","https://www.rakuten-sec.co.jp/web/market/data/chf.html","https://www.rakuten-sec.co.jp/web/market/data/nzd.html","https://www.rakuten-sec.co.jp/web/market/data/aud.html"]
currencies = ["ドル円","ポンド円","カナダドル円","スイスフラン円","NZドル円","豪ドル円"]
output = []



for i in range(0,6):

	main_url = links[i]
	driver.get(main_url)
	iframe = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//iframe[@class='iframe-ms-01-01']")))
	driver.switch_to.frame(iframe)

	# Getting individual cities url
	soup = BeautifulSoup(driver.page_source, 'html.parser')

	table = soup.find("table", {"class":"tbl-data-01"})
	tbody = table.find("tbody")
	trs = tbody.findAll("tr")
	tr = trs[2]
	tds = tr.findAll('td')

	# print(tds)

	rate = tds[0].getText()
	dt = tds[1].getText()
	dt = dt.split("/")

	Y = datetime.datetime.now()
	m = ''.join([n for n in dt[0] if n.isdigit()])
	d = ''.join([n for n in dt[1] if n.isdigit()])

	real_dt = Y.strftime("%Y") + "-" + m + "-" + d

	output.append(real_dt + " " + currencies[i] + " " + rate)




print("==================================== 前日終値 ========================================")
for s in output:
	print(s)
