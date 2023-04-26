public class Solution {
    public int SingleNumber(int[] nums) {
        
        Dictionary<int, int> count = new Dictionary<int, int> ();
        
        for (int i = 0; i < nums.Length; i++){
            if (count.ContainsKey(nums[i])){
                count[nums[i]]++;
            }
            else{
                count.Add(nums[i], 1);   
            }
        }
        
        foreach(var kvp in count){
            if (kvp.Value == 1){
                return kvp.Key;
            }
        }
     return -1;   
    }
}