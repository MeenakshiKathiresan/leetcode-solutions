class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # compare left and right
        # do binary search
        
        l = 0 
        r = len(arr) - 1
        
        while l <= r:
            mid = (l+r)//2
            
            if arr[mid-1] < arr[mid] < arr[mid+1]:
                l = mid + 1
            elif arr[mid-1] > arr[mid] > arr[mid+1]:
                r = mid - 1
            else:
                if arr[mid-1] < arr[mid] > arr[mid + 1]:
                    return mid
                else:
                    if mid == 0:
                        return mid + 1
                    elif mid == len(arr)-1:
                        return mid -1