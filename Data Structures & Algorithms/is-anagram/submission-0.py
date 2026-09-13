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
        
        for key in dict_s.keys():
            if key not in dict_t.keys():
                return False
            if dict_s[key] != dict_t[key]:
                return False
        
        for key in dict_t.keys():
            if key not in dict_s.keys():
                return False
            if dict_t[key] != dict_s[key]:
                return False

        return True
        