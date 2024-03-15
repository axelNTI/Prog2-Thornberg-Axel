package A9;

import java.awt.Point;
import javax.swing.ImageIcon;

public class Wolf extends Animal {
    private final ImageIcon image = new ImageIcon("A9/wolf.gif");
    private Pasture pasture;
    private Point position;
    private int maxFood;
    private int currentFood;
    private String type;
    private double ticks;
    public Boolean mature = false;

    public Wolf(Pasture pasture, Point position) {
        super(position, new javax.swing.ImageIcon("A9/wolf.gif"), "Wolf", pasture, 20);
    }

    public String type() {
        return "Wolf";
    }

    public ImageIcon getImage() {
        return image;
    }

    // return food type
    public String getFoodType() {
        return "Sheep";
    }

    public void tick() {
        ticks++;
        if (ticks % 10 == 0) {
            hunger();
        }
        if (ticks % 2 == 0) {
            move();
        }
        if (ticks > 30) {
            mature = true;
        }
    }

    public Boolean maturity() {
        return mature;
    }
}
