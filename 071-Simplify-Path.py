class Solution:
    '''
    Input: "/a/./b/../../c/"
    Output: "/c"'
    '''
    
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        parts = path.split('/')
        
        for part in parts:
            if part in ['', '.']:
                continue
            elif part == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(part)
        
        return '/' if len(stack) == 0 else '/'.join([''] + stack)


if __name__ == '__main__':
    path = "/a/./b/../../c/"
    result = Solution().simplifyPath(path)
    print(result)
    
    path = "/home/"
    result = Solution().simplifyPath(path)
    print(result)
    
    path = "/../"
    result = Solution().simplifyPath(path)
    print(result)
    
    path = "/home//foo/"
    result = Solution().simplifyPath(path)
    print(result)
    
    path = "/a/../../b/../c//.//"
    result = Solution().simplifyPath(path)
    print(result)
    
    path = "/a//b////c/d//././/.."
    result = Solution().simplifyPath(path)
    print(result)
