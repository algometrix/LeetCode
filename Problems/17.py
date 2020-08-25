class Solution:
    keystrokes = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz',]
    def generateKeystrokes(self, _input, index, length, result, p = ''):
        #print(p, index, length, len(p), self.keystrokes[int(_input[index])])
        if len(p) == length:
            result.append(p)
            return
        
        for letter in self.keystrokes[int(_input[index])]:
            self.generateKeystrokes(_input, min(index+1, length-1), length,result, p + letter)

        
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        digits = digits + ''
        result = []
        for letter in self.keystrokes[int(digits[0])]:
            self.generateKeystrokes(digits, 1, len(digits), result, p = letter)
        
        return result