class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        first = 0
        center = len(nums) // 2
        last = len(nums) - 1
        while last > first:
            if nums[center] == target:
                return center
            if nums[first] == target:
                return first
            if nums[last] == target:
                return last
            elif nums[center] > target:
                last = center - 1
                center = ((last - first) + 1) // 2
            else:
                first = center + 1
                center = (last + first) // 2
        return -1
        