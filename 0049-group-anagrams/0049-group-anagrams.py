class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        sorted version as key
        """
        anagram = {}
        res = []
        for word in strs:
            key_list = sorted(word)
            key = "".join(key_list)
            if key not in anagram:
                anagram[key] = []
            anagram[key].append(word)
        
        for v in anagram.values():
            res.append(v)
        return res