

def longestSubstringWithoutDuplcation(string):
    lastSeen = {}
    longest = [0, 1]
    startIndex = 0
    for index, character in enumerate(string):
        if character in lastSeen:
            startIndex = max(lastSeen[character] + 1, startIndex)
        if longest[1] - longest[0] < index + 1 - startIndex:
            longest = [startIndex, index + 1]
        lastSeen[character] = index 
    
    return string[longest[0]: longest[1]]


if __name__ == "__main__":
    _string = 'clementisacap'
    result = longestSubstringWithoutDuplcation(_string)
    print('Output : {}'.format(result))