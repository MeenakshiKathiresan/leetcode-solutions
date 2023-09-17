public class Solution {
    public string CountAndSay(int n) {
        string say = "";
        string last_say = "";
        string no = "1";
        int ct = 0;
        int count = 1;

    if (n == 1){
        return "1";
    }

    while(ct<n-1){
        
    ct +=1;
      for(int i =0; i<no.Length;i++){

            if (i<no.Length -1 && no[i] == no[i+1]){
                count += 1;
            }else{
                say += count.ToString() + no[i]; 
                
                count = 1;
            }

        }
            no = say;
            last_say = say;
            say = "";
        }
        return last_say;
    
    }
}