class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        leftovers = {}
        for i, num in enumerate(nums):
            lefter = target - num
            try:
                #print(leftovers[lefter])
                return [leftovers[lefter], i]
            except:
                leftovers[num] = i
        









        