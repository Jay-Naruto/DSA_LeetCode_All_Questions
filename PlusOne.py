# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int(''.join(map(str,digits)) ) + 1
        return [int(digit) for digit in str(num)]

        

# Runtime: 18 ms, faster than 41.52% of Python online submissions for Plus One.
# Memory Usage: 13.3 MB, less than 45.67% of Python online submissions for Plus One.