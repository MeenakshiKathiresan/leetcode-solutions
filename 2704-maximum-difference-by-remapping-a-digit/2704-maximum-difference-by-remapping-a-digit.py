class Solution:
    def minMaxDifference(self, num: int) -> int:
        # making the first digit 0
        # making the first non 9 digit 9

        num_str = str(num)
        smallest = num_str.replace(num_str[0], "0")
        change = ""
        for ch in num_str:
            if ch != "9":
                change = ch
                print(ch)
                break
        
        if change != "":
            largest = num_str.replace(change,"9")
        else:
            largest = num_str
        print(largest, smallest)
        return int(largest) - int(smallest)
