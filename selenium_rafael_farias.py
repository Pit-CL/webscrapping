###############################################################################
# IMPORTANDO LAS LIBRERÍAS NECESARIAS.
###############################################################################


from selenium_rafael_farias import webdriver
from time import sleep, strftime
import re
import pandas as pd
from sqlalchemy import create_engine


###############################################################################
# ABRIL: ABRIENDO LA PÁGINA.
###############################################################################


# Indico la URL y cargo el driver para la manipulación de la página.
url = 'https://jetsmart.com/cl/es/'
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    '/home/rafaelfarias/Dropbox/Postgrados/MDS/Almacenamiento_y_captura_de_datos/Tarea_WebScrapping/chromedriver')
driver.implicitly_wait(20)
driver.get(url)

###############################################################################
# ABRIL: CERRANDO EL POP-UP.
###############################################################################


# Se hace click en el no gracias para cerrar ese "pop-up"
cerrar = driver.find_element_by_id("onesignal-slidedown-cancel-button")
cerrar.click()


###############################################################################
# ABRIL: INGRESANDO LOS DATOS DE BÚSQUEDA.
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
# ABRIL: EXTRAYENDO PRECIOS Y FECHAS IDA Y VUELTA.
###############################################################################


# El viaje redondo se analizará utilizando el día de inicio del viaje como el
# día Jue 01-04 y todas las posibles vueltas dentro del mes, excluyendo como
# retorno el día 01-04.
sleep(3)
# Loop que me permite obtener todos los datos de llegada de la página 1
for elem1 in driver.find_elements_by_xpath(
        "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]"):
    elem1 = elem1.text

# Repito el proceso 6 para cambiar de datos y repito 5 veces el proceso para
# obtener los 30 días del mes de Abril
# Proceso 1 de 5
click_anterior = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/div[1]/i")
click_anterior.click()
sleep(2)
click_anterior = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/div[1]/i")
click_anterior.click()
sleep(2)
click_anterior = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/div[1]/i")
click_anterior.click()
sleep(2)
click_anterior = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/div[1]/i")
click_anterior.click()
sleep(2)
click_anterior = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/div[1]/i")
click_anterior.click()
sleep(2)
click_anterior = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/div[1]/i")
click_anterior.click()
sleep(2)

for elem2 in driver.find_elements_by_xpath(
        "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]"):
    elem2 = elem2.text
sleep(5)

# Proceso 2 de 5
click_anterior = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/div[1]/i")
click_anterior.click()
sleep(2)

click_anterior = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/div[1]/i")
click_anterior.click()
sleep(2)
click_anterior = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/div[1]/i")
click_anterior.click()
sleep(2)
click_anterior = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/div[1]/i")
click_anterior.click()
sleep(2)
click_anterior = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/div[1]/i")
click_anterior.click()
sleep(2)
click_anterior = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/div[1]/i")
click_anterior.click()
sleep(2)

for elem3 in driver.find_elements_by_xpath(
        "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]"):
    elem3 = elem3.text
sleep(3)

# Proceso 3 de 5
click_anterior = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/div[1]/i")
click_anterior.click()
sleep(2)
click_anterior = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/div[1]/i")
click_anterior.click()
sleep(2)
click_anterior = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/div[1]/i")
click_anterior.click()
sleep(2)
click_anterior = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/div[1]/i")
click_anterior.click()
sleep(2)
click_anterior = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/div[1]/i")
click_anterior.click()
sleep(2)
click_anterior = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/div[1]/i")
click_anterior.click()
sleep(2)

for elem4 in driver.find_elements_by_xpath(
        "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]"):
    elem4 = elem4.text
sleep(3)

# Proceso 4 de 5
click_anterior = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/div[1]/i")
click_anterior.click()
sleep(2)
click_anterior = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/div[1]/i")
click_anterior.click()
sleep(2)
click_anterior = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/div[1]/i")
click_anterior.click()
sleep(2)
click_anterior = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/div[1]/i")
click_anterior.click()
sleep(2)
click_anterior = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/div[1]/i")
click_anterior.click()
sleep(2)
click_anterior = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/div[1]/i")
click_anterior.click()
sleep(2)

for elem5 in driver.find_elements_by_xpath(
        "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]"):
    elem5 = elem5.text
sleep(3)

# Proceso 5 de 5
click_anterior = driver.find_element_by_xpath(
    "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]/div[1]/i")
click_anterior.click()
sleep(2)
for elem6 in driver.find_elements_by_xpath(
        "/html/body/app/div[1]/div[2]/div/section/div/flight/div/div/flight-select-form/div/form[1]/div[1]/section/flight-fee-selector[2]/div/div[1]"):
    elem6 = elem6.text
sleep(3)

###############################################################################
# GENERANDO UN DATAFRAME CON LA DATA EXTRAÍDA.
###############################################################################


# Limpio un poco la data.
elem1 = re.sub('\n', ',', elem1)
elem2 = re.sub('\n', ',', elem2)
elem3 = re.sub('\n', ',', elem3)
elem4 = re.sub('\n', ',', elem4)
elem5 = re.sub('\n', ',', elem5)
elem6 = re.sub('\n', ',', elem6)

# Creo la lista con todos los elementos extraídos.
bd = [elem1, elem2, elem3, elem4, elem5, elem6]


b1_1 = (bd[0][4:18]).split(',')
b1_2 = (bd[1][4:18]).split(',')
b1_3 = (bd[2][4:18]).split(',')
b1_4 = (bd[3][4:18]).split(',')
b1_5 = (bd[4][4:18]).split(',')
b1_6 = (bd[5][4:18]).split(',')
b2_1 = (bd[0][23:37]).split(',')
b2_2 = (bd[1][23:37]).split(',')
b2_3 = (bd[2][23:37]).split(',')
b2_4 = (bd[3][23:37]).split(',')
b2_5 = (bd[4][23:37]).split(',')
b2_6 = (bd[5][23:37]).split(',')
b3_1 = (bd[0][42:56]).split(',')
b3_2 = (bd[1][42:56]).split(',')
b3_3 = (bd[2][42:56]).split(',')
b3_4 = (bd[3][42:56]).split(',')
b3_5 = (bd[4][42:56]).split(',')
b3_6 = (bd[5][42:56]).split(',')
b4_1 = (bd[0][61:75]).split(',')
b4_2 = (bd[1][61:75]).split(',')
b4_3 = (bd[2][61:75]).split(',')
b4_4 = (bd[3][61:75]).split(',')
b4_5 = (bd[4][61:75]).split(',')
b4_6 = (bd[5][61:75]).split(',')
b5_1 = (bd[0][80:94]).split(',')
b5_2 = (bd[1][80:94]).split(',')
b5_3 = (bd[2][80:94]).split(',')
b5_4 = (bd[3][80:94]).split(',')
b5_5 = (bd[4][80:94]).split(',')
b5_6 = (bd[5][80:94]).split(',')
b6_1 = (bd[0][99:116]).split(',')
b6_2 = (bd[1][99:116]).split(',')
b6_3 = (bd[2][99:116]).split(',')
b6_4 = (bd[3][99:116]).split(',')
b6_5 = (bd[4][99:116]).split(',')
b6_6 = (bd[5][99:116]).split(',')

bd_fechas_precios = [b1_1, b1_2, b1_3, b1_4, b1_5, b1_6,
                     b2_1, b2_2, b2_3, b2_4, b2_5, b2_6,
                     b3_1, b3_2, b3_3, b3_4, b3_5, b3_6,
                     b4_1, b4_2, b4_3, b4_4, b4_5, b4_6,
                     b5_1, b5_2, b5_3, b5_4, b5_5, b5_6,
                     b6_1, b6_2, b6_3, b6_4, b6_5, b6_6]

# Creo la base de datos.
df_precios = pd.DataFrame(bd_fechas_precios, columns=(['Fecha_regreso',
                                                       'Precio']))

# Hay algunos valores que están duplicados y son eliminados.
df_precios.drop_duplicates(subset=['Fecha_regreso'], inplace=True)

# Ordeno las fechas de menor a mayor.
df_precios.sort_values(by='Fecha_regreso', inplace=True, ascending=True,
                       ignore_index=True)

# Elimino datos que no corresponden al mes.
df_precios.drop([0, 2], axis=0, inplace=True)


# Como la fecha de Ida es el 01-04 para todos los regresos, sólo se analizará
# la tarifa de retorno para determinar la tarifa más barata.


# Se crea la base de datos SQL.
engine = create_engine(
    'sqlite:////home/rafaelfarias/Dropbox/Postgrados/MDS/Almacenamiento_y_captura_de_datos/Tarea_WebScrapping/data/tarea2.db',
    echo=False)
connection = engine.raw_connection()
df_precios.to_sql('precios_fechas', connection, index=False)

# Realizo la consulta para obtener el valor mínimo. Que en combinación con el
# valor de IDA siempre dará el mínimo valor del viaje completo.
consulta = pd.read_sql("SELECT MIN(Precio) AS minimum  FROM precios_fechas",
                       connection)

# Ahora traigo todos los días con el valor mínimo que sumado al día de IDA
# siempre se obtendrá el total ida y vuelta menor.
consulta2 = pd.read_sql("SELECT * FROM precios_fechas WHERE (Precio) = (SELECT MIN(Precio) FROM precios_fechas)",
                        connection)

