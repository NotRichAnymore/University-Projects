/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Json_Weather;


public class Wind10M {
    private Direction direction;
    private long speed;

    public Direction getDirection() { return direction; }
    public void setDirection(Direction value) { this.direction = value; }

    public long getSpeed() { return speed; }
    public void setSpeed(long value) { this.speed = value; }
    
    @Override
    public String toString(){
    return getDirection() + "," + getSpeed();
    }
}