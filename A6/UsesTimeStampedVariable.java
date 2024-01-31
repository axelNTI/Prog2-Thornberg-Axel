import java.util.Scanner;

// UsesTimeStampedVariable.java
public class UsesTimeStampedVariable {

    public static void main(String[] args) {
        TimeStampedVariable<String> minVariabel1 = new TimeStampedVariable<String>("AB");
        TimeStampedVariable<Integer> minVariabel2 = new TimeStampedVariable<Integer>(5);
        TimeStampedVariable<Double> minVariabel3 = new TimeStampedVariable<Double>(3.14);

        Scanner variableScanner = new Scanner(System.in);
        System.out.println("Enter the new variable");
        minVariabel1.updateVariable(variableScanner.nextLine());
        variableScanner.close();

        System.out.println("minVariabel1 ändrades: " + minVariabel1.getTimeStamp());
        System.out.println("minVariabel2 ändrades: " + minVariabel2.getTimeStamp());
        System.out.println("minVariabel3 ändrades: " + minVariabel3.getTimeStamp());

        minVariabel1.printVariable();
        minVariabel2.printVariable();
        minVariabel3.printVariable();

    }
}
