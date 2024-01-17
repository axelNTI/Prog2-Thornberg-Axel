package A5;

public abstract class Fordon {
    double weight;
    double price;
    String colour;

    public void printInfo(String[] args) {
        System.out.println(weight);
        System.out.println(colour);
        System.out.println(price);
    }
}
