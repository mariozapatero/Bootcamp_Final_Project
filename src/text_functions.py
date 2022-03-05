# Lista de palabras relacionadas con el atributo de marca 'precio'.

price_list = ['ackers', 'affordable', 'banknote', 'bargain', 'bill', 'bill', 'boodle', 'brass', 'brass', 'bread',
              'buck', 'budget', 'capital', 'carfare', 'cash', 'cent', 'charge', 'cheap', 'coin', 'competitive', 'copper',
              'cost', 'cost', 'currency', 'damage', 'dibs', 'dime', 'dinero', 'discount', 'dollar', 'dosh', 'dough',
              'ducats', 'economic', 'economy', 'euros', 'expenditure', 'expense', 'expensive', 'fare', 'fee', 'fraud',
              'funds', 'gelt', 'gold', 'gravy', 'greenbacks', 'invoice', 'levy', 'lolly', 'loot', 'lucre', 'mazuma',
              'means', 'monetary', 'money', 'money', 'moolah', 'note', 'noting', 'oof', 'outlay', 'pay', 'pence', 'penny',
              'plonk', 'plunder', 'plunk', 'price', 'pricy', 'quotation', 'rate', 'rhino', 'rich', 'rob', 'sale',
              'settlement', 'shekels', 'silver', 'simoleons', 'smacker', 'splosh', 'spondulicks', 'steal', 'sterling',
              'sum', 'terms', 'theft', 'thievery', 'toll', 'valuation', 'value', 'wherewithal', 'wonga', 'worthy']


def data_groups(string):

    matches = []

    for word in price_list:
        matches.append(word in string)

    if True in matches:
        return 'price'
    
    else:
        return 'quality'


