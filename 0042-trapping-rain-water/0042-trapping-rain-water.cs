public class Solution {
    public int Trap(int[] height) {
        int leftWall, rightWall, left, right;
        left = 0;
        right = height.Length - 1;
        leftWall = height[left];
        rightWall = height[right];
        int res = 0;

        while(left <= right){
            if (leftWall < rightWall){
                if(height[left] > leftWall){
                    leftWall = height[left];                    
                }else{
                    res += leftWall - height[left];
                }
                left++;

            }else{
                if(height[right] > rightWall){
                    rightWall = height[right];                    
                }else{
                    res += rightWall - height[right];
                }
                right--;
            }
        }        
        return res;

    }
}