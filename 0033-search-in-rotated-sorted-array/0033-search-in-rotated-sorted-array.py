class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # find pivot

        # is given number greater than first number?
        # if yes pivot is after that
        # if no pivot is before that


        # is number before or after pivot - binary search
        low = 0
        high = len(nums) - 1
        mid = -1

        while(low-1<high):
            mid = low + ((high - low) /2)
            print(mid, low, high)
            if mid!=0 and nums[mid] < nums[mid -1]:
                break
            if nums[mid] > nums[0]:
                low = mid + 1
            elif nums[mid] < nums[0]:
                high = mid - 1
            else:

                if len(nums)>1 and nums[mid] > nums[mid+1]:
                    mid = mid + 1
                break
        

        pivot = mid
        print(pivot)
        

        if target < nums[0] or pivot ==0:
            low = pivot
            high = len(nums) -1
        else:
            low = 0
            high = pivot
        
        
        print(low, high)
        # 1 2 3 4 5 6 7
        while(low<high):
            mid = low + ((high - low) /2)
            print(mid, low, high)
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid

        if low == high and nums[low] == target:
            return low


        return -1