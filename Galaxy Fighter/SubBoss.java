import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class SubBoss here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class SubBoss extends Actor
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
        Ship s = x;//This is to set up which ship will be used, which could be useful later
    }
    public void setLevel (int l) {
        level = l;
    }
    //These time vairables will help us know 
    long lastLaser = System.currentTimeMillis();
    long newLaser;
    long lastRocket = System.currentTimeMillis();
    long newRocket;
    int health = 50;
    public void act() 
    {
        
        int mobil = Greenfoot.getRandomNumber(15);
        ifHit();
        movement(mobil);
        newLaser = System.currentTimeMillis();//We'll be setting our newLaser variable in order to compare it with lastLaser variable 
        shoot(mobil, newLaser);
        newRocket = System.currentTimeMillis();//We'll be setting our newRocket variable in order to compare it with lastRocket variable
        fire(mobil, lastRocket, newRocket);
        if (health <= 0) {//If the boss' health becomes 0, remove it from the world and take the player to the Credits screen
            getWorld().removeObject(this);
            Greenfoot.delay(50);
            Greenfoot.setWorld(new Credits ());
        }
            
        }
        
        public void ifHit() {
            //Basically if the it gets hit by a laser, the Boss's health decreases and the laser disappears
            Actor l = getOneIntersectingObject(SubBoss.class);
            if (l != null) {
                health--;
                getWorld().removeObject(l);
                
            }
            
        }
        public void setStartLoc (int  s) {
    startlocY = s;
}
public void movement(int mobil) {//This method works almost exactly the same way as the Level1Enemy
    if (mobil >= 0 && mobil < 4 && !(getX() <= (1000))) {
            move(-10);

        }
    else if (mobil >= 4 && mobil < 8 && !(getX() >= (1200))) {
            move(10);
            
        }
    else if (mobil >= 8 && mobil < 12 && ! (getY() >= 650) ){
            setLocation(getX(), getY()+10);
            
        }
    else if (mobil >= 12 && mobil < 15 && ! (getY() <= 50 ) ){
            setLocation(getX(), getY()-10);
            
        }
        
    }
    public void shoot(int mobil, long newLaser) {//This is essentially a cleaner version of the Level1Enemy Classes 
        if( ((mobil > 0 && mobil < 3) || (mobil > 4 && mobil < 7) || (mobil > 8 && mobil < 11) || (mobil > 12 && mobil < 14))&& newLaser >= (lastLaser +500) ) {
                
                getWorld().addObject(new bossEnemyLaser(this, s), getX(), getY() + 20);
                lastLaser = System.currentTimeMillis();
   }
  
    }
    public void fire(int mobil, long newRocket, long lastRocket) {
        if( mobil > 5 && mobil < 10 && newRocket >= (lastRocket +1000) ) {//If the mobil number is between 5 and 10 and enough time has passed
                
                getWorld().addObject(new Rocket(this, s), getX(), getY() + 20);
                lastRocket = System.currentTimeMillis();
   }
 
    }
}

