import java.util.Stack;
class MyQueue {
   private Stack<Integer> stack;
    private Stack<Integer> queue;
    private int size;

    public MyQueue() {
        stack = new Stack<Integer>();
        size = 0;
    }
    private Stack<Integer> toQueue(Stack<Integer> stk){
        Stack<Integer> q =  new Stack<Integer>();
        Stack<Integer> s =  new Stack<Integer>();
        while (!stk.empty()){
            int last =  stk.pop();
            q.push(last);
            s.push(last);
        }
        while (!s.empty()){
            int last =  s.pop();
            stk.push(last);
        }
        return q;
    }

    public void push(int x) {
        stack.push(x);
        size++;
        queue = toQueue(stack);
        System.out.println(stack.toString());
    }
    
    public int pop() {
       
            int i = queue.peek();
            queue.pop();
            stack = toQueue(queue);
            size--;
            return i;
    }
    
    public int peek() {
        return queue.peek();
    }
    
    public boolean empty() {
        if (size == 0)
            return true;
        else
            return false;
        
    }
}
