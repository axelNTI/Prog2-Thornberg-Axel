package A9;

import java.awt.Point;
import javax.swing.ImageIcon;

public class Plant extends LivingThing {

    private ImageIcon image;

    public Plant(Pasture pasture, Point position) {
        super(position, new javax.swing.ImageIcon("plant.gif"), "Plant");
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
