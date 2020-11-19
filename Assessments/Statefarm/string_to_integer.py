


mapping = {}
mapping['zero'] = 0
mapping['one'] = 1
mapping['two'] = 2
mapping['three'] = 3
mapping['four'] = 4
mapping['five'] = 5
mapping['six'] = 6
mapping['seven'] = 7
mapping['eight'] = 8
mapping['nine'] = 9
mapping['ten'] = 10
mapping['eleven'] = 11
mapping['twelve'] = 12
mapping['thirteen'] = 13
mapping['fourteen'] = 14
mapping['fifteen'] = 15
mapping['sixteen'] = 16
mapping['seventeen'] = 17
mapping['eigtheen'] = 18
mapping['nineteen'] = 19
mapping['twenty'] = 20
mapping['thirty'] = 30
mapping['forty'] = 40
mapping['fifty'] = 50
mapping['sixty'] = 60
mapping['seventy'] = 70
mapping['eighty'] = 80
mapping['ninety'] = 90
mapping['hundred'] = 100
mapping['thousand'] = 1000
mapping['million'] = 1000000

def string_to_integer(s):
    s = s[:-1]
    tokens = s.split(' ')
    value = 0
    prev = value
    for token in tokens:
        if token == 'negative':
            continue
        if token in ['hundred','thousand','million']:
            temp = mapping[prev] * mapping[token]
            value += temp - mapping[prev]
        else:
            value += mapping[token]

        prev = token
    
    return -1 * value if tokens[0] == 'negative' else value


if __name__ == "__main__":
    print(string_to_integer('eleven thousand one hundred eleven\n'))