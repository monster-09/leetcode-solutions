class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        
        # Step 1: Sort the array
        sorted_nums = sorted(nums)
        
        # Step 2: Create a dictionary to store how many numbers are smaller
        # The first time a number appears in sorted order = count of smaller numbers
        rank = {}
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in rank:
                rank[sorted_nums[i]] = i   # index = how many numbers are smaller
        
        # Step 3: Build the result using the rank dictionary
        result = []
        for x in nums:
            result.append(rank[x])
        
        return result
