package Classes;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;



public class User {
    private String userID;
    private String username;
    private String password;
    private String name;
    private String city;
    private String country;
    private String ageGroup;
    private String interests;
    private String travelReasons;
    
    public String getUserID(){return userID;}
    public void setUserID(String value){this.userID = value;}
    
    public String getUsername(){return username;}
    public void setUsername(String value){this.username = value;}
    
    public String getPassword(){return password;}
    public void setPassword(String value){this.password = value;}
    
    public String getName(){return name;}
    public void setName(String value){this.name = value;}
    
    public String getCity(){return city;}
    public void setCity(String value){this.city = value;}
    
    public String getCountry(){return country;}
    public void setCountry(String value){this.country = value;}
    
    public String getAgeGroup(){return ageGroup;}
    public void setAgeGroup(String value){this.ageGroup = value;}
    
    public String getInterests(){return interests;}
    public void setInterests(String value){this.interests = value;}
    
    public String getTravelReasons(){return travelReasons;}
    public void setTravelReasons(String value){this.travelReasons = value;}
    
     public User createUserObject(String userID, String username, String password, String name, String city, String country, String ageGroup, String interests, String travelReasons) throws IOException{
        User user = new User();
        user.setUsername(username);
        user.setPassword(password);
        user.setName(name);
        user.setCity(city);
        user.setCountry(country);
        user.setAgeGroup(ageGroup);
        user.setInterests(interests);
        user.setTravelReasons(travelReasons);
         
        return user;
    }
}


