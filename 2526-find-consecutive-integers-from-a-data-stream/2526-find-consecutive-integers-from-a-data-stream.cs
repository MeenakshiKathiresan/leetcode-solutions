public class DataStream {

    private int _value, _k, canAdd = 0;
    
    public DataStream(int value, int k) {
         _value = value;
         _k = k;
     
    }
    
    public bool Consec(int num) {
        if (num == _value){
            canAdd++;
        }else{
            canAdd = 0;
        }
        
        
        if (canAdd >= _k){
            return true;
        }
        return false;
    }
}

/**
 * Your DataStream object will be instantiated and called as such:
 * DataStream obj = new DataStream(value, k);
 * bool param_1 = obj.Consec(num);
 */