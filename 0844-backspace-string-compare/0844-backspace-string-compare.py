class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1, s2 = [], []
        for ch in s:
            if ch == "#":
                if s1:
                    s1.pop()
            else:
                s1.append(ch)
        
        for ch in t:
            if ch == "#":
                if s2:
                    s2.pop()
            else:
                s2.append(ch)
        print(s1,s2)
        st1 = "".join(s1)
        st2 = "".join(s2)
        return st1 == st2
            