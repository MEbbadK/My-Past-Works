import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class EnemyLaser here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class EnemyLaser extends Level1Enemy
{
    /**
     * Act - do whatever the EnemyLaser wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    {
    GreenfootImage image = getImage();
    image.scale(image.getWidth(), image.getHeight());
    setImage(image);
}
private Ship s = new Ship();
private Level1Enemy l = new Level1Enemy();
public EnemyLaser (Level1Enemy L1E, Ship x) {
    s = x;
    l = L1E;
    }
    public void act() 
    {
        setLocation(getX() - 50, getY());
        if (getX() == 0) {
            getWorld().removeObject(this);
        }
    }    
}