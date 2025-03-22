class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif len(stack) == 0:
                return False
            elif s[i] == ')':
                if stack.pop() != '(':
                    return False

            elif s[i] == ']': 
                if stack.pop() != '[':
                    return False

            elif s[i] == '}':
                if stack.pop() != '{':
                    return False
        
        if len(stack) == 0:
            return True
        return False
