public class SortedSquares {
    

    public int[] sortedSquares(int[] nums){
        int n = nums.length;
        int left = 0; 
        int right = n-1;
        int[] res = new int[n];

        for(int i=n-1; i >=0 ; i-- ){
            int square = 0;
            if(Math.abs(nums[left]) > Math.abs(nums[right])){
                square = nums[left];
                left++;
            } else {
                square = nums[right];
                right--;
            }
            res[i] = square * square;
        }
        return res;
    }
}
