
def upper_first_char(string):
    if isinstance(string, str):
       s = string[0:1].upper()
       string = s + string[1:]
    return string
if __name__ == '__main__':
    result = map(upper_first_char, ['adam', 'LISA', 'barT', 12232])
    print result
