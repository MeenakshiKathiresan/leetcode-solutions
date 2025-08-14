public class Solution {
    public string LargestGoodInteger(string num) {
        int sameCount = 0;
        int high = -1;
        char previous = '0';
        
        foreach (char no in num){
            if(previous == no){
                sameCount++;
                
            }
            else{
                sameCount=0;
            }
            if(sameCount == 2){
               int current = no -'0';
                if(current>high){
                    high = current;
                }
            }
            previous = no;
        }
        if (high == -1)
            return "";
        int numb = high;
        numb = numb * 100 + numb *10 + numb* 1;
        
        if(numb == 0){
            return "000";
        }
         return numb.ToString();
    }
}