class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remainder = 0
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] += 1
                remainder = digits[i] // 10
                digits[i] = digits[i] % 10
        
        if remainder > 0:
            digits = [remainder] + digits
        return digits