class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = []
        for i in range(0, len(s)):
            if s[i] == '*':
                st.pop()
            else:
                st.append(s[i])

        return ''.join(st)