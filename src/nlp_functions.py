from textblob import TextBlob

def blob_scoring(token):
    text = TextBlob(' '.join(token))
    return text.sentiment.polarity



from nltk.sentiment.vader import SentimentIntensityAnalyzer

vader = SentimentIntensityAnalyzer()

def vader_scoring(token):     # VADER ejecuta el análisis sobre strings, por lo que convertimos los tokens en una única string.
    return(vader.polarity_scores(' '.join(token))) 