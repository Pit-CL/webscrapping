from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from random import randint
from time import sleep, strftime
import re
import pandas as pd
import numpy as np

origin = 'SCL'
destination = 'ARI'
startdate = '2021-04-01'
enddate = '2021-04-30'

url = 'https://jetsmart.com/cl/es/'
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    '/home/rafaelfarias/Dropbox/Postgrados/MDS/Almacenamiento_y_captura_de_datos/Tarea_WebScrapping/chromedriver')
driver.implicitly_wait(40)
driver.get(url)

# TODO: Debo primero rellenar los campos con la info solicitada.


# Buscando las clases en las que hay interés y llamando todos los "span".
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Busco input para la búsqueda.
elem = driver.find_element_by_class_name('dg - city - selector - list ps')
# elem.clear()
# elem.send_keys('SCL')

# Aprieto enter
# elem.send_keys(Keys.RETURN)

# Evitar los pop-ups.
caps = DesiredCapabilities.CHROME
caps["chromeOptions"] = {}
caps["chromeOptions"]["excludeSwitches"] = ["disable-popup-blocking"]


inputs = soup.find_all('span')
# arrtimes = soup.find_all('span', attrs={'class': 'dg - location - selector'})
# meridies = soup.find_all('span', attrs={'class': 'time-meridiem meridiem'})

# deptime = []
# for div in deptimes:
#     deptime.append(div.getText()[:-1])

# arrtime = []
# for div in arrtimes:
#     arrtime.append(div.getText()[:-1])

# meridiem = []
# for div in meridies:
#     meridiem.append(div.getText())

# deptime = np.asarray(deptime)
# deptime = deptime.reshape(int(len(deptime) / 2), 2)

# arrtime = np.asarray(arrtime)
# arrtime = arrtime.reshape(int(len(arrtime) / 2), 2)

# meridiem = np.asarray(meridiem)
# meridiem = meridiem.reshape(int(len(meridiem) / 4), 4)
