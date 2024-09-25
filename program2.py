class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Roman numeral to integer mapping
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        total = 0
        prev_value = 0
        
        # Iterate over the string in reverse order
        for char in reversed(s):
            # Get the integer value of the current Roman numeral
            current_value = roman_map[char]
            
            # If the current value is smaller than the previous one, subtract it (e.g., IV, IX)
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
                
            # Update previous value
            prev_value = current_value
        
        return total

        pass



