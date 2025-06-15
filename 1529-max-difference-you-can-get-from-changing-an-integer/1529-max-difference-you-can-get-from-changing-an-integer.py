class Solution:
    def maxDiff(self, num: int) -> int:
        # convert first number non 9 to 9
        # convert first number to 1 if possible, if not second number to 0

        num_str = str(num)
        min_num = 1
        a, b = num_str, num_str
        # if all numbers are same
        all_same = True
        for i, ch in enumerate(num_str):
            if ch != num_str[0]:
                all_same = False
                break
        
        if all_same:
            a = num_str.replace(num_str[0],"9")
            b = num_str.replace(num_str[0],"1")
            return int(a) - int(b)


        if num_str[0] == "1":
            for ch in num_str:
                if ch != "1" and ch != "0":
                    b = num_str.replace(ch, "0")
                    break
        else:
            b = num_str.replace(num_str[0], "1")
        
        if num_str[0] == "9":
            for ch in num_str:
                if ch != "9":
                    a = num_str.replace(ch, "9")
                    break
        else:
            a = num_str.replace(num_str[0], "9")
        print(a, b)
        return int(a) - int(b)
