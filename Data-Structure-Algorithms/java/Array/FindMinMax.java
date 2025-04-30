public class FindMinMax {
 public static void main(String[] args) {
    /*
     * Create a program that reads 10 integers into an array and finds
     * the maximum and minimum elements without using built-in methods.
     */
    int[] numbers = {3,4,23,11,5,8,90,2314,1,2};
    int min=0;
    int max=0;
    for(int index = 0;index < numbers.length ;index++){
        int currentValue =numbers[index];
        if (index==0)
        {
            min=currentValue;
            max=currentValue;
            continue;
        }
        if(min > currentValue)
            min = currentValue;
        
        if(max <currentValue)
            max = currentValue;
    }
    System.out.println("max value :"+max +"\n" +"Min value :" +min);
 }   
}
