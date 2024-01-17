package A5;

public class Boss extends Enemy {
    public Boss(double health) {
        super(health);
    }

    public void takeDamage(double damage) {
        this.hp -= (damage / 2);
    }
}
