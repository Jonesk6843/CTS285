package m1hw_jones;
import java.text.DecimalFormat;
import java.util.Scanner;
/*
 * CTS 285
 * M1HW_Calculator
 * Kent Jones
 * 8/23/23
 */
public class M1HW_Jones
{
    // declare Scanner
    public static final Scanner keyboard = new Scanner(System.in);
    
    public static void main(String[] args)
    {
        //Opening Main Menu
        MainMenu();
    }
    
    public static void MainMenu()
    {
       // Declaring Variables
        int userInput;
        boolean retry = false;

        // Present user with main menu
        System.out.println("GREETINGS! I AM CALCULATORTRON!");

        // Loop main menu until vaild input is made
        while (retry = true)
        {
            System.out.println("WHAT MATHEMATICAL APPLICATION WOULD YOU LIKE TO RUN?");
            System.out.println("1. ADDITION" + "\n" +
                        "2. SUBTRACTION" + "\n" +
                        "3. MULTIPLICATION" + "\n" +
                        "4. DIVISION" + "\n" +
                        "5. EXIT");
            // Getting User Input
            System.out.print("> ");
            userInput = keyboard.nextInt();

            switch (userInput)
            {
                case 1:
                    addition();
                    break; 
                case 2:
                    subtraction();
                    break; 
                case 3:
                    multiplication();
                    break; 
                case 4:
                    division();
                    break; 
                case 5:
                    System.out.println("HAVE A NICE DAY!");
                    System.exit(0);
                default:
                    System.out.println("INVALID INPUT!");
            } 
        }    
    }
    
    public static int addition()
    {
        // Declaring Variables
        int userInput;
        float userNum1;
        float userNum2;
        Boolean repeat = false;
        DecimalFormat format = new DecimalFormat("0.#"); // Eliminates empty decimal place

        // Ask for the user's numbers.
        System.out.println("ADDITION!");
        while(repeat = true)
        {
            System.out.print("ENTER A NUMBER: ");
            userNum1 = keyboard.nextFloat();
            System.out.print("ADD IT TO: ");
            userNum2 = keyboard.nextFloat();

            // Call calculation method
            additionCalc(userNum1, userNum2);
            
            // Display answer
            System.out.println(format.format(userNum1) + " + " + format.format(userNum2) + " = " + format.format(additionCalc(userNum1, userNum2)));

           // Present option to repeat or leave.
           System.out.println("1. RETRY" + "\n" +
                        "2. MAIN MENU");
           System.out.print("> ");
           userInput = keyboard.nextInt();
           switch (userInput)
            {
                case 1:
                    repeat = true;
                    break;
                case 2:
                    MainMenu();
                    break;
                default:
                    System.out.println("ENTER VALID OPTION! RESETING ADDITION PROGRAM!");
            }
        }
        return 0;
    }

    public static int subtraction()
    {
        // Declaring Variables
        int userInput;
        float userNum1;
        float userNum2;
        Boolean repeat = false;
        DecimalFormat format = new DecimalFormat("0.#"); // Eliminates empty decimal place
        
        // Ask for the user's numbers.
        System.out.println("SUBTRACTION!");
        while(repeat = true)
        {
            System.out.print("ENTER A NUMBER: ");
            userNum1 = keyboard.nextFloat();
            System.out.print("SUBTRACT IT BY: ");
            userNum2 = keyboard.nextFloat();
            
            // Call calculation method and display answer
            System.out.println(format.format(userNum1) + " - " + format.format(userNum2) + " = " + format.format(subtractionCalc(userNum1, userNum2)));

           // Present option to repeat or leave.
           System.out.println("1. RETRY" + "\n" +
                        "2. MAIN MENU");
            System.out.print("> ");
            userInput = keyboard.nextInt();
           switch (userInput)
            {
                case 1:
                    repeat = true;
                    break;
                case 2:
                    repeat = false;  
                    MainMenu();
                default:
                    System.out.println("ENTER VALID OPTION! RESETING SUBTRACTION PROGRAM!");
            }
        }
        return 0;
}
    
    public static int multiplication()
    {
        // Declaring Variables
        int userInput;
        float userNum1;
        float userNum2;
        Boolean repeat = false;
        DecimalFormat format = new DecimalFormat("0.#"); // Eliminates empty decimal place
        
        // Ask for the user's numbers.
        System.out.println("MULTIPLICATION!");
        while(repeat = true)
        {
            System.out.print("ENTER A NUMBER: ");
            userNum1 = keyboard.nextFloat();
            System.out.print("MULTIPLY IT BY: ");
            userNum2 = keyboard.nextFloat();

            // Call calculation method and display answer
            System.out.println(format.format(userNum1) + " * " + format.format(userNum2) + " = " + format.format(multiplicationCalc(userNum1, userNum2)));

           // Present option to repeat or leave.
           System.out.println("1. RETRY" + "\n" +
                        "2. MAIN MENU");
            System.out.print("> ");
            userInput = keyboard.nextInt();
           switch (userInput)
            {
                case 1:
                    repeat = true;
                    break;
                case 2:
                    repeat = false;  
                    MainMenu();
                default:
                    System.out.println("ENTER VALID OPTION! RESETING MULTIPLICATION PROGRAM!");
            }
        }
        return 0;
}
    
    public static int division()
    {
        // Declaring Variables
        int userInput;
        float userNum1;
        float userNum2;
        Boolean repeat = false;
        DecimalFormat format = new DecimalFormat("0.#"); // Eliminates empty decimal place
        
        // Ask for the user's numbers.
        System.out.println("DIVISION!");
        while(repeat = true)
        {
            System.out.print("ENTER A NUMBER: ");
            userNum1 = keyboard.nextFloat();
            System.out.print("DIVIDED BY: ");
            userNum2 = keyboard.nextFloat();

            /// Call calculation method and display answer
            System.out.println(format.format(userNum1) + " / " + format.format(userNum2) + " = " + format.format(divisionCalc(userNum1, userNum2)));

           // Present option to repeat or leave.
           System.out.println("1. RETRY" + "\n" +
                        "2. MAIN MENU");
            System.out.print("> ");
            userInput = keyboard.nextInt();
           switch (userInput)
            {
                case 1:
                    repeat = true;
                    break;
                case 2:
                    repeat = false;  
                    MainMenu();
                default:
                    System.out.println("ENTER VALID OPTION! RESETING DIVISION PROGRAM!");
            }
        }
        return 0;
}
    
    public static float additionCalc(float num1, float num2)
    {
        //Declaring variables
        float sum;

        // Begin calculations
        sum = num1 + num2;

        // Return the sum
        return sum;
    }

    public static float subtractionCalc(float num1, float num2)
        {
            //Declaring variables
            float difference;

            // Begin calculations
            difference = num1 - num2;

            // Return the difference
            return difference;
        }

    public static float multiplicationCalc(float num1, float num2)
        {
            //Declaring variables
            float product;

            // Begin calculations
            product = num1 * num2;

            // Return the product
            return product;
        }

    public static float divisionCalc(float num1, float num2)
        {
            //Declaring variables
            float quotiant;

            // Begin calculations
            quotiant = num1 / num2;

            // Return the quotiant
            return quotiant;
        }
}
