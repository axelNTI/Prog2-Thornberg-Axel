package A9;

import java.awt.Point;
import javax.swing.ImageIcon;

public class Sheep extends Animal {

    private final ImageIcon image = new ImageIcon("A9/sheep.gif");
    private Pasture pasture;
    private Point position;
    private int maxFood;
    private int currentFood;
    private String type;
    private double ticks;
    public Boolean mature = false;

    public Sheep(Pasture pasture, Point position) {
        super(position, new javax.swing.ImageIcon("A9/sheep.gif"), "Sheep", pasture, 10);
    }

    public String type() {
        return "Sheep";
    }

    public ImageIcon getImage() {
        return image;
    }

    // return food type
    public String getFoodType() {
        return "Plant";
    }

    public void tick() {
        ticks++;
        if (ticks % 5 == 0) {
            hunger();
        }
        if (ticks % 5 == 0) {
            move();
        }
        if (ticks > 20) {
            mature = true;
        }
    }

    public Boolean maturity() {
        return mature;
    }

}
