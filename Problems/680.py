class Solution:
    def validPalindrome(self, s: str) -> bool:
        new_string = ''
        i = 0
        for _ in range(len(s)):
            if s[i] == s[-(i + 1)]: 
                i += 1
        
        if i == len(s):
            return True
        
        new_string_1 = s[:i] + s[i+1:]
        if new_string_1 == new_string_1[::-1]:
            return True
        
        new_string_2 = s[:len(s)-i-1] + s[len(s)-i:]
        if new_string_2 == new_string_2[::-1]:
            return True
        
        return False
        
            