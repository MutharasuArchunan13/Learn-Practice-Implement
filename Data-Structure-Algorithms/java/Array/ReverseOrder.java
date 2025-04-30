import java.util.Scanner;

public  class ReverseOrder{
    public static void main(String [] args){
        /*
            Write a Java program to create an array of five integers, input values from the user, and print them in reverse order.
        */
        Scanner io = new Scanner(System.in);
        System.out.println("Enter how many numbers you want input");
        int size = io.nextInt();

        if (size <= 0) {
            System.out.println("Invalid array size. Must be positive.");
            io.close();
            return;
        }

        int numbers[] = new int[size];

        System.out.println("Enter "+size + "of integer inputs");
        for(int index =0;index < numbers.length;index++){
            while(!io.hasNextInt()){
                System.out.println("Invalid input, give me corrected integer value");
                io.next();
            }

            numbers[index] = io.nextInt();
        }

        io.close();

        for(int index =size - 1;index >= 0;index--){
            System.out.println(numbers[index]);
        }  
         
    }
}