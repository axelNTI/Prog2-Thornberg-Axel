package A9;

import java.awt.Point;
import javax.swing.ImageIcon;

public abstract class LivingThing implements Entity {

    private Point position;
    private ImageIcon image;
    private String type;

    public LivingThing(Point position, ImageIcon image, String type) {
        this.position = position;
        this.image = image;
        this.type = type;
    }

    public Point getPosition() {
        return position;
    }

    public void setPosition(Point newPosition) {
        position = newPosition;
    }

    public abstract ImageIcon getImage();

    public abstract String type();

    public abstract void tick();
}
