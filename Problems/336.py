

def palindromePairs(words):
    d = {w: i for i, w in enumerate(words)}
    ans = []
    for i, w in enumerate(words):
        # no divide, two cases
        if w[::-1] in d and d[w[::-1]] != i:
            ans.append([i, d[w[::-1]]])
        if w != '' and w[::-1] == w and '' in d:
            ans.append([i, d['']])
            ans.append([d[''], i])
        
        # divide into two parts, can't be self, another two cases
        for k in range(1, len(w)):
            s1, s2 = w[:k], w[k:]
            if s1 == s1[::-1] and s2[::-1] in d:
                ans.append([d[s2[::-1]], i])
            if s2 == s2[::-1] and s1[::-1] in d:
                ans.append([i, d[s1[::-1]]])
    return ans


if __name__ == "__main__":
    words = ["abcd","dcba","lls","s","sssll"]
    result = palindromePairs(words)
    print('Result : {}'.format(result))