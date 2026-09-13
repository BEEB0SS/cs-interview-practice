class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        smap = {}
        tmap = {}
        for letter in s:
            try:
                smap[letter] += 1
            except:
                smap[letter] = 1
        for letter in t:
            try:
                tmap[letter] += 1
            except:
                tmap[letter] = 1
        for key in smap:
            if key not in tmap or tmap[key] != smap[key]:
                return False
        return True
        