class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        vector<int> bskt1, bskt2;
        int strt = 0, end = 0, total = 0;
        int next = 1;
        while(strt < fruits.size()){
            end =  strt;
            while(end < fruits.size()){
                if(bskt1.size() == 0 || (bskt1.size() > 0 && bskt1.back() ==  fruits[end])){
                    bskt1.push_back(fruits[end]);
                    if(bskt2.size() == 0)
                        next++;
                }
                else if(bskt2.size() == 0 || (bskt2.size() > 0 && bskt2.back() ==  fruits[end])){
                    bskt2.push_back(fruits[end]);
                }
                else{
                    strt = next;
                    break;
                }
                
                if(end > strt && fruits[end-1] != fruits[end]){
                    next  = end; 
                    }
                end++;
        } 
        strt = next;
        if(total < bskt1.size()+bskt2.size())
            total = bskt1.size()+bskt2.size();
        bskt1.clear();
        bskt2.clear();   
            
        if(end  == fruits.size())
            break;  
        }
        return total;
    }
};
