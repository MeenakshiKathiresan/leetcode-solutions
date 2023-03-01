class Solution(object):
    def sortArray(self, the_list):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge_lists(left, right):
            result = []
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            while i < len(left):
                result.append(left[i])
                i += 1

            while j < len(right):
                result.append(right[j])
                j += 1

            return result
        
        
        if len(the_list) <= 1:
            return the_list
        
        list_divider_index = len(the_list) // 2
        left_list = self.sortArray(the_list[:list_divider_index])
        right_list = self.sortArray(the_list[list_divider_index:])
        return merge_lists(left_list, right_list)

        
        


