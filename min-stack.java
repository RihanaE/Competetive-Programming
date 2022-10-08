import java.util.Stack;
class MinStack {
    private int size;
    private Stack<Integer> stk, min;
    public MinStack() {
        size = 0;
        stk = new Stack<Integer>();
        min =  new Stack<Integer>();

        
    }
    
    public void push(int val) {
        stk.push(val);
        size++;
        if(size == 1)
            min.push(stk.peek());
        else if(size > 1){
            if(min.peek() >= stk.peek())
                min.push(stk.peek());
        }
        
    }
    
    public void pop() {
        int i = stk.peek();
        stk.pop();
        size--;
        if(i == min.peek())
            min.pop();
        
    }
    
    public int top() {
        return stk.peek();
        
    }
    
    public int getMin() {
        return min.peek();
        
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
