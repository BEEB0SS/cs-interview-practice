class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_num = {}
        for num in nums:
            if dict_num.get(num) != None:
                return True
            else:
                dict_num[num] = 1
        return False
        
        