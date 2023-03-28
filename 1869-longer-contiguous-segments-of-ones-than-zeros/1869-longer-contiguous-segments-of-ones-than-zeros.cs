public class Solution {
    public bool CheckZeroOnes(string s) {
        
        int zCount = 0 , oCount = 0;
        
        int current = 0;
        
        if (s=="1")
            return true;
        
        for (int i = 0; i < s.Length; i++){
            if (i>0 && s[i] == s[i-1]){
                current += 1;
                if (s[i] == '1'){
                    
                    oCount = Math.Max(oCount, current);
                }
                else if(s[i] == '0'){
                    zCount = Math.Max(zCount, current);
                }
            }
            else{
                current = 0;
            }
        }
        
        return zCount < oCount;
        
    }
}