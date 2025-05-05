import java.util.Arrays;

public class NoDuplicates {

    public int[] removeDuplicates(int[] input){
       
        // First sort the values in the input
        Arrays.sort(input);
        int[] temp = new int[input.length];
        int counter = 0;
        temp[counter] =input[counter];
        for( int index =1; index < input.length;index++){
            if (input[index] != temp[counter]) {
                temp[++counter] = input[index];
            }
        }
        return Arrays.copyOfRange(temp, 0, counter+1);
    }
    public static void main(String[] args) {
        /*
         * Write a Java method that takes an integer array and returns a new array containing only the unique elements (no duplicates).
         */

        int[] input = {1,4,4,4,77,3,2,34,2,5,6,9};
        NoDuplicates objRef = new NoDuplicates();
        int[] duplicatesRemoved = objRef.removeDuplicates(input);
        for(int val:duplicatesRemoved){
            System.out.println(val);
        }

    }
}
