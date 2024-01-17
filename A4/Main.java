package A4;

public class Main {
    public static void main(String[] args) {
        Cykel cykel1 = new Cykel();
        cykel1.gears = 5;
        cykel1.weight = 15;
        cykel1.colour = "Black";
        cykel1.price = 5000;
        Bil bil1 = new Bil();
        bil1.weight = 1000;
        bil1.registration = "ABC12D";
        bil1.colour = "Gray";
        bil1.price = 150000;
        bil1.consumption = 5;
        cykel1.printInfo(args);
        bil1.printInfo(args);
    }
}
