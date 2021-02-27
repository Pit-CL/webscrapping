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

###############################################################################
# Abriendo la página.
###############################################################################
# Indico la URL y cargo el driver para la manipulación de la página.
url = 'https://jetsmart.com/cl/es/'
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    '/home/rafaelfarias/Dropbox/Postgrados/MDS/Almacenamiento_y_captura_de_datos/Tarea_WebScrapping/chromedriver')
driver.implicitly_wait(20)
driver.get(url)

###############################################################################
# Cerrando el pop up.
###############################################################################
# Se hace click en el no gracias para cerrar ese "pop-up"
cerrar = driver.find_element_by_id("onesignal-slidedown-cancel-button")
cerrar.click()

###############################################################################
# Ingresando los datos de búsqueda
###############################################################################
# Una vez cerrado el pop up que aparece debo revisar la clase de origen y
# destino.
origen = driver.find_element_by_class_name("dg-dummy")
destino = driver.find_element_by_class_name("dg-dummy")

# Hago click en el campo origen
sleep(3)
origen.click()
origen.send_keys("Santiago (SCL)")

# Del menú desplegable selecciono Santigo (SCL)
sleep(3)
click_origen = driver.find_element_by_class_name("dg-typing-results-list-item")
click_origen.click()

# Ahora hago click en destino
sleep(3)
click_destino =\
    driver.find_element_by_xpath(
        "/html/body/div[1]/main/div[2]/searchbox/div/div/div[1]/div/form/route-selector/div[2]/div[3]/ul/li[2]")
click_destino.click()

# Ahora debo ingresar la fecha. Primero que click en la flecha para correr el
# mes.
sleep(3)
click_flecha = driver.find_element_by_xpath(
    "/html/body/div[1]/main/div[2]/searchbox/div/div/div[1]/div/form/date-selector/div[3]/div[2]/div/div[1]/span[2]")
click_flecha.click()

# Ahora selecciona el primer día del intervalo de fecha.
sleep(3)
click_fecha_in = driver.find_element_by_xpath(
    "/html/body/div[1]/main/div[2]/searchbox/div/div/div[1]/div/form/date-selector/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/span[4]")
click_fecha_in.click()

# Ahora selecciono el último día del intervalo.
sleep(3)
click_fecha_fin = driver.find_element_by_xpath(
    "/html/body/div[1]/main/div[2]/searchbox/div/div/div[1]/div/form/date-selector/div[4]/div[2]/div/div[2]/div/div[2]/div[1]/span[33]")
click_fecha_fin.click()

# Ahora le doy click al botón buscar.
sleep(3)
click_buscar = driver.find_element_by_xpath(
    "/html/body/div[1]/main/div[2]/searchbox/div/div/div[1]/div/form/div[2]/button[2]")
click_buscar.click()

###############################################################################
# Extrayendo la información solicitada.
###############################################################################
# El viaje redondo se analizará utilizando el día de inicio del viaje como el
# día Jue 01-04 y todas las posibles vueltas dentro del mes.

# TODO: Ahora debo tratar de hacer un loop que recorra todos los precios y fechas.

precio_ida = []
precio_vuelta = []
fecha_ida = []
fecha_regreso = []

elemento_1 = driver.find_elements_by_xpath("/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[1]/div/div[1]/ul/li[4]/span[2]")
for e in elemento_1:
    precio_ida.append(e.text)

elemento_2 = driver.find_elements_by_xpath("/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-itinerary/div/div[1]/div[4]")
for c in elemento_2:
    fecha_regreso.append(c.text)


elemento_3 = driver.find_elements_by_xpath("/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/ul/li[4]/span[2]")
for a in elemento_3:
    precio_vuelta.append(a.text)

elemento_4 = driver.find_elements_by_xpath("/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-itinerary/div/div[1]/div[2]")
for d in elemento_4:
    fecha_ida.append(d.text)

# Loops que me permite obtener todos los datos de partida.
for elem in driver.find_elements_by_xpath("/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[1]/div/div[1]"):
    print(elem.text)

# Ahora le doy click a siguiente.
sleep(3)
click_siguiente = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[1]/div/div[1]/div[2]/i")
click_siguiente.click()

# Loop que me permite obtener todos los datos de llegada.
for elem2 in driver.find_elements_by_xpath("/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]"):
    print(elem2.text)



# TODO: ver como puedo trabajar con el texto para pasarlo a df.







# extraigo elementos de resultados de consulta e imprimo
# elems = driver.find_elements_by_class_name("week-selector.open")
# for e in elems:
#     try:
#         print(e.find_element_by_tag_name('span').text)
#         print()
#     except:
#         print("No encontré elementos")
#         print()


# https://stackoverflow.com/questions/37732649/scrapy-loop-xpath-selector-escaping-object-it-is-applied-to-and-returning-all
# def parse(self, response):
#     hxs = Selector(response)
#     split_url = response.url.split("/")
#     listings = hxs.xpath("//div[contains(@class,'listing-item')]")
#     for vehicle in listings:
#         item = Vehicle()
#         item['make'] = split_url[5]
#         item['price'] = vehicle.xpath(".//div[contains(@class,'price')]/text()").extract()
#         item['description'] = vehicle.xpath(".//div[contains(@class,'title-module')]/h2/a/text()").extract()
#         yield item

# https://medium.com/analytics-vidhya/what-if-selenium-could-do-a-better-job-than-your-travel-agency-5e4e74de08b0

from selenium.webdriver.support.ui import Select

# From Date
# date_picker_from_xpath = '//*[contains(@id, "dateRangeInput-display-start-inner")]'
# from_date_click_xpath = '//div[contains(@id, "depart")]'
# from_date_text_xpath = '//div[contains(@id, "depart-input")]'
# from_flexible_xpath = '//select[contains(@id, "datePicker-plusMinusThreeDepart-select")]'
# departure_date = '05/08/2021'
# driver.find_element_by_xpath(date_picker_from_xpath).click()
# sleep(1)
# driver.find_element_by_xpath(from_date_click_xpath).click()
# driver.find_element_by_xpath(from_date_text_xpath).clear()
# driver.find_element_by_xpath(from_date_text_xpath).send_keys(departure_date)
#
# # Add flexible date option +/- 3days
# Select(driver.find_element_by_xpath(from_flexible_xpath)).select_by_value('plusminusthree')
# sleep(1)
#
# # To Date
# to_date_text_xpath = '//div[contains(@id, "return-input")]'
# to_flexible_xpath = '//select[contains(@id, "datePicker-plusMinusThreeReturn-select")]'
# returning_date = '13/08/2021'
# driver.find_element_by_xpath(to_date_text_xpath).clear()
# sleep(1)
# driver.find_element_by_xpath(to_date_text_xpath).send_keys(returning_date)
# sleep(1)
#
# # Add flexible date option +/- 3days
# Select(driver.find_element_by_xpath(to_flexible_xpath)).select_by_value('plusminusthree')
#
# # Click the submit button to launch the search
# submit_button_xpath = '//button[contains(@id, "submit")]'
# driver.find_element_by_xpath(submit_button_xpath).click()