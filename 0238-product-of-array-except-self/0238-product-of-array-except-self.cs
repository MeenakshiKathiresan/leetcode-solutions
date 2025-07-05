public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        List<int> res = new List<int>();

        for(int i = 0; i < nums.Length; i++){
            res.Add(1);
        }

        int product = 1;
        for(int i = 1; i < nums.Length; i++){
            product *= nums[i-1];
            res[i] = product;
        }

        product = 1;

        for(int i = nums.Length - 2; i >= 0; i--){
            product *= nums[i+1];
            res[i] *= product;
        }
        return res.ToArray();
    }
}