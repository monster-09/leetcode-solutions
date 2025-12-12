class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        prod = 1
        for i in str(n):
            num = int(i)
            sum += num
            prod *= num
        return prod - sum


        