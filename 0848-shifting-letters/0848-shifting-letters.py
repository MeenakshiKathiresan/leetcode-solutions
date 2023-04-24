class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        s = list(s)
        total_shifts = sum(shifts) % 26

        for i, shift in enumerate(shifts):
            new_char = chr((ord(s[i]) - ord('a') + total_shifts) % 26 + ord('a'))
            s[i] = new_char
            total_shifts = (total_shifts - shift) % 26

        return ''.join(s)