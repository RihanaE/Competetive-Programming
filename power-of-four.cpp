class Solution {
public:
    bool isPowerOfFour(int n) {
        if(n >1  &&  n%4 != 0)
            return false;
        else if(n == 0 || n ==1)
            return (n == 0) ?false : true;
        else if(n == 4)
            return true;
        else
            return isPowerOfFour(n/4);
        
    }
};
