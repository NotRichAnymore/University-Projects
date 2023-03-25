/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Json_Cities;


public class Datum {

    private long id;
    private String wikiDataID;
    private String name;
    private String country;
    private String countryCode;
    private String region;
    private String regionCode;
    private double latitude;
    private double longitude;
    private long population;

    public long getID() { return id; }
    public void setID(long value) { this.id = value; }

    public String getWikiDataID() { return wikiDataID; }
    public void setWikiDataID(String value) { this.wikiDataID = value; }

    public String getName() { return name; }
    public void setName(String value) { this.name = value; }

    public String getCountry() { return country; }
    public void setCountry(String value) { this.country = value; }

    public String getCountryCode() { return countryCode; }
    public void setCountryCode(String value) { this.countryCode = value; }

    public String getRegion() { return region; }
    public void setRegion(String value) { this.region = value; }

    public String getRegionCode() { return regionCode; }
    public void setRegionCode(String value) { this.regionCode = value; }

    public double getLatitude() { return latitude; }
    public void setLatitude(double value) { this.latitude = value; }

    public double getLongitude() { return longitude; }
    public void setLongitude(double value) { this.longitude = value; }

    public long getPopulation() { return population; }
    public void setPopulation(long value) { this.population = value; }
}

