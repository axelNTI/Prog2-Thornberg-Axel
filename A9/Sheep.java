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

}
