/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Classes;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import java.io.IOException;


public class ProposeJson{
        private String userID;
        private String tripID;
        private String city;
        private String country;
        private String tripDates;
        private String weather;/*Set weather identifier instead of string*/ 
        
        public String getUserID(){return userID;}
        public void setUserID(String value){this.userID = value;}
        
        public String getTripID(){return tripID;}
        public void setTripID(String value){this.tripID = value;}
        
        public String getCity(){return city;}
        public void setCity(String value){this.city = value;}
        
         public String getCountry(){return country;}
        public void setCountry(String value){this.country = value;}
        
        public String getTripDates(){return tripDates;}
        public void setTripDates(String value){this.tripDates = value;}
        
        public String getWeather(){return weather;}
        public void setWeather(String value){this.weather = value;}
        
    
    public ProposeJson createProposeJsonObject(String userID, String tripID, String city, String country, String tripDates, String weather) throws IOException{
            ProposeJson PJ = new ProposeJson();
            
            PJ.setUserID(userID);
            PJ.setTripID(tripID);
            PJ.setCity(city);
            PJ.setCountry(country);
            PJ.setTripDates(tripDates);
            PJ.setWeather(weather);

            return PJ;
        }
}

