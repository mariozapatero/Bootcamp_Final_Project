import re

# Lista de palabras relacionadas con el atributo de marca 'precio'.

price_list = ['ackers', 'affordable', 'banknote', 'bargain', 'bill', 'bill', 'boodle', 'brass', 'brass', 'bread',
              'buck', 'budget', 'capital', 'carfare', 'cash', 'cent', 'charge', 'cheap', 'coin', 'competitive', 'copper',
              'cost', 'cost', 'currency', 'damage', 'dibs', 'dime', 'dinero', 'discount', 'dollar', 'dosh', 'dough',
              'ducats', 'economic', 'economy', 'euro', 'expenditure', 'expense', 'expensive', 'fare', 'fee', 'fraud',
              'funds', 'gelt', 'gold', 'gravy', 'greenbacks', 'invoice', 'levy', 'lolly', 'loot', 'lucre', 'mazuma',
              'means', 'monetary', 'money', 'money', 'moolah', 'note', 'noting', 'oof', 'outlay', 'pay', 'pence', 'penny',
              'plonk', 'plunder', 'plunk', 'price', 'pricy', 'quotation', 'rate', 'rhino', 'rich', 'rob', 'sale',
              'settlement', 'shekels', 'silver', 'simoleons', 'smacker', 'splosh', 'spondulicks', 'steal', 'sterling',
              'sum', 'terms', 'theft', 'thievery', 'toll', 'valuation', 'value', 'wherewithal', 'wonga', 'worthy']


def data_groups(string):    # Función para definir el atributo de marca al que hace refencia el tweet.
                            # Este es el nivel más básico con 'price' y 'quality' como únicos atributos.
    matches = []

    for word in price_list:
        matches.append(word in string)

    if True in matches:
        return 'price'
    
    else:
        return 'quality'




def extract_hashtags(string): # Queremos extraer los hashtags de los tweets y almacenarlos en una nueva columna.
                              # Realmente no es una función de limpieza como tal, pero debemos hacerlo antes de limpiar los datos (eliminaremos #).
    hashtags = re.findall('#[^\s]*', string)   # Generamos una lista con todos los hashtags del tweet (si no hay # nos devuelve lista vacía).
    return hashtags           # Esta nueva columna de hashtags nos servirá para análisis de los hashtags a posteriori.

