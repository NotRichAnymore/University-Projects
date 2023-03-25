/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Json_Functionality;


import com.google.gson.Gson;
import java.io.IOException;


public class TripQueryJson {
    /*public class QueryJson{
        
        protected HashMap<String, String> publisher = new HashMap<>();
        
        public QueryJson(String locationName, String locationRegion, String locationCountry){
            publisher.put("City",locationName);
            publisher.put("Region", locationRegion);
            publisher.put("Country", locationCountry);
        }
        
        private String cityName;
        private String cityRegion;
        private String cityCountry;
        
        public String getCityName(){return cityName;}
        public void setCityName(String value){this.cityName = value;}
        
        public String getCityRegion(){return cityRegion;}
        public void setCityRegion(String value){this.cityRegion = value;}
        
        public String getCityCountry(){return cityCountry;}
        public void setCityCountry(String value){this.cityCountry = value;}
     }
    
    private  QueryJson createQueryJsonObject() throws IOException{
        QueryJson QJ = new QueryJson();
        
        String cityName = getCitySpecifiedName();
        QJ.setCityName(cityName);
        
        String cityRegion = getCitySpecifiedRegion();
        QJ.setCityRegion(cityRegion);
        
        String cityCountry = getCitySpecifiedCountry();
        QJ.setCityCountry(cityCountry);
        
        return QJ;
    }
    public String setQueryForNewTripJson() throws IOException{
        Gson gson = new Gson();
        QueryJson QJ = createQueryJsonObject();
        
        FileWriter writer = new FileWriter("\QueryJson.json")
        gson.toJson(QJ, writer);
        
        return gson.toJson(QJ);
    }*/
    
}
