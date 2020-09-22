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
    def dfs(s, left, right, result):
        print('Left : {} : Right : {} => {}'.format(left, right, s))
        if left != 0:
            dfs(s + '(', left-1, right, result)
        if right and right > left:
            dfs(s + ')', left, right-1, result)

        if left == 0 and right == 0:
            result.append(s)

    result = []
    dfs('', n, n, result)
    return result


if __name__ == "__main__":
    result = generateParenthesis(3)
    print(result)
