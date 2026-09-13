class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for ls in s:
            if ls not in dict_s.keys():
                dict_s[ls] = 1
            else:
                dict_s[ls] = dict_s[ls] + 1
        
        for lt in t:
            if lt not in dict_t.keys():
                dict_t[lt] = 1
            else:
                dict_t[lt] = dict_t[lt] + 1
        
        return dict_s == dict_t
        