class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = [] # stack of directories
        for p in path.split('/'): # split by '/'
            if p == '..': # go up one level
                if stack: 
                    stack.pop() # pop the last directory
            elif p and p != '.': # ignore empty and current directory
                stack.append(p) # push the directory
        return '/' + '/'.join(stack) # join the directories with '/'