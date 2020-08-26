class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [0,]
        max_parenthesis = 0
        for bracket in s:
            #print(bracket)
            if bracket == '(':
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    max_parenthesis = max(max_parenthesis, stack[-1])
                else:
                    stack = [0]

        return max_parenthesis
        