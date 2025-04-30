import java.util.Scanner;

public  class ReverseOrder{
    public static void main(String [] args){
        /*
            Write a Java program to create an array of five integers, input values from the user, and print them in reverse order.
        */
        Scanner io = new Scanner(System.in);
        int numbers[] = new int[5];

        for(int index =0;index < numbers.length;index++){
            numbers[index] = io.nextInt();
        }

        io.close();

        for(int index =numbers.length - 1;index >= 0;index--){
            System.out.println(numbers[index]);
        }  
         
    }
}