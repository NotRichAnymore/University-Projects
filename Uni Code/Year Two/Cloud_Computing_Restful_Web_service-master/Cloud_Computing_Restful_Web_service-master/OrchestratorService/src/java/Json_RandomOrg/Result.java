/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Json_RandomOrg;


public class Result {
    private Random random;
    private long bitsUsed;
    private long bitsLeft;
    private long requestsLeft;
    private long advisoryDelay;

    public Random getRandom() { return random; }
    public void setRandom(Random value) { this.random = value; }

    public long getBitsUsed() { return bitsUsed; }
    public void setBitsUsed(long value) { this.bitsUsed = value; }

    public long getBitsLeft() { return bitsLeft; }
    public void setBitsLeft(long value) { this.bitsLeft = value; }

    public long getRequestsLeft() { return requestsLeft; }
    public void setRequestsLeft(long value) { this.requestsLeft = value; }

    public long getAdvisoryDelay() { return advisoryDelay; }
    public void setAdvisoryDelay(long value) { this.advisoryDelay = value; }
}
