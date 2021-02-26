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
fecha_ida = ['Jue 01-04']
fecha_regreso = []

elemento_1 = driver.find_elements_by_xpath("/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[1]/div/div[1]/ul/li[4]/span[2]")
for e in elemento_1:
    precio_ida.append(e.text)

elemento_2 = driver.find_elements_by_xpath("/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/ul/li[4]/span[2]")
for a in elemento_2:
    precio_vuelta.append(a.text)

# extraigo elementos de resultados de consulta e imprimo
elems = driver.find_elements_by_class_name("week-selector.open")
for e in elems:
    try:
        print(e.find_element_by_tag_name('span').text)
        print()
    except:
        print("No encontré elementos")
        print()

