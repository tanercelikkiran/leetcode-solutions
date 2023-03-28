import collections

class Solution:
    def isValid(self, s: str) -> bool:
        dic = { # dictionary to store the closing brackets
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = collections.deque() # stack to store the opening brackets
        for c in s: # iterate through the string
            if c == '(' or c == '[' or c == '{': # if the character is an opening bracket
                stack.append(c) # push it to the stack
            elif len(stack) == 0: # if the stack is empty and the character is a closing bracket
                return False # return False
            else: # if the character is a closing bracket
                if stack.pop() != dic[c]: # if the top of the stack is not the corresponding opening bracket
                    return False # return False
        return len(stack) == 0 # if the stack is empty, return True, else return False