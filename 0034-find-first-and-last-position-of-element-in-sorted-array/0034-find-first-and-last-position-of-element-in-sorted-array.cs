public class Solution {
    public int[] SearchRange(int[] nums, int target) {
     int[] startEnd = {-1,-1};
     int left = 0;
     int right = nums.Length -1;
     int mid = (left + right)/2;    
     while(left<=right){
         mid = (left + right)/2; 
         if(nums[mid]<target){
             left = mid +1;
         }else if(nums[mid]>target){
             right = mid -1;
         }else{
             
             left = right+1;
             bool terminateStart = false;
             bool terminateEnd = false;
             startEnd[0]=mid;
             startEnd[1]=mid;
             
             while(!(terminateStart&& terminateEnd)){
             if(startEnd[0]-1>=0 && nums[startEnd[0]-1]==nums[mid]){
                
                 startEnd[0]-=1;
             }else{
                 terminateStart = true;
             }
             if(startEnd[1]+1<nums.Length && nums[startEnd[1]+1]==nums[mid]){
                 startEnd[1]+=1;
                 
             }else{
                 terminateEnd = true;
             }
                 
             
         }
         
     }
     }
        return startEnd;
    }
}