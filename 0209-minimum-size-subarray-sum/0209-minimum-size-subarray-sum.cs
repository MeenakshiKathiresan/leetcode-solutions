public class Solution {
    public int MinSubArrayLen(int target, int[] nums) {
        
        int shortest = nums.Length;
        int currentSum = 0;
        int count = 0;
        
        int left = 0;
        bool found = false;
        for (int i = 0; i < nums.Length; i++){
            
            currentSum += nums[i];
            count++;
            
            if (currentSum >= target ){
                found = true;
                
                while (currentSum >= target){
                    shortest = Math.Min(shortest, count);
                    currentSum -= nums[left];
                    left++;
                    count--;
                    
                }
                
                
            } 
            
        }
        
        if (!found){
            return 0;
        }
        
        return shortest;
        
    }
}