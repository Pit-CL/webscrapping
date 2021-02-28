###############################################################################
# Se importan las librerías necesarias
###############################################################################
import collections
import tweepy
import pandas as pd
import string
from nltk.corpus import stopwords
import nltk
import itertools
import matplotlib.pyplot as plt

nltk.download('stopwords')


###############################################################################
# API
###############################################################################
consumer_key = 'xxxxxx'
consumer_secret = 'xxxxxx'
access_token = 'xxxxxxx'
access_token_secret = 'xxxxxxxx'


# Seteando la API:
def twitter_setup():
    # Llaves de autenticación.:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Devuelve API autenticado:
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api


# Declaro usuario que usaré más adelante.
usuario_principal = 'DFinanciero'


###############################################################################
# Extracción de tweets
###############################################################################
# Se crea el objeto que extraerá la info:
extractor = twitter_setup()

# Se crea la lista de tweets:
tweets = tweepy.Cursor(extractor.user_timeline,
                       screen_name=usuario_principal).items(1000)

# Se crea el df:
df_tweets = pd.DataFrame(data=[tweet.text for tweet in tweets],
                         columns=['Tweets'])


###############################################################################
# Análisis de frecuencia de palabras.
###############################################################################
# Limpieza y Stopwords

def clean_text(text):
    # Removiendo la puntuación
    text = text.translate(string.punctuation)

    # Se lleva los tweets a minúscula y se tokenizan.
    text = text.lower().split()

    # Se eliminan los "stops words"
    stops = set(stopwords.words("spanish"))
    text = [w for w in text if not w in stops and len(w)]
    return text


# Se recorre toda la columna Tweets aplicando la función clean_text
df_tweets['Tweets'] = df_tweets['Tweets'].\
    map(lambda x:clean_text(x))

# Quedaron algunas palabras que hay que seguir limpiando.
stop = ['@presidencia_cl', '[vivo]', 'rt', 'pdte', '2', '@sebastianpinera',
        '@', '@presidencia_cl:', '@sebastianpinera,', '@gobiernodechile:',
        '-', 'of', 'q', '_', '+', 'e...', 'a...', 'de...', 's...', 'y.,.',
        'tras', 'd...', '[en', 'vivo]', 'x', '#lomásleído', '#dfmas',
        '|', '🔑#dffull', '#dffull', '$', '4', '5', 'us$', 'df', '🧫covid-19',
        'chile:', '24', 'si', 'tres', '2020']

df_tweets['Tweets'] = df_tweets['Tweets'].\
    map(lambda x:[item for item in x if item not in stop])

# Lista de todas las palabras.
palabras_todas = list(itertools.chain(*df_tweets['Tweets']))

# Se crea el contador de palabras
cuenta_palabras = collections.Counter(palabras_todas)

# Se crea el df que contiene las palabras.
df_palabras = pd.DataFrame(cuenta_palabras.most_common(100),
                           columns=['palabras', 'cantidad'])

# Se grafica.
fig, ax = plt.subplots(figsize=(14, 14))

# Gráfico horizontal.
df_palabras.sort_values(by='cantidad').plot.barh(x='palabras',
                                                 y='cantidad',
                                                 ax=ax,
                                                 color="purple")
ax.set_title("100 Palabras más comunes encontradas en los tweets de Piñera")
plt.show()


###############################################################################
# Extracción de seguidos por el Diario Financiero.
###############################################################################
# Se crea el objeto que extraerá los seguidos:
extractor2 = twitter_setup()

# Se listan los amigos:
amigos = tweepy.Cursor(extractor2.friends,
                       id=usuario_principal).items(100)

# Se crea el df_amigos.
df_amigos = pd.DataFrame(data=[friends.id for friends in amigos],
                         columns=['amigos'])

# Se crea la lista que nos permitirá iterar.
lista_de_amigos = df_amigos['amigos'].tolist()

# Loop para encontrar los 10 tweets de los 100 usuarios seguidos.
df_final = pd.DataFrame()
for i in range(0, 99):
    tweets = tweepy.Cursor(extractor2.user_timeline,
                           id=lista_de_amigos[i]).items(10)

    df_tweets_amigos = pd.DataFrame(data=[tweet.text for tweet in tweets],
                                    columns=['Tweets'])
    # df_final = df_tweets_amigos.append(df_tweets_amigos)
    df_final = df_final.append(df_tweets_amigos)

###############################################################################
# Análisis de frecuencia de palabras.
###############################################################################
# Limpieza y Stopwords
# Se recorre toda la columna Tweets aplicando la función clean_text
df_final['Tweets'] = df_final['Tweets'].\
    map(lambda x:clean_text(x))

# Quedaron algunas palabras que hay que seguir limpiando.
stop = ['@presidencia_cl', '[vivo]', 'rt', 'pdte', '2', '@sebastianpinera',
        '@', '@presidencia_cl:', '@sebastianpinera,', '@gobiernodechile:',
        '-', 'of', 'q', 'https://', 'https://t.co/yrxme7dw6k',
        'https://t.co/sj3fapuhdh', 'https://t.co/rjfmcwrkk1',
        'https://t.co/fzbheccdlx', 'https://t.co/biruccqpvb',
        'https://t.co/cpbsvugtyk', 'https://t.co/fgb36ictit',
        'https://t.co/rz8jaxf5uw', 'https://t.co/eofq7xmsed',
        '#sigamosaprendiendo', 'https://t.co/26g2tizxwd', '1.8',
        '2.092.453', 'hola,', '|', '@potus:', '5', 'd…', 'la...',
        'la…', '@vtrsoporte', 'a…', 'l…', '🙌🏻', '2021', 's.a.;',
        '#las3claves:', 'p…', '#fcab', '#dfmas', 'it’s', '@meconomia:',
        '&amp;', '#covid19', 'us', '@sodimacayuda', 'dm.']

df_final['Tweets'] = df_final['Tweets'].\
    map(lambda x:[item for item in x if item not in stop])


# Limpieza de stopwords en inglés.
def clean_text_english(text):
    # Se eliminan los "stops words"
    stops = set(stopwords.words("english"))
    text = [w for w in text if not w in stops and len(w)]
    return text


df_final['Tweets'] = df_final['Tweets'].\
    map(lambda x:clean_text_english(x))

# Lista de todas las palabras.
palabras_todas2 = list(itertools.chain(*df_final['Tweets']))

# Se crea el contador de palabras
cuenta_palabras2 = collections.Counter(palabras_todas2)

# Se crea el df que contiene las palabras.
df_palabras2 = pd.DataFrame(cuenta_palabras2.most_common(100),
                            columns=['palabras', 'cantidad'])

# Se grafica.
fig2, ax2 = plt.subplots(figsize=(14, 14))

# Gráfico horizontal.
df_palabras2.sort_values(by='cantidad').plot.barh(x='palabras',
                                                  y='cantidad',
                                                  ax=ax2,
                                                  color="purple")
ax2.set_title("100 Palabras más comunes encontradas en los tweets de amigos")
plt.show()
