public class Solution {
    public int FirstMissingPositive(int[] nums) {
        
        HashSet<int> numbers = new HashSet<int>();
        
        for (int i = 0; i <= nums.Length; i++){
            numbers.Add(i+1);
        }
        
        for (int i = 0; i <nums.Length; i++){
            if (numbers.Contains(nums[i])){
                numbers.Remove(nums[i]);
            }
        }
        
        return numbers.First();
        
        
    }
}