public class Solution {
    public bool IsSubsequence(string s, string t) {
        int sPointer = 0;
        if(s.Length==0) return true;
        for(int i=0;i<t.Length;i++){
            
            if(t[i]==s[sPointer]){
                Console.WriteLine(t[i]);
                if(sPointer<s.Length-1){
                    sPointer++;
                }else{
                    return true;
                }
            }
        }
        if(sPointer >= s.Length){
            return true;
        }
        return false;
    }
}