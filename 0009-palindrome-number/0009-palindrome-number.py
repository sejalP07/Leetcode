class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # Negative numbers cannot be palindromes
        if x < 0:
            return False

        original = x
        reverse = 0

        # Reverse the number
        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x //= 10

        # Compare original and reversed numbers
        return original == reverse