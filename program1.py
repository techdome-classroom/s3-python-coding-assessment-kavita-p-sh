class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """


        bracket_map = {')': '(', '}': '{', ']': '['}
       
        stack = []


        for char in s:

            if char in bracket_map:

                top_element = stack.pop() if stack else '#'

                if bracket_map[char] != top_element:
                    return False
            else:

                stack.append(char)
        
        # If the stack is empty, all opening brackets have been matched; otherwise, it's invalid
        return not stack

        pass







    



  

