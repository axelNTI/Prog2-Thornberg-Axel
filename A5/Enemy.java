package A5;

public class Enemy {
    double hp;

    public Enemy(double health) {
        this.hp = health;

    }

    public void printHp() {
        System.out.println(this.hp);
    }

    public void takeDamage(double damage) {
        this.hp -= damage;
    }
}
