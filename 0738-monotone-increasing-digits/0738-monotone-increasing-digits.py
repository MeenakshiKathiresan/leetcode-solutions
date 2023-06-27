class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_string = str(n)
        length = len(num_string)
        index = length
        
        for i in range(length - 1, 0, -1):
            if num_string[i] < num_string[i - 1]:
                index = i - 1
                num_string = num_string[:index] + str(int(num_string[index]) - 1) + '9' * (length - index - 1)
        
        return int(num_string)