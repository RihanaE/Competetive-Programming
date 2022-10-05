
class Solution
{
	int  select(int arr[], int i)
	{
        // code here such that selectionSort() sorts arr
        int min = i;
        for(int j = i; j<arr.length;j++){
            if(arr[j] < arr[min])
                min = j;
            
        }
        return min;
	}
	
	void selectionSort(int arr[], int n)
	{
	    //code here
	    int temp;
	    for(int i = 0; i < n; i++){
	        temp = arr[i];
	        int ind = select(arr, i);
	        arr[i] = arr[ind];
	        arr[ind] = temp;
     
	    }
	    
	}
}
