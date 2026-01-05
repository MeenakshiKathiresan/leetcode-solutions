class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        def sum_of_divisors(num):
            res = 0
            for i in range(1, int(num**0.5) + 1):
                if num % i == 0:
                    res += i
                    if i != num // i:
                        res += num // i
            return res

        def is_four_divisors(num):
            cnt = 0
            for i in range(1, int(num**0.5) + 1):
                if num % i == 0:
                    cnt += 1
                    if i != num // i:
                        cnt += 1
                    if cnt > 4:  
                        return False
            return cnt == 4

        final_res = 0
        for num in nums:
            if is_four_divisors(num):
                final_res += sum_of_divisors(num)

        return final_res