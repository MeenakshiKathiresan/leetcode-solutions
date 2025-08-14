class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_val = -1

        prev = ""
        cnt = 1

        def get_3_digit(n):
            i = 1
            res = n
            while i < 3:
                res *= 10
                res += n
                i += 1
            return res

        for ch in num:
            if ch == prev:
                cnt += 1
            else:
                cnt = 1
            
            if cnt == 3:
                curr = get_3_digit(int(ch))
                if curr > max_val:
                    max_res = ch * 3
                    max_val = curr
                print(ch)
                cnt = 1
            prev = ch

        if max_val == -1:
            return ""

        return max_res