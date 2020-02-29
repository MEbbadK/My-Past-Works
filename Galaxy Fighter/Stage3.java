import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Stage3 here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Stage3 extends World
{

    /**
     * Constructor for objects of class Stage3.
     * 
     */
    public Stage3(Ship p , int x, int y)
    {    
        // Create a new world with 600x400 cells with a cell size of 1x1 pixels.
        super(1200, 700, 1);
        Ship s = p;
        s.changeHealth(10);
        addObject(s, x, y);
        Level1Enemy [] l = new Level1Enemy[2];//I'll create an array of my level one enemies
        int goonLoc = 600;//I set up the location on the y-axis for the enemies
        int [] startlocy = new int [2];//Create array for storing the enemies location on the x-axis
        
        for (int i = 0; i < 2; i++) {//Create a for loop for adding enemies
            l[i] = new Level1Enemy();
            addObject(l[i], 1100, goonLoc);//Set the enemy at 1100 on the x-axis and whatever goonLoc is on the y-axis
            startlocy[i] = l[i].getY();//Store the value for y value for the enemies location at their respective indexes
            goonLoc = goonLoc - 300;//I decreased goonLoc so they'll spawn 150 pixels away from each other, vertically 
        }
        for (int i = 0; i < 2; i++) {
            l[i].setStartLoc(startlocy[i]);//Set the y start location for each object at the Level1Enemy class
            l[i].setLevel(2);//Telling the enemies what level it is to ramp up the difficulty
            l[i].setShip(s);
        }
    }
}
