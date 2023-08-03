public class Solution {
    public IList<string> LetterCombinations(string digits) {    
        List<string> combos = new List<string>();
        
         if (digits.Length == 0) return combos;
        combos.Add("");
        
   string[] digitMap  = {"0", "1" ,"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        for(int i = 0 ; i< digits.Length ; i++ ){
            
                 List<string> temp = new List<string>();
            
            for(int j = 0; j< digitMap[digits[i] - '0'].Length;j++){
                for(int k = 0; k<combos.Count;k++){
                  temp.Add(combos[k] + digitMap[digits[i] - '0'][j]);
                }
            }
            
            combos = temp;
        }
        return combos;
            
}
}