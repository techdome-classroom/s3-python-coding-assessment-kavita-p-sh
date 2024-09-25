class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """


        bracket_map = {')': '(', '}': '{', ']': '['}
       
        stack = []


        for char in s:
            # If it's a closing bracket
            if char in bracket_map:
                # Pop the top of the stack if it's non-empty, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the top element matches the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all opening brackets have been matched; otherwise, it's invalid
        return not stack

        pass







    



  

