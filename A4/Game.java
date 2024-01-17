package A4;

public class Game {
    public static void main(String[] args) {
        Enemy goomba = new Enemy(30); // hp är 30
        Boss bowser = new Boss(200); // hp är 200
        goomba.takeDamage(10); // fiender tar hela damagen som ges
        bowser.takeDamage(10); // bossar ska bara ta halva damagen som ges
        goomba.printHp(); // skriver ut 20 (30-10)
        bowser.printHp(); // skriver ut 195 (200-(10/2))
    }

}
