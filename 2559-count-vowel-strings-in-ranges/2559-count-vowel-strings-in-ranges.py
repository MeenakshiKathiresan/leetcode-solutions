class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        count = 0
        vowel_set = {"a", "e", "i", "o", "u"}

        def isVowel(word):
            if word[0] in vowel_set and word[-1] in vowel_set:
                return True
            return False

        for word in words:
            if isVowel(word):
                count += 1
            res.append(count)

        soln = []

        for query in queries:
            if query[0] == query[1]:
                if isVowel(words[query[0]]):
                    soln.append(1)
                else:
                    soln.append(0)
                continue

            start = res[query[0] - 1] if query[0] > 0 else 0
            ans = res[query[1]] - start
            soln.append(ans)

        return soln