'''
Recursion Levels with indentation

N : 3
1. Left : 3 and Right : 3 = 
 2. Left : 2 and Right : 3 = (
  3. Left : 1 and Right : 3 = ((
   4. Left : 0 and Right : 3 = (((
    5. Left : 0 and Right : 2 = ((()
     6. Left : 0 and Right : 1 = ((())
      7. Left : 0 and Right : 0 = ((()))
Not Right : ((()))
Parenthesis String : ['((()))']
****************************************************************************
   4. Left : 1 and Right : 2 = (()
    5. Left : 0 and Right : 2 = (()(
     6. Left : 0 and Right : 1 = (()()
      7. Left : 0 and Right : 0 = (()())
Not Right : (()())
Parenthesis String : ['((()))', '(()())']
****************************************************************************
    5. Left : 1 and Right : 1 = (())
     6. Left : 0 and Right : 1 = (())(
      7. Left : 0 and Right : 0 = (())()
Not Right : (())()
Parenthesis String : ['((()))', '(()())', '(())()']
****************************************************************************
  3. Left : 2 and Right : 2 = ()
   4. Left : 1 and Right : 2 = ()(
    5. Left : 0 and Right : 2 = ()((
     6. Left : 0 and Right : 1 = ()(()
      7. Left : 0 and Right : 0 = ()(())
Not Right : ()(())
Parenthesis String : ['((()))', '(()())', '(())()', '()(())']
****************************************************************************
    5. Left : 1 and Right : 1 = ()()
     6. Left : 0 and Right : 1 = ()()(
      7. Left : 0 and Right : 0 = ()()()
Not Right : ()()()
Parenthesis String : ['((()))', '(()())', '(())()', '()(())', '()()()']
****************************************************************************
['((()))', '(()())', '(())()', '()(())', '()()()']
'''

def generateParenthesis(n):
    def generate(p, left, right, parens=[], level = 1):
        if left:         
            generate(p + '(', left-1, right, parens, level + 1)
        if right > left: 
            generate(p + ')', left, right-1, parens, level + 1)
        if not right:    
            parens += p,
        
        return parens
    
    return generate('', n, n)


if __name__ == "__main__":
    result = generateParenthesis(3)
    print(result)