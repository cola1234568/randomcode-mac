def rempunc(s: str): # noqa
    s = s.\
        replace(',', '').\
        replace('.', '').\
        replace('!', '').\
        replace('?', '').\
        replace('\"', '').\
        replace('\'', '')
    return s