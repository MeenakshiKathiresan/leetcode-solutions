public class Solution {
    public int MaxProfit(int[] prices) {
        if(prices.Length<1)
            return 0;
        int high = 0;
        int lowest = prices[0];
        for(int i=0;i<prices.Length;i++){
            if (lowest < prices[i]){
                high = Math.Max(high,prices[i]-lowest);
            }else{
                lowest = prices[i];
            }
        }
        return high;
    }
}