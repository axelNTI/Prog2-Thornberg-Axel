package A9;

import javax.swing.*;
import java.util.*;
import java.awt.*;

public class Dummy implements Entity {

  private final ImageIcon image = new ImageIcon("A9/unknown.gif");

  protected Point position;

  protected Pasture pasture;

  public Dummy(Pasture pasture) {
    this.pasture = pasture;
  }

  public Dummy(Pasture pasture, Point position) {
    this.pasture = pasture;
    this.position = position;
  }

  public Point getPosition() {
    return position;
  }

  public void setPosition(Point newPosition) {
    position = newPosition;
  }

  public void tick() {

    Random rand = new Random();
    setPosition(new Point((int) getPosition().getX() + rand.nextInt(3) - 1, (int) getPosition().getY() + rand.nextInt(3)
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
    System.out.println("New Position: " + getPosition());
  }

  public String type() {
    return "Dummy";
  }

  public ImageIcon getImage() {
    return image;
  }
}
