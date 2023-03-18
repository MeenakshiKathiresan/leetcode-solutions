public class Solution {
    public string Convert(string s, int numRows) {
        if (numRows == 1){
            return s;
        }
        
        string[] rows = new string[numRows];
        bool down = true;
        int current = 0;
        
        for(int i = 0; i < s.Length; i++){
            rows[current] += s[i];
            if (down){
                current += 1;
            }
            else{
                current -= 1;
            }
            if (current == rows.Length){
                down = false;
                current -= 2;
            }else if(current == -1){
                down = true;
                current += 2;
            }
        }
        
    var result = string.Empty;
    foreach (var item in rows)
    {
        result += item;
    }
    return result;
    }
}