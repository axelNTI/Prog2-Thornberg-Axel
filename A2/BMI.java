package A2;

import java.util.Scanner;

public class BMI {

    public static void main(String[] args) {
        Scanner inputWeightScanner = new Scanner(System.in);
        System.out.println("Enter your weight in kilograms");
        double weight = inputWeightScanner.nextLine();
        Scanner inputHeightScanner = new Scanner(System.in);
        System.out.println("Enter your height in meters");
        double height = inputHeightScanner.nextLine();
        double BMI = weight / Math.pow(height, 2);
        System.out.println("Your BMI is" + BMI);
    }

}
