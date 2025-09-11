class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_nums = {
            'I' :  1,
            'V' :  5,
            'X' :  10,
            'L' :  50,
            'C' :  100,
            'D' :  500,
            'M' : 1000
        }

        total = 0
        for i in range(len(s) - 1):
            if roman_nums[s[i]] < roman_nums[s[i + 1]]:
                total -= roman_nums[s[i]]
            else:
                total += roman_nums[s[i]]
        return total + roman_nums[s[-1]]