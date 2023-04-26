public class MyCircularDeque {
    private List<int> queue;
    private int size;


    public MyCircularDeque(int k) {
        queue = new List<int>();
        size = k;
    }
    
    public bool InsertFront(int value) {
        if (queue.Count < size){
            
            queue.Insert(0, value);
            return true;
        }
        return false;
    }
    
    public bool InsertLast(int value) {
        if (queue.Count < size){
            
            queue.Add(value);
            return true;
        }
        return false;
    }
    
    public bool DeleteFront() {
        if (queue.Count > 0){
            
            queue.RemoveAt(0);
            return true;
        }
        return false;
    }
    
    public bool DeleteLast() {
        if (queue.Count > 0){
            
            queue.RemoveAt(queue.Count - 1);
            return true;
        }
        return false;
    }
    
    public int GetFront() {
        if (queue.Count > 0){
            return queue[0];
            
        }
        return -1;
    }
    
    public int GetRear() {
        if (queue.Count > 0){
            return queue[queue.Count - 1];
            
        }
        return -1;
    }
    
    public bool IsEmpty() {
        return queue.Count == 0;
    }
    
    public bool IsFull() {
        return queue.Count == size;
    }
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque obj = new MyCircularDeque(k);
 * bool param_1 = obj.InsertFront(value);
 * bool param_2 = obj.InsertLast(value);
 * bool param_3 = obj.DeleteFront();
 * bool param_4 = obj.DeleteLast();
 * int param_5 = obj.GetFront();
 * int param_6 = obj.GetRear();
 * bool param_7 = obj.IsEmpty();
 * bool param_8 = obj.IsFull();
 */