import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Ship here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Ship extends Actor
{
    /**
     * Act - do whatever the Ship wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    public Ship () {
    GreenfootImage image = getImage();
    image.scale(image.getWidth()/4, image.getHeight()/4);
    setImage(image);
}
    public int KillCounter = 0;
    public void setKillCounter(int k) {
        KillCounter = KillCounter + k;
    }
    public int health = 10;
    public void changeHealth(int h) {
        health = health + h;
    }
    public void checkHealth () {
        Actor e = getOneIntersectingObject(EnemyLaser.class);
        Actor b = getOneIntersectingObject(bossEnemyLaser.class);    
        if(e != null) {
            getWorld().removeObject(e);
            World world = getWorld();
            health = health - 1;
        }
        else if (b != null) {
            getWorld().removeObject(e);
            World world = getWorld();
            health = health - 2;
        }
       
    }
    public void act() 
{
        checkFire();//This sends the act to the method that will allow the user to shoot
        endLevel1();
        endLevel2();
        checkHealth();
        if (health <= 0 ) {
            getWorld().removeObject(this);
            Greenfoot.setWorld(new GameOver());
        }
        else if (Greenfoot.isKeyDown("right") || Greenfoot.isKeyDown("d"))//If the user presses 'right' or 'd', move 4 pixels ahead on the x-axis
        {
            move(4);
        }
        else if (Greenfoot.isKeyDown("left")|| Greenfoot.isKeyDown("a"))//If the user presses 'left' or 'a', move 4 pixels behind on the x-axis
        {
            move(-4);
        }
        else if (Greenfoot.isKeyDown("up")|| Greenfoot.isKeyDown("w"))//If the user presses 'up' or 'w', move 4 pixels up on the y-axis
        {
            setLocation(getX(), getY()-4);
        }
        else if (Greenfoot.isKeyDown("down")|| Greenfoot.isKeyDown("s"))//If the user presses 'down' or 's', move 4 pixels down on the y-axis
        {
            setLocation(getX(), getY()+4);
        }
}
public void checkFire()
{
   if((Greenfoot.getKey() == "space") || Greenfoot.isKeyDown("f")) {//If the user presses 'space' or 'w', shoot a laser
       
       getWorld().addObject(new Laser(this), getX(), getY());
       
   }
}
    public void endLevel1() {
        if (KillCounter == 4) {
            //Put a congratulations, you beat level one message here
            World ws2 = new Stage2(this, getX(), getY());
            //ws2.addObject();
            Greenfoot.setWorld(ws2);  
            KillCounter++;
        }
}
    public void endLevel2() {
        if (KillCounter == 7) {
            //Put a congratulations, you beat level one message here
            World ws3 = new Stage3(this, getX(), getY());
            //ws2.addObject();
            Greenfoot.setWorld(ws3);  
            KillCounter++;
        }
        if (KillCounter == 10) {
            //Put a congratulations, you beat level one message here
            World ws3 = new Stage3Continued(this, getX(), getY());
            //ws2.addObject();
            Greenfoot.setWorld(ws3);  
            KillCounter++;
        }
}
}