public static int countingValleys(int steps, String path) {
        int p = 0, count = 0;
        for(int i = 0; i < steps; i++){
            if(path.charAt(i) == 'U'){
                p++;
                if(p == 0)
                    count++;
            }
                
            else
                p--;
        }
        return count;
    }an
