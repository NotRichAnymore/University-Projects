/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Classes;

import java.io.IOException;


public class Location {
    private String username;
    private String city;
    private String country;
    
    public String getUsername(){return username;}
    public void setUsername(String value){this.username = value;}
    
    public String getCity(){return city;}
    public void setCity(String value){this.city = value;}
    
    
    public String getCountry(){return country;}
    public void setCountry(String value){this.country = value;}
    
    public Location createNewLocationObject(String username, String city, String country) throws IOException{
        Location L = new Location();
        
        L.setUsername(username);
        L.setCity(city);
        L.setCountry(country);
        
        return L;
    }
}
