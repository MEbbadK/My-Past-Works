import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)
import java.util.Random;
/**
 * Write a description of class Level1Enemy here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Level1Enemy extends Actor
{
    /**
     * Act - do whatever the Level1Enemy wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    {
    GreenfootImage image = getImage();
    image.scale(image.getWidth()/2, image.getHeight()/2);
    setImage(image);
}
    private int startlocY;
    private int level;
    private Ship s;
    public void setShip (Ship x) {
        Ship s = x;
    }
    public void setLevel (int l) {
        level = l;
    }
    //These 2 variables will help me make space between the times the enemy shoots
    long lastAdded = System.currentTimeMillis();
    long newLaser;
    public void act() 
    {
        
        int mobil = Greenfoot.getRandomNumber(15);//This number will help randomize the enemy movements
        if (mobil >= 0 && mobil < 4 && !(getX() <= (1000))) {//If the number is between 0 and 4, move ahead
            move(-10);
            newLaser = System.currentTimeMillis();
            if((level >= 2) && mobil > 0 && mobil < 3 && newLaser >= (lastAdded +500) ) {//If the level is 2 or greater and if enough time has passed, shoot slowly at the player 
                
                getWorld().addObject(new EnemyLaser(this, s), getX(), getY());
                lastAdded = System.currentTimeMillis();
   }
        }
        else if (mobil >= 4 && mobil < 8 && !(getX() >= (1200))) {//If the number is between 4 and 8, move ahead
            move(10);
            newLaser = System.currentTimeMillis();
            if((level >= 2) && mobil > 4 && mobil < 7 && newLaser >= (lastAdded +500)) {//If the level is 2 or greater and if enough time has passed, shoot slowly at the player
                
                getWorld().addObject(new EnemyLaser(this, s), getX(), getY());
                lastAdded = System.currentTimeMillis();
   }
        }
        else if (mobil >= 8 && mobil < 12 && ! (getY() >= (startlocY + 50))) {//If the number is between 0 and 4, move ahead
            setLocation(getX(), getY()+10);
            newLaser = System.currentTimeMillis();
            if((level >= 2) && mobil > 8 && mobil < 11 && newLaser >= (lastAdded +500)) {//If the level is 2 or greater and if enough time has passed, shoot slowly at the player
                
               
                getWorld().addObject(new EnemyLaser(this, s), getX(), getY());
                lastAdded = System.currentTimeMillis();
   }
        }
        else if (mobil >= 12 && mobil < 15 && ! (getY() <= (startlocY - 50)) ) {
            setLocation(getX(), getY()-10);
            newLaser = System.currentTimeMillis();
            if((level >= 2) && mobil > 12 && mobil < 14 && newLaser >= (lastAdded +500)) {//If the level is 2 or greater and if enough time has passed, shoot slowly at the player
                
                
                getWorld().addObject(new EnemyLaser(this, s), getX(), getY());
                lastAdded = System.currentTimeMillis();
   }
        }
}

public void setStartLoc (int  s) {
    startlocY = s;
}

    }