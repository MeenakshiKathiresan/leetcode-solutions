class Solution:
    def maximum69Number (self, num: int) -> int:
        
        num_str = str(num)
        
        i = 0
        while i < len(num_str) and num_str[i] == "9":
            i += 1

        print(i)

        if i == len(num_str):
            return num
        else:
            return int(num_str[:i] + "9" + num_str[i+1:])