class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Numbers ending with 0 (except 0 itself) cannot be palindromes because reversed numbers can't start with 0.
        # Negative numbers cannot be palindromes because of the negative sign.
        if x < 0:  
            return False
        
        s = str(x)  # Convert number to string
        n = len(s)

        # i starts from beginning, j from end
        for i in range(n):
            j = n - 1 - i
            if s[i] != s[j]:
                return False
        return True
