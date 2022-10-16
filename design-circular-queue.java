class MyCircularDeque {
    int last;
    int size;
    int deque[];
        
    
    public MyCircularDeque(int k) {
        deque = new int[k];
        for(int i = 0; i < k; i++)
            deque[i] = 0;
        last = 0;
        size = k;
    }
    
    public boolean insertFront(int value) {
         if(last < size){
            for(int i =  last; i > 0; i--)
                deque[i] = deque[i -1];
            deque[0] = value;
            last++;
            return true;}
        else return false;
    }
    
    public boolean insertLast(int value) {
         if(last < size){
            deque[last] = value;
            last++;
            return true;}
        else return false;
                
        
    }
    
    public boolean deleteFront() {
        if(last > 0){
            for(int i = 1; i < last; i++){
                
                deque[i-1] = deque[i];
                
            }
            deque[last-1] = 0;
            last--;
            return true;
        }
        return false;
        
    }
    
    public boolean deleteLast() {
        if(last > 0){
            deque[last-1] = 0;
            last--;
            return true;
        }
        else return false;
    }
    
    public int getFront() {
         if(last > 0)
            return deque[0];
        else return -1;
    }
    
    public int getRear() {
        if(last > 0)
            return deque[last-1];
        else return -1;

    }
    
    public boolean isEmpty() {
        if(last == 0)
            return true;
        else
            return false;
    }
    
    public boolean isFull() {
        if(last == size)
            return true;
        else return false;
    }
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque obj = new MyCircularDeque(k);
 * boolean param_1 = obj.insertFront(value);
 * boolean param_2 = obj.insertLast(value);
 * boolean param_3 = obj.deleteFront();
 * boolean param_4 = obj.deleteLast();
 * int param_5 = obj.getFront();
 * int param_6 = obj.getRear();
 * boolean param_7 = obj.isEmpty();
 * boolean param_8 = obj.isFull();
 */
