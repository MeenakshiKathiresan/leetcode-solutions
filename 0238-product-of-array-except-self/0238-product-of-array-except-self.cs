public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int n = nums.Length;
        int[] res = new int[n];
        
        // Step 1: Compute the left products and store them in res
        res[0] = 1;
        for (int i = 1; i < n; i++) {
            res[i] = res[i - 1] * nums[i - 1];
        }
        
        // Step 2: Compute the right products and update the res array
        int product = 1;
        for (int i = n - 2; i >= 0; i--) {
            product *= nums[i + 1];
            res[i] *= product;
        }
        
        return res;
    }
}
