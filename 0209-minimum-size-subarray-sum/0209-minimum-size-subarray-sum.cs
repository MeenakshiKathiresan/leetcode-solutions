public class Solution {
    public int MinSubArrayLen(int target, int[] nums) {
        
        int shortest = nums.Length + 1;
        int currentSum = 0;
        int count = 0;
        
        int left = 0;
        for (int i = 0; i < nums.Length; i++){
            
            currentSum += nums[i];
            count++;
            
            if (currentSum >= target ){
                while (currentSum >= target){
                    shortest = Math.Min(shortest, count);
                    currentSum -= nums[left];
                    left++;
                    count--;
                    
                }
                
                
            } 
            
        }
        
        if (shortest > nums.Length){
            return 0;
        }
        
        return shortest;
        
    }
}