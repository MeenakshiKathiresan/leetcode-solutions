public class Solution {
    public int[] ProductExceptSelf(int[] nums) {

        int[] res = new int[nums.Length];
        Array.Fill(res,1);

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
        return res;
    }
}