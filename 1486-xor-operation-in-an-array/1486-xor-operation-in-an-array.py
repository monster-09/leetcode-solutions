class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0   # will store the XOR of all elements
        
        # Generate each element nums[i] = start + 2*i
        # and XOR it into result
        for i in range(n):
            value = start + 2 * i   # current element in the array
            result ^= value         # XOR with previous result
        
        return result
