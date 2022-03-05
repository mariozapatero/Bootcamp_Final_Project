import tweepy
import config
import json
import time

# Credenciales (cliente):

def getClient():

    client = tweepy.Client(bearer_token = config.BEARER_TOKEN,
                           consumer_key = config.API_KEY,
                           consumer_secret = config.API_KEY_SECRET,
                           access_token = config.ACCESS_TOKEN,
                           access_token_secret = config.ACCESS_TOKEN_SECRET,
                           wait_on_rate_limit = True)
    return client


# Extracción de tweets:

'''Primero ejecutamos 'single_searchTweets' para tener el punto de partida
(nos devuelve lista de diccionarios con los datos de los primeros 100 tweets y el next_token de esta primera búsqueda).

Después utilizamos la función 'all_searchTweets'.
Partimos del next_token que hemos obtenido anteriormente y añadimos los datos a la lista de diccionario.
Obtenemos una lista con los datos de todos los tweets de la ultima semana (que cumplen la query).'''

def single_searchTweets(query):

    client = getClient()

    tweets = client.search_recent_tweets(query=query, max_results=100,
                                         tweet_fields = ['id','text','created_at','author_id'])

    tweet_data = tweets.data

    results = []

    if tweet_data != None and len(tweet_data)>0:
        for tweet in tweet_data:
            obj = {}
            obj['id'] = tweet.id
            obj['text'] = tweet.text
            obj['date'] = tweet.created_at
            obj['author_id'] = tweet.author_id
            results.append(obj)
    
    else:
        return []
        print("No matching tweets found")
    

    return results, tweets.meta['next_token']    # Nos devuelve los parámetros de entrada para all_searchTweets().



def all_searchTweets(query, token):

    client = getClient()

    tweets = client.search_recent_tweets(query=query, max_results=100, next_token = token,
                                         tweet_fields = ['id','text','created_at','author_id'])

    tweet_data = tweets.data

    results = []

    if tweet_data != None and len(tweet_data)>0:
        for tweet in tweet_data:
            obj = {}
            obj['id'] = tweet.id
            obj['text'] = tweet.text
            obj['date'] = tweet.created_at
            obj['author_id'] = tweet.author_id
            results.append(obj)
    
    else:
        print("No matching tweets found")
    

    try:
        return results, tweets.meta['next_token']

    except:
        return results
        print('No next_token avaliable: query copleted.')


##################################################
'''
La manera de utilizar las dos funciones anteriores para combinarlar y obtener lo que queremos es la siguiente:

query_results = single_searchTweets('nike -is:retweet lang:en')[0]
token = single_searchTweets('nike -is:retweet lang:en')[1]

while len(query_results) < 'nº de tweets deseados':
    query = all_searchTweets('nike -is:retweet lang:en', token)
    query_results += query[0]
    token = query[1]
    '''
##################################################



def searchAll(query):     # SOLO podemos utilizarlo con Academic Access.

    client = getClient()
    all_tweets = []

    for response in tweepy.Paginator(client.search_all_tweets,
                                     query = query,
                                     tweet_fields = ['id', 'text', 'created_at'],
                                     start_time = '2021-01-01T00:00:01Z',
                                     end_time = '2021-12-31T23:59:59Z',
                                     max_results = 10):
        all_tweets.append(response)




# Funciones de prueba (no utilizadas finalmente al haber construido otras más eficientes).


'''
def searchTweets(query):

    client = getClient()

    results = []

    for tweet in tweepy.Paginator(client.search_recent_tweets,
                                     query = query,
                                     tweet_fields = ['id', 'text', 'created_at'],
                                     max_results = 10):
        
        tweet_data = tweet.data

        if tweet_data != None and len(tweet_data)>0:
            for tweet in tweet_data:
                obj = {}
                obj['id'] = tweet.id
                obj['text'] = tweet.text
                obj['date'] = tweet.created_at

                time.sleep(1)

                results.append(obj)
                
        else:
            return []
            print("No matching tweets found")

    return results



def getTweets(query):

    client = getClient()
    
    tweets = []

    for response in tweepy.Paginator(client.search_recent_tweets,
                                     query = query,
                                     user_fields = ['username', 'public_metrics', 'location'],
                                     tweet_fields = ['created_at', 'geo', 'public_metrics', 'text'],
                                     max_results = 100,
                                     start_time = '2022-02-24T20:00:00Z'):
                                     
        time.sleep(1)

        tweets.append(response)

        return tweets





def get_more_tweets(query, next):   # Añadimos next_token para obtener todos los tweets de manera automática.

    client = getClient()
    
    tweets = []

    for response in tweepy.Paginator(client.search_recent_tweets,
                                     query = query,
                                     user_fields = ['username', 'public_metrics', 'location'],
                                     tweet_fields = ['created_at', 'geo', 'public_metrics', 'text'],
                                     max_results = 100,
                                     next_token = next):

        time.sleep(1)

        tweets.append(response)

        return tweets
'''