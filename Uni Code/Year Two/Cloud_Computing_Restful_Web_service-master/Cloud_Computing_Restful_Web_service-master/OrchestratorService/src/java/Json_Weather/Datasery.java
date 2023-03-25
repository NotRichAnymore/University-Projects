/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Json_Weather;


public class Datasery {
    private long timepoint;
    private long cloudcover;
    private long seeing;
    private long transparency;
    private long liftedIndex;
    private long rh2M;
    private Wind10M wind10M;
    private long temp2M;
    private PrecType precType;

    public long getTimepoint() { return timepoint; }
    public void setTimepoint(long value) { this.timepoint = value; }

    public long getCloudcover() { return cloudcover; }
    public void setCloudcover(long value) { this.cloudcover = value; }

    public long getSeeing() { return seeing; }
    public void setSeeing(long value) { this.seeing = value; }

    public long getTransparency() { return transparency; }
    public void setTransparency(long value) { this.transparency = value; }

    public long getLiftedIndex() { return liftedIndex; }
    public void setLiftedIndex(long value) { this.liftedIndex = value; }

    public long getRh2M() { return rh2M; }
    public void setRh2M(long value) { this.rh2M = value; }

    public Wind10M getWind10M() { return wind10M; }
    public void setWind10M(Wind10M value) { this.wind10M = value; }

    public long getTemp2M() { return temp2M; }
    public void setTemp2M(long value) { this.temp2M = value; }

    public PrecType getPrecType() { return precType; }
    public void setPrecType(PrecType value) { this.precType = value; }
}

