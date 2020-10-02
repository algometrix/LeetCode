def wordBreak(s, wordDict):
    length = len(s)
    ok = [True,]
    tracker = {} 
    for i in range(length):
        flag = False
        for j in range(i+1):
            check = ok[j] and s[j:i+1] in wordDict
            if check:
                flag = True
                if j in tracker:
                    tracker[j].append(i)
                else:
                    tracker[j] = [i]
        
        ok.append(flag)
        
    if ok[-1] == False:
        return []

    result = []
    def dfs(key, st):
        if key not in tracker:
            if s[key:] in wordDict or key == len(s):
                result.append((st + ' ' + s[key:]).strip())
            return
        
        for value in tracker[key]:
            dfs(value + 1, st + ' ' + s[key:value+1])
    
    dfs(0, '')
    return result

if __name__ == "__main__":
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    result = wordBreak(s, wordDict)
    print('Output : {}'.format(result))