def percents(x, y):
    """ Определение процента x от y"""
    oneprc = x/100
    result = y/oneprc
    return int(result)


def print_prc(x, y):
    print(str(y) + " составляет " + str(percents(x, y))+" процентов от "+ str(y))

print_prc(200,50)