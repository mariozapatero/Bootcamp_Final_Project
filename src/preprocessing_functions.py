import spacy

from nltk.corpus import stopwords
from spacy.lang.en.stop_words import STOP_WORDS

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def preprocessing(string):
    
    tokenized_string = word_tokenize(string)
    
    tokens = []
    
    for token in tokenized_string:
        if token not in list(STOP_WORDS) and token not in list(stopwords.words('english')):
            tokens.append(lemmatizer.lemmatize(token))
    
    return tokens