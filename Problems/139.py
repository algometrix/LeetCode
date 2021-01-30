

def wordBreak(s, wordDict):
    ok = [True]
    for i in range(1, len(s)+1):
        ok += any(ok[j] and s[j:i] in wordDict for j in range(i)),
    return ok[-1]

if __name__ == "__main__":
    s = "cars"
    wordDict = ["ca", "car", "ra", 's']
    result = wordBreak(s, wordDict)
    print('Output : {}'.format(result))