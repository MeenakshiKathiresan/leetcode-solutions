class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def recurse(word):
            if word == "":
                return True
            if word in dp:
                return dp[word]
            
            n = len(word)
            res = False
            for w in wordDict:
                # match found
                if len(w) <= n and word[:len(w)] == w:
                    res = res or recurse(word[len(w):])
            dp[word] = False
            
            return res
        return recurse(s)
            


