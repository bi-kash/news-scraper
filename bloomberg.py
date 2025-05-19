import warnings
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from selenium.common.exceptions import NoSuchElementException 
import re
import requests


# Need these: shop_name,language,year,brand,modell,condition,category_shop,stock_status,stock_text,stock_sizes,url-detail,price,rrp
def get_driver():
    chromeOptions = webdriver.ChromeOptions()

    # Headless is faster. If headless is False then it opens a browser and you can see action of web driver. You can try making it False
    chromeOptions.headless = False
    chromeOptions.add_argument("--log-level=3")

    # installs chrome driver automatically if not present
    s = Service(ChromeDriverManager().install())
    # chromeOptions.add_argument("user-data-dir=/home/bikash/.config/google-chrome/Profile 1")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chromeOptions
    )
    return driver

sitemap_index_url = "https://www.bloomberg.com/feeds/bbiz/sitemap_index.xml"
response = requests.get(sitemap_index_url)
soup = BeautifulSoup(response.content, "xml")

sitemap_urls = [loc.text for loc in soup.find_all("loc")]

#driver = webdriver.Chrome()
driver = get_driver()
driver.get(sitemap_urls[0])
soup1 = BeautifulSoup(driver.page_source, "xml")
urls = [loc1.text for loc1 in soup1.find_all("loc")]

driver.get(urls[0])
driver
time.sleep(5)
a=driver.title

soup2 = BeautifulSoup(driver.page_source, "html")
title=soup2.find("h3").text
time=soup2.find("p").text

import pandas as pd
data=pd.DataFrame([{"Title":title,
                  "Time":time}])
                  
data.to_json("news10.json")