public class Solution {
    public int SearchInsert(int[] nums, int target) {
                
        int lower = 0;
        int upper = nums.Length-1;
        
        while(lower<=upper){
            int n = lower + (upper - lower)/2;
            if(nums[n]<target){
                lower = n+1;
            }
            else{
                upper = n-1;
            }
            
        }
        return lower;
    }
}