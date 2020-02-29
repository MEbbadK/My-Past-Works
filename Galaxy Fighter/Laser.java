import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Laser here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Laser extends Ship
{
    /**
     * Act - do whatever the Laser wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    {
    GreenfootImage image = getImage();
    image.scale(image.getWidth(), image.getHeight());
    setImage(image);
}
private Ship s = new Ship();    
public Laser (Ship x) {
    s = x;
    }
    public void act() 
    {
        setLocation(getX() + 50, getY());//Keep the laser moving 50 pixels to the right each act
        deleteCondition();
    }    
    public void deleteCondition()  
    {
        Actor b = getOneIntersectingObject(Level1Enemy.class);//Create an actor that's a Level1Enemy interacting the laser
               
        World world = getWorld();
        if(b != null)//If there is a level1ENemy interacting with it 
        {      
            //Increase the player's kill counter
            s.setKillCounter(1);
            //Remove the enemy
            getWorld().removeObject(b);
            //Remove this laser
            getWorld().removeObject(this);
        }
        else if(getX() > getWorld().getWidth() - 10) {//If the laser gets close enought to the world's edge
            getWorld().removeObject(this);//Remove the laser
        }
    }
}

