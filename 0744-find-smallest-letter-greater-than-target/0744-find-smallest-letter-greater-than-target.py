class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if letters[-1] <= target:
            return letters[0]
        
        
        
        left = 0
        right = len(letters)-1
        
        while (left <= right):
            mid = (left + right) //2
            
            if letters[mid]>target:
                right = mid -1
            else:
                left = mid+1
                
        return letters[left]