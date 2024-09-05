import java.util.ArrayList;
import java.util.List;

public class TwoSortedArraysIntoOne {
 
    
    public List<Integer> twoSortedArraysIntoOne(int[] arr1, int[] arr2){
        int i = 0;
        int j = 0;
        List<Integer> ans = new ArrayList<>();

        while(i < arr1.length &&  j< arr2.length){
            if(arr1[i] < arr2[j]){
                ans.add(arr1[i]);
                i++;
            } else {
                ans.add(arr2[j]);
                j++;
            }
        }

        while(i < arr1.length){
            ans.add(arr1[i]);
            i++;
        }

        while(j< arr2.length){
            ans.add(arr2[j]);
            j++;
        }
        
        return ans;
    }
}
