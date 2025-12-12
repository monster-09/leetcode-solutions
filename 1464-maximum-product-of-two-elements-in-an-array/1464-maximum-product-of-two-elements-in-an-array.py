class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = 0
        for i in range(n):
            for j in range(i + 1,n):
                prod = (nums[i]-1)*(nums[j]-1)

                 # Update maximum product found
                if prod > max_val:
                    max_val = prod

        return max_val
        