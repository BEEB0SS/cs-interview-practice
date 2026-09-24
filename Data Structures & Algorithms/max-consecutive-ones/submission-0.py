class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        counter = 0
        for num in nums:
            if num == 1:
                counter += 1
            else:
                counter = 0
            if counter > max_ones:
                max_ones = counter
        return max_ones   
        