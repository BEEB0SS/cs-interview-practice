class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for n in nums:
            #print(dic.keys())
            if n in dic.keys():
                return True
            else:
                dic[n] = "present"
        return False

        