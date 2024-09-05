public class TwoSumSorted {
    
    public boolean twoSumSorted(int[] nums,int target){
        int left = 0;
        int right = nums.length -1;
        
        while(left < right){
            int current = nums[left] + nums[right];
            if(current == target){
                return true;
            }
            if(current > target){
                right--;
            }
            if(current < target){
                left++;
            }
        }

        return false;
    }
}
