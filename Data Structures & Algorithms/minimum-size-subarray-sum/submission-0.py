class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        total = 0
        min_window = float('inf')
        L = 0
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                window_size = i - L + 1
                if window_size < min_window:
                    min_window = window_size
                if min_window == 1:
                    return min_window
                total -= nums[L]
                L += 1
                window_size -= 1
    
        return min_window



        