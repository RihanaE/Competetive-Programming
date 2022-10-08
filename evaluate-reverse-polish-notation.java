import java.util.Stack;
class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stk = new Stack<Integer>();
        for(int i = 0; i < tokens.length ;i++){
            if (!(tokens[i].equals("+") || tokens[i].equals("-") || tokens[i].equals("*") || tokens[i].equals("/"))){
                stk.push(Integer.parseInt(tokens[i]));}
            else{
                int latter  = stk.pop(), former = stk.pop();
                switch(tokens[i]){
                    case "+":stk.push(former + latter);
                             break;
                    case "-":stk.push(former - latter);
                             break;
                    case "*":stk.push(former * latter);
                             break;
                    case "/": stk.push(former / latter);
                             break;
                }
            }
            
        }
    return stk.peek();   
        
    }
}
