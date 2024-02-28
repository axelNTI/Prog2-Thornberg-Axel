package A9;

import java.awt.Point;
import javax.swing.ImageIcon;

public class Plant extends LivingThing {

    private final ImageIcon image = new ImageIcon("A9/plant.gif");
    // private ImageIcon image;

    public Plant(Pasture pasture, Point position) {
        super(position, new javax.swing.ImageIcon("A9/plant.gif"), "Plant");
    }

    public void tick() {
    }

    public String type() {
        return "Plant";
    }

    public javax.swing.ImageIcon getImage() {
        return image;
    }

}
