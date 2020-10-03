

def match(prefix, suffix):
    if len(prefix) == 0:
        return len(prefix) + len(suffix)
    if len(suffix) == 0:
        return 0
    if prefix[0] != suffix[0]:
        return 0

    counter = 0
    i, j = 0, 0
    print(prefix, suffix)
    while j < len(suffix):
        if j == len(suffix):
            return counter
        if prefix[i] == suffix[j]:
                counter += 1
                i = (i + 1) % len(prefix)
                j += 1
        else:
            return counter
    
    return counter

def commonPrefixLength(s):
    length = len(s)
    prefixSum = 0
    for i in range(length+1):
        prefix = s[:i]
        suffix = s[i:]
        matchVal = match(prefix, suffix)
        prefixSum += matchVal
        print('{} {} : {}'.format(prefix, suffix, matchVal))
    
    
    return prefixSum

if __name__ == "__main__":
    match("ababa", "a")
    _input = "ababaa"
    result = commonPrefixLength(_input)
    print('Output : {}'.format(result))