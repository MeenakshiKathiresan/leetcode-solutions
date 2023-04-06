class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        longest_word = ""
        for word in dictionary:
            i = 0
            j = 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1
            if j == len(word) and len(word) > len(longest_word):
                longest_word = word
        return longest_word