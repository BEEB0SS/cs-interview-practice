class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_of_anagrams = []
        anagram_map = {}
        for word in strs:
            word_dict = [0] * 26
            for letter in word:
                num_letter = ord(letter)
                index_letter = 25 - (122 - num_letter)
                word_dict[index_letter] += 1
            word_key = tuple(word_dict)
            if word_key in anagram_map:
                anagram_map[word_key].append(word)
            else:
                anagram_map[word_key] = [word]
        for word_key in anagram_map:
            list_of_anagrams.append(anagram_map[word_key])
        return list_of_anagrams 
        


        
        
        