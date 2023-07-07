class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        l, r = 0, 0
        curr_k, max_count = 0, 0
        
        # First T to F
        for ans in answerKey:
            r += 1
            if ans == "T":
                curr_k += 1
            if curr_k > k:
                if answerKey[l] == 'T':
                    curr_k -= 1
                l += 1

            max_count = max(max_count, r - l)

        l, r = 0, 0
        curr_k = 0
        max_count_F_to_T = 0

        # Second F to T
        for ans in answerKey:
            r += 1
            if ans == "F":
                curr_k += 1
            if curr_k > k:
                if answerKey[l] == 'F':
                    curr_k -= 1
                l += 1

            max_count_F_to_T = max(max_count_F_to_T, r - l)

        return max(max_count, max_count_F_to_T)
