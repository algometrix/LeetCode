def numDistinct1(s, t):
    string_length, pattern_length = len(s), len(t)
    dp = [ 0 for x in range(string_length + 1) ]


if __name__ == "__main__":
    _string, _pattern = 'babgbagg', 'bag'
    result = numDistinct1(_string, _pattern)
    print('Result : {}'.format(result))