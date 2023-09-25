class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letters = {}
        for letter in s:
            if letter not in letters:
                letters[letter] = 0
            letters[letter] += 1
        
        for letter in t:
            if letter not in letters or letters[letter] == 0:
                return letter
            letters[letter] -=1
        