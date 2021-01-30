
def geSubsequenceCount(s1, s2): 
      
    string_pattern = len(s1) 
    N = len(s2) 
    pattern = [None] * string_pattern 
    j = 0  
    buildString(s1, string_pattern, pattern) 
  
    i = 0  
    res = 0
    next_i = 0
  
    while i < N: 
        if s1[j] == s2[i]: 
            j = j + 1
            i = i + 1
        if j == string_pattern: 
            j = pattern[j - 1] 
            res = res + 1
            if pattern[j] != 0: 
                next_i = next_i + 1
                i = next_i 
                j = 0
  
        elif i < N and s1[j] != s2[i]: 
            if j != 0: 
                j = pattern[j - 1] 
            else: 
                i = i + 1
                  
    return res 
      
def buildString(pat, string_pattern, pattern): 
    len = 0
    i = 1
    pattern[0] = 0 
  
    while i < string_pattern: 
        if pat[i] == pat[len]: 
            len = len + 1
            pattern[i] = len
            i = i + 1
        else:  
            if len != 0: 
                len = pattern[len - 1] 
            else:  
                pattern[i] = len
                i = i + 1
  
if __name__ == "__main__": 
      
    txt = "geeksforgeeks"
    pat = "eeks"
    ans = geSubsequenceCount(pat, txt) 
      
    print(ans) 
  
