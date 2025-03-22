class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackMap = {'}':'{', ']':'[', ')':'('}

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif stack and stack[-1] == brackMap[s[i]]:
                stack.pop()
            else:
                return False

        
        if len(stack) == 0:
            return True
        return False
