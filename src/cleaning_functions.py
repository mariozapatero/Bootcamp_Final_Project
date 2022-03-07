import pandas as pd
import re


def drop_duplicates(dataframe):
    return dataframe.drop_duplicates(inplace=True)




def extract_hashtags(string): # Queremos extraer los hashtags de los tweets y almacenarlos en una nueva columna.
                              # Realmente no es una función de limpieza como tal, pero debemos hacerlo antes de limpiar los datos (eliminaremos #).
    hashtags = re.findall('#[^\s]*', string)   # Generamos una lista con todos los hashtags del tweet (si no hay # nos devuelve lista vacía).
    return hashtags           # Esta nueva columna de hashtags nos servirá para análisis de los hashtags a posteriori.




def basic_cleaning(string):     #OJO QUE ES LA ANTIGUA!!!!
    
    string = re.sub('http[^\s]*\s', ' ', string)   # Quitamos urls (desde http hasta el siguiente espacio).
    
    string = re.sub('@[^\s]*\s', ' ', string)   # Eliminamos usuarios (desde @ hasta el siguiente espacio)

    numbers = {'1':' one', '2':' two', '3':' three', '4':' four', '5':' five',
               '6': ' six', '7':' seven', '8':' eight', '9':' nine', '0':' zero',
               '$':' dollars', '€':' euros'}    # Diccionario para sustituir los dígitos por el número escrito, '$' por 'dollar' y '€' por 'euro'.
                                              # Incluimos un espacio al principio para evitar problemas con otras transformaciones en la función.
    for number, word in numbers.items():
        string = string.replace(number, word)
    
    string = string.split(' ')    # Tratamos los hashtags como caso particular (a partir de aquí empieza su tratamiento).
    
    result = []                   # Generamos lista vacía para evitar problemas en el bucle (para qno eliminar elementos de la lista sobre la que iteramos).
    
    for e in string:              # Rellenamos la lista con todas las palabras del tweet para evitar errores en la función.
        if e != '':               # Descartando valores vacíos (los habrá si el tweet contiene más de un espacio seguido).
            result.append(e)     
    
    for index in range(len(result)):      # Queremos pasar de '#HelloWorld' a 'hello world', por ejemplo.
        if result[index][0] != '#':       # Descartamos los hashtags.
            result[index] = result[index].title()   #Ponemos la primera letra en mayúscula (podríamos usar capitalize()).
    
    result = ' '.join(result)     # Pasamos la lista a una única string (con la inicial de cada palabla en mayúscula).
    
    result = re.findall('[A-Z][a-z]*', result) # Cambiamos los hashtags a lo que queremos (separar palabras por mayúsculas).
                                               # Descartamos caracteres no alfabéticos (incluido '#').
                                               # Generamos una lista con las palabras (con inicial en mayúcula).
    for i in range(len(result)):
        result[i] = result[i].lower()          # Ponemos todas las balabras de la lista en minúscula.
        
    return ' '.join(result)       # Return de una única string separando los elementos de la lista por espacios.






# Función limpieza básica SIN TRATAMIENTO DE HASHTAGS:
'''
def basic_cleanning(string):
    
    hashtag_words = 
    
    string = string.lower().strip()     # Todo a minúsculas y quitamos espacios en los extremos.
    
    string = re.sub('http[^\s]*\s', ' ', string)   # Quitamos urls (desde http hasta el siguiente espacio).
    
    string = re.sub('@[^\s]*\s', ' ', string)   # Eliminamos usuarios (desde @ hasta el siguiente espacio)

    string = " ".join(re.findall('[a-z]+', string)) # Eliminamos todo lo que no sea una letra.

    return string
'''