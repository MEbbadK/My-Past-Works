import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Stage3Continued here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Stage3Continued extends World
{

    /**
     * Constructor for objects of class Stage3Continued.
     * 
     */
    public Stage3Continued(Ship p , int x, int y)
    {    
        // Create a new world with 600x400 cells with a cell size of 1x1 pixels.
        super(1200, 700, 1);
        Ship s = p;
        s.changeHealth(100);
        addObject(s, x, y);
        Level1Enemy [] l = new Level1Enemy[2];//I'll create an array of my level one enemies
        int goonLoc = 350;//I set up the location on the y-axis for the sub boss
        int [] startlocy = new int [2];//Create array for storing the enemies location on the x-axis
        SubBoss sb = new SubBoss(); 
        addObject(sb, 900, 350);
        sb.setStartLoc(sb.getX());
    }
}
