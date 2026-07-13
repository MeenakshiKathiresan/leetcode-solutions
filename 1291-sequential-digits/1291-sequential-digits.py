class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """

        def digit_count(n):
            cnt = 0
            while n > 0:
                n = n // 10
                cnt += 1
            return cnt

        def generate(digit_count, min, max):
            print(digit_count,min,max)
            temp = []

            for i in range(1, 11 - digit_count):
                curr_num = 0
                for j in range(i, i + digit_count):
                    curr_num = curr_num * 10 + j

                if curr_num > max:
                    return temp

                if curr_num >= min:
                    temp.append(curr_num)
            return temp

        res = []
        low_count = digit_count(low)
        high_count = digit_count(high) + 1

        for i in range(low_count, high_count):
            curr = generate(i, low, high)
            res += curr

        return res