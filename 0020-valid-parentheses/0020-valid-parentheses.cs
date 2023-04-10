public class Solution {
    public bool IsValid(string s) {
        Dictionary<char,char> bracketPairs = new  Dictionary<char,char>();
        bracketPairs.Add('}','{');
        bracketPairs.Add(')','(');
        bracketPairs.Add(']','[');
        
        bool valid = true;
        
        List<char> brackets = new List<char>();
        foreach (char letter in s){
            if(letter == '{' || letter == '(' || letter == '['){
                brackets.Add(letter);
            }
            if(letter == '}' || letter == ')' || letter == ']'){
                if(brackets.Count>0 && bracketPairs[letter] == brackets[brackets.Count-1])
                    brackets.RemoveAt(brackets.Count-1);
                else
                    return false;
            }
            
        
        }
        if (brackets.Count != 0){
            return false;
        }
        return true;
        
    }
}