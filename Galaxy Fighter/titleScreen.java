import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class titleScreen here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class titleScreen extends World
{

    /**
     * Constructor for objects of class titleScreen.
     * 
     */
    
    
    public titleScreen()
    {    
        // Create a new world with 600x400 cells with a cell size of 1x1 pixels.
        super(1200, 700, 1); 
        GreenfootImage bg = new GreenfootImage("Title Screen.png");
        bg.scale(getWidth(), getHeight());
        setBackground(bg);
        
        
    }
     public void act() 
{
    if (Greenfoot.isKeyDown("enter")) 
            Greenfoot.setWorld(new Stage1());
    
}
}
