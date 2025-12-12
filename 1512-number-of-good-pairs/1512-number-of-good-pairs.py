class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        freq = {}
        count = 0

        for i in nums:
            if i in freq:
                count += freq[i]   # each previous occurrence forms a good pair
                freq[i] += 1
            else:
                freq[i] = 1

        return count
