###############################################################################
# Se importan las librerías necesarias
###############################################################################
import collections

import tweepy
from credentials import *  # This will allow us to use the keys as variables
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import string
import re
from nltk.corpus import stopwords
from nltk import word_tokenize
import nltk
import itertools
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

nltk.download('stopwords')

###############################################################################
# API
###############################################################################
consumer_key = 'V2NQxXmZPCAQVtsECjLedJDY4'
consumer_secret = 'KjyjaFdCUlxDy2Oj0o7aqihIxvERHFrW4Hy9122eJJC2pZ6TFz'
access_token = '1322018135537520640-JXb5lZMnFb8DH2Evp6CA2vTcrHw9u8'
access_token_secret = 'TSoqCk7qbAIGJgCD8jJTCrnXNuTAgob2q8LxBFmygq17g'


# Seteando la API:
def twitter_setup():
    # Llaves de autenticación.:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Devuelve API autenticado:
    api = tweepy.API(auth)
    return api


###############################################################################
# Extracción de tweets
###############################################################################
# Se crea el objeto que extraerá la info:
extractor = twitter_setup()

# Se crea la lista de tweets:
tweets = tweepy.Cursor(extractor.user_timeline,
                       screen_name="DFinanciero").items(10)

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
df_tweets['Tweets'] = df_tweets['Tweets']. \
    map(lambda x: clean_text(x))

# Lista de todas las palabras.
palabras_todas = list(itertools.chain(*df_tweets['Tweets']))

# Se crea el contador de palabras
cuenta_palabras = collections.Counter(palabras_todas)

# Se crea el df que contiene las palabras.
df_palabras = pd.DataFrame(cuenta_palabras.most_common(5),
                           columns=['palabras', 'cantidad'])

# Se grafica.
fig, ax = plt.subplots(figsize=(14, 14))

# Gráfico horizontal.
df_palabras.sort_values(by='cantidad').plot.barh(x='palabras',
                                                 y='cantidad',
                                                 ax=ax,
                                                 color="purple")

ax.set_title("Palabras más comunes encontradas en los tweets del Diario")
plt.show()

###############################################################################
# Extracción de seguidos por el Diario Financiero.
###############################################################################
# Se crea el objeto que extraerá los seguidos:
extractor2 = twitter_setup()

# Se listan los amigos:

amigos = tweepy.Cursor(extractor2.friends,
                       screen_name='DFinanciero').items(10)

# Se crea el df_amigos.
df_amigos = pd.DataFrame(data=[friends.name for friends in amigos],
                         columns=['amigos'])

# TODO: Debo hacer un loop con la info como lo de abajo que sea capaz
# TODO: de recorrer los 100 nombres y sacar los tweets.

lista_de_amigos = df_amigos['amigos'].tolist()
# Se crea la lista de tweets:
for tweets2 in lista_de_amigos:
    tweets2 = tweepy.Cursor(extractor2.user_timeline,
                            screen_name=amigos).items(10)
    print(tweets2)

# Se crea el df:
df_tweets_amigos = pd.DataFrame(data=[tweet.text for tweet in tweets2],
                                columns=['Tweets'])

for amigos in lista_de_amigos:
    print(amigos)
