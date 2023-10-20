/* The isBadVersion API is defined in the parent class VersionControl.
      bool IsBadVersion(int version); */

public class Solution : VersionControl {
    public int FirstBadVersion(int n) {
   
        int start = 0;
        int end = n;
        while(start<end){
            int current = start + (end - start)/2;
            if (IsBadVersion(current)){
                if(!IsBadVersion(current-1)){
                    return current;
                }
                end = current;
            }
            else{
                if (IsBadVersion(current+1)){
                    return current+1;
                }
                start = current;
            }
        }
        return 0;
    }
}