class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        res = ""
        count = 1
        i = 0
        while i < len(chars)-1:
            if chars[i] == chars[i+1]:
                chars.pop(i)
                count+=1
            else:
                res += str(chars[i]) + str(count)
                
                 
                if count > 9:
                    digits = []
                    
                    while count > 0:
                        n = count%10
                        count = count/10
                        digits.append(n)
                    
                    for digit in digits[::-1]:
                        chars.insert(i+1, str(digit))
                        i+=1
                    
                if count > 1:
                    chars.insert(i+1, str(count))
                    i+=1
                
                count = 1
            
                i += 1
                
        res += str(chars[i]) + str(count)
                
                 
        if count > 9:
            digits = []

            while count > 0:
                n = count%10
                count = count/10
                digits.append(n)

            for digit in digits[::-1]:
                chars.insert(i+1, str(digit))
                i+=1




        if count > 1:

            chars.insert(i+1, str(count))
        return len(res)
                