class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)
        ans = 0
        changed = False
        for i, no in enumerate(num_str):
            if not changed and no == '6':
                changed = True
                no = '9'

            ans += int(no) * pow(10, (len(num_str) - i - 1))

        return ans