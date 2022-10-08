import java.util.Stack;
class Solution {
    public String reverseParentheses(String s) {
        Stack<String> stk  = new Stack<String>();
        String result = "";
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) != ')')
                stk.push(s.charAt(i) + "");
            else{
                while(!(stk.peek().equals("(")))
                    result = result + stk.pop();
                stk.pop();
                for(int j = 0; j < result.length(); j ++)
                    stk.push(result.charAt(j)+"");
                result = "";
   
            }
        }
        String rev = "";
        while(!stk.empty()){
            rev =  stk.pop() + rev;
        }
        return rev;
        
    }
}
