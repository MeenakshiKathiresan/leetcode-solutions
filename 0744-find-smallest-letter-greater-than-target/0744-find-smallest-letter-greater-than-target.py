class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if letters[-1] <= target:
            return letters[0]
        
        
        
        largest = letters[-1]
        
        left = 0
        right = len(letters)-1
        
        while (left <= right):
            mid = (left + right) //2
            
            if letters[mid]>target:
                if letters[mid] < largest:
                    largest = letters[mid]
                right = mid -1
            else:
                left = mid+1
                
        return largest