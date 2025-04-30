public class FindMinMax {
 public static void main(String[] args) {
    /*
     * Create a program that reads 10 integers into an array and finds
     * the maximum and minimum elements without using built-in methods.
     * 
     * Time complexity -> O(n)
     * Space complexity -> O(1)
     */
    int[] numbers = {3,4,23,11,5,8,90,2314,1,2};
    int min=numbers[0];
    int max=numbers[0];
    for(int index = 0;index < numbers.length ;index++){
        int currentValue =numbers[index];
        if (index==0)
            continue;

        if(min > currentValue)
            min = currentValue;
        
        if(max <currentValue)
            max = currentValue;
    }
    System.out.println("max value :"+max +"\n" +"Min value :" +min);
 }   
}
