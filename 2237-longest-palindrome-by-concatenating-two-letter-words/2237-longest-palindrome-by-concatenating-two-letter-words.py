class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # use counter
        # for every word, if not palindrome itself,
        # check if its opposite is available 
        # if yes, subtract 1 of both

        word_counter = Counter(words)
        res = 0
        once_used = False
        for w in words:
            if word_counter[w] > 0:
                if w[0] == w[1]:
                    if word_counter[w] < 2 and not once_used:
                        res += 2
                        once_used = True
                    elif word_counter[w] > 1:
                        res += 4
                        word_counter[w] -= 2
                else:
                    rev = w[::-1]
                    if rev in word_counter and word_counter[rev] > 0:
                        word_counter[rev] -= 1
                        word_counter[w] -= 1
                        res += 4
        return res