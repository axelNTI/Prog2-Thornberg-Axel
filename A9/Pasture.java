package A9;

import java.util.Collection;
import java.util.Collections;
import java.util.HashSet;
import java.util.Iterator;
import java.util.MissingResourceException;
import java.util.Set;
import javax.swing.Timer;
import java.awt.event.*;
import java.lang.reflect.Array;
import java.awt.*;
import java.util.ArrayList;

public class Pasture implements ActionListener {

    /** A reference to use when setting the speed. */
    private final int SPEED_REFERENCE = 1000;
    /** The entities that this pasture contains. */
    private Set world = Collections.synchronizedSet(new HashSet());
    /** The speed of this simulation. */
    private int speed = 10;
    /** The timer that triggers ticks to be sent out to the entities. */
    private Timer timer = new Timer(SPEED_REFERENCE / speed, this);
    /** The width of this pasture */
    private int width = 25;
    /** The height of this pasture */
    private int height = 20;

    private PastureGUI gui;

    public Pasture(PastureGUI gui) {
        this.gui = gui;
        for (int i = 0; i < 50; i++) {
            try {
                Point position = new Point((int) (Math.random() * width),
                        (int) (Math.random() * height));
                Entity plant = new Plant(this, position);
                addEntity(plant);
            } catch (MissingResourceException pe) {
                System.err.println("Pasture.initPasture(): " + pe.getMessage());
                System.exit(20);
            }
        }
        for (int i = 0; i < 15; i++) {
            try {
                Point position = new Point((int) (Math.random() * width),
                        (int) (Math.random() * height));
                Entity sheep = new Sheep(this, position);
                addEntity(sheep);
            } catch (MissingResourceException pe) {
                System.err.println("Pasture.initPasture(): " + pe.getMessage());
                System.exit(20);
            }
        }
        for (int i = 0; i < 4; i++) {
            try {
                Point position = new Point((int) (Math.random() * width),
                        (int) (Math.random() * height));
                Entity wolf = new Wolf(this, position);
                addEntity(wolf);
            } catch (MissingResourceException pe) {
                System.err.println("Pasture.initPasture(): " + pe.getMessage());
                System.exit(20);
            }
        }
    }

    public void actionPerformed(ActionEvent e) {

        ArrayList<Entity> deadArray = new ArrayList<>();
        ArrayList<Entity> plantArray = new ArrayList<>();
        ArrayList<Entity> sheepArray = new ArrayList<>();
        ArrayList<Entity> wolfArray = new ArrayList<>();
        Iterator<Entity> it = world.iterator();
        while (it.hasNext()) {
            Entity entity = it.next();
            entity.tick();
            if (entity instanceof Plant) {
                plantArray.add(entity);
            }
            if (entity instanceof Sheep) {
                sheepArray.add(entity);
            }
            if (entity instanceof Wolf) {
                wolfArray.add(entity);
            }
        }
        for (Entity sheep : sheepArray) {
            Animal animal = (Animal) sheep;
            for (Entity plant : plantArray) {
                if (sheep.getPosition().equals(plant.getPosition())) {
                    animal.maxFood();
                    deadArray.add(plant);
                }
            }
            if (animal.getFood() <= 0) {
                deadArray.add(sheep);
            }
            for (Entity otherSheep : sheepArray) {
                Animal otherAnimal = (Animal) otherSheep;
                if (sheep.getPosition().equals(otherSheep.getPosition()) && sheep != otherSheep && animal.maturity()
                        && otherAnimal.maturity()) {
                    Point pos = sheep.getPosition();
                    Entity newSheep = new Sheep(this, pos);
                    addEntity(newSheep);
                }
            }
        }
        for (Entity wolf : wolfArray) {
            Animal animal = (Animal) wolf;
            for (Entity sheep : sheepArray) {
                if (wolf.getPosition().equals(sheep.getPosition())) {
                    animal.maxFood();
                    deadArray.add(sheep);
                }
            }
            if (animal.getFood() <= 0) {
                deadArray.add(wolf);
            }
            for (Entity otherWolf : wolfArray) {
                Animal otherAnimal = (Animal) otherWolf;
                if (wolf.getPosition().equals(otherWolf.getPosition()) && wolf != otherWolf && animal.maturity()
                        && otherAnimal.maturity()) {
                    Point pos = wolf.getPosition();
                    Entity newWolf = new Wolf(this, pos);
                    addEntity(newWolf);
                }
            }
        }

        for (Entity entity : deadArray) {
            removeEntity(entity);
        }
        gui.updateAll();
    }

    public void addEntity(Entity entity) {
        synchronized (world) {
            world.add(entity);
        }
    }

    public Collection getEntities() {
        HashSet currentWorld = new HashSet();

        synchronized (world) {
            Iterator it = world.iterator();

            while (it.hasNext())
                currentWorld.add(it.next());
        }

        return currentWorld;
    }

    public void removeEntity(Entity entity) {
        synchronized (world) {
            world.remove(entity);
        }
    }

    public void start() {

        timer.start();
    }

    public void stop() {
        timer.stop();
    }

    public int getWidth() {
        return width;
    }

    public int getHeight() {
        return height;
    }
}
