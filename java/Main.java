import java.util.List;
import java.util.Stack;

import org.json.JSONException;
import org.json.JSONObject;
import java.lang.Math;
import java.lang.Integer;

public class Main {
    public static void main(String[] args) {
        System.out.println("Starting program...");   
        IsPalindrome palindrome = new IsPalindrome();
        //boolean response = palindrome.checkIsPalindrome("racecar");

        TwoSumSorted twoSumSorted = new TwoSumSorted();
        //int[] nums = {1, 2, 4, 6, 8, 9, 14, 15};
        //boolean response = twoSumSorted.twoSumSorted(nums,13);

        TwoSortedArraysIntoOne twoSortedArraysIntoOne = new TwoSortedArraysIntoOne();
        int[] arr1 = {1,4,7,20};
        int[] arr2 = {3,5,6};
        //List<Integer> response = twoSortedArraysIntoOne.twoSortedArraysIntoOne(arr1, arr2);

        IsSubsequence isSubsequence = new IsSubsequence();
        boolean response  = isSubsequence.isSubsequence("ace", "abcde");

        //String response = reverseWords("This is the first sentence.  This is the second.");
        //String response = smallestSubsequence("bcabc");
        System.out.println(response);
        System.out.println("Finishing program...");   

    }

    /*public static String smallestSubsequence(String s) {
           
    }*/

    public static String spinWords(String sentence) {
        //TODO: Code stuff here
        String [] words = sentence.split(" ");

        for(int i=0; i < words.length; i++){
            if(words[i].toCharArray().length >= 5){
                words[i] = new StringBuilder(words[i]).reverse().toString();
            }
        }

        return String.join(" ", words);
      }

    public static boolean isPrime(int num) {   
        if(num <= 1) return false;
        
        for(int i=2; i <= Math.round(Math.sqrt(num)+1) ; i++){
            if((num % i) == 0 && num != i){
                return false;
            }
        }
        
        return true; 
    }

    public static String reverseWords(final String original) {
        String[] words = original.split(" ");
    
        if(words.length == 0) return original;

        int i = 0;
        for(String word : words){
            words[i] = new StringBuilder(word).reverse().toString();
            i++;
        }

        return String.join(" ",words);
    }

    public static void exampleCompiler(){
        boolean valid = validatorCompiler("[()]{}");
        if(valid){
            System.out.println("Valid");
        } else {
            System.out.println("Not Valid");
        }
    }

    public static boolean validatorCompiler(String cadena){
        boolean isValid = false;
        Stack<Character> pila = new Stack<>();

        for(char c: cadena.toCharArray()){
            //System.out.println(c);
            if(c == '(' || c == '{' || c == '['){
                pila.push(c);
            } else if (c == ')' || c == '}' || c == ']'){
                if(pila.isEmpty()){
                    return false;
                }
                char open = pila.pop();
                if(( c == ')' && open != '(' ) || ( c == ']' && open != '[' ) || ( c == '}' && open != '{' )  ){
                    return false;
                }
            }
        }

        return pila.isEmpty();
    }

    public static void testingJson(){
        JSONObject json = new JSONObject();
		try {
            json.put("fromDate", JSONObject.NULL);
            json.put("toDate", "12/12/2023");
            JSONObject wccFilters = new JSONObject();
		    wccFilters.put("wccFilters", json);
            System.out.println(wccFilters.get("wccFilters").toString());
            System.out.println(json.toString());
        } catch (JSONException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

    }

}