import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Rocket here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Rocket extends SubBoss
{
    /**
     * Act - do whatever the Rocket wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    {
    GreenfootImage image = getImage();
    image.scale(image.getWidth(), image.getHeight());
    setImage(image);
}
private Ship s = new Ship();
private SubBoss sb = new SubBoss();
public Rocket (SubBoss subboss, Ship x) {
    s = x;
    sb = subboss;
    }
    public void act() 
    {
        setLocation(getX() - 50, getY());//Programming wise this act works the exact same way the enemylase act does
        if (getX() == 0) {
            getWorld().removeObject(this);
        }
    }    
}
