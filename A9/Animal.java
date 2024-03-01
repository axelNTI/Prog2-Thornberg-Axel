package A9;

import java.awt.Point;
import java.util.Random;

import javax.swing.ImageIcon;

public abstract class Animal extends LivingThing {

    // Variables for maxFood and currentFood

    private int maxFood;
    private int currentFood;
    private Pasture pasture;

    public Animal(Point position, ImageIcon image, String type, Pasture pasture, int maxFood) {
        super(position, image, type);
        this.maxFood = maxFood;
        this.currentFood = maxFood;
    }

    // Reduce currentFood by 1 each tick
    public void tick() {
        currentFood--;
        Random rand = new Random();
        setPosition(
                new Point((int) getPosition().getX() + rand.nextInt(3) - 1, (int) getPosition().getY() + rand.nextInt(3)
                        - 1));
        if (getPosition().getX() < 0) {
            setPosition(new Point((int) 0, (int) getPosition().getY()));
        }
        if (getPosition().getX() > 24) {
            setPosition(new Point((int) 24, (int) getPosition().getY()));
        }
        if (getPosition().getY() < 0) {
            setPosition(new Point((int) getPosition().getX(), (int) 0));
        }
        if (getPosition().getY() > 19) {
            setPosition(new Point((int) getPosition().getX(), (int) 19));
        }
    }

    // Sets food to maxFood
    public int getFood() {
        return currentFood;
    }

    public abstract String getFoodType();
}
