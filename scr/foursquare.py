from functools import reduce
import operator
import requests
import json
from dotenv import load_dotenv
import os
import pandas as pd
import scr.foursquare as f
load_dotenv()


url_query = 'https://api.foursquare.com/v2/venues/explore'

tok1 = os.getenv("tok1")
tok2 = os.getenv("tok2")

def geoquery(city, tok1, tok2, coord):

    city = {'type': 'Point', 'coordinates': coord}
    url_query = 'https://api.foursquare.com/v2/venues/explore'
    parametros = {
       "client_id": tok1,
       "client_secret": tok2,
       "v": "20180323",
       "ll": f"{city.get('coordinates')[0]},{city.get('coordinates')[1]}",
       "query": "starbucks", 
       "limit": 170
    }
    resp = requests.get(url= url_query, params = parametros).json()

def getFromDict(diccionario,mapa):
    return reduce(operator.getitem,mapa,diccionario)

