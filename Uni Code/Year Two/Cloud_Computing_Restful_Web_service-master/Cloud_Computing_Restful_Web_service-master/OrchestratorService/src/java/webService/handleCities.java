
package webService;

import Json_Cities.Cities;
import Json_Cities.Datum;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URI;
import java.net.URL;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.logging.Level;
import java.util.logging.Logger;


public class handleCities {
    
    public static List<String> getListOfCitiesFromFile() throws FileNotFoundException, IOException{
        
        List<String> listOfCities = new ArrayList<>();
        BufferedReader reader = null;
        URL file = new URL("http://localhost:8080/OrchestratorService/webresources/webservice/cities/listofcities?filename=listofcities.txt");
        //File file = new File(fileName);
        try{
            reader = new BufferedReader(new InputStreamReader(file.openStream()));
        
            String line;
            while((line = reader.readLine()) != null){
                System.out.println(line);
                listOfCities.add(line);    
            }
        }catch (IOException ioe){
            ioe.printStackTrace();
        }finally{
            try{
                if(reader != null)
                    reader.close();
            }catch (IOException ioe){
                ioe.printStackTrace();
            }
        }
        return listOfCities;
    }
    
    public static List getListOfWikiIDsFromFile() throws FileNotFoundException, IOException{
        List<String> listOfWikiIDs = new ArrayList<>();
        BufferedReader reader = null;
        URL file = new URL("http://localhost:8080/OrchestratorService/webresources/webservice/cities/WikiIDs?filename=listofwikiids.txt");
        //File file = new File(fileName);
        try{
            reader = new BufferedReader(new InputStreamReader(file.openStream()));
        
            String line;
            while((line = reader.readLine()) != null){
                System.out.println(line);
                listOfWikiIDs.add(line);    
            }
        }catch (IOException ioe){
            ioe.printStackTrace();
        }finally{
            try{
                if(reader != null)
                    reader.close();
            }catch (IOException ioe){
                ioe.printStackTrace();
            }
        }
        return listOfWikiIDs;
    }
    
    
    public static boolean checkCityIsValid(String userInput) throws IOException{
        boolean valid = false;
        List<String> listOfCities = getListOfCitiesFromFile();
        
        for(String city: listOfCities){
            if(city.contains(userInput)){
                valid = true;
            }
        }
        return valid;
    }
    
    public static String getWikiIDFromCity(String userDefinedCity, String userDefinedCountry) throws FileNotFoundException, IOException{
        String wikiID = "";
        List<String> listOfWikiIDs = getListOfWikiIDsFromFile();
       
        Map<String, String> wikiIDs_Cities = new LinkedHashMap<>();
        String country = "#" + userDefinedCountry;
        for(String line:listOfWikiIDs){
            while(line != null){
                String city = "";
                String qNum = "";
                
                int countryIndex = line.indexOf(country);
                int startIndex = countryIndex + 1;
                int endIndex = startIndex + 9;
                List<String> indexList = listOfWikiIDs.subList(startIndex, endIndex);
                
                for(String str: indexList){
                    if(str.contains(userDefinedCity)){
                        int colonIndex = str.indexOf(":");
                        qNum = str.substring(colonIndex);
                    }
                }
                wikiID = qNum;
            }
        }
        return wikiID;
     }
    
    public static String getCityJson(String wikiID) throws IOException{
        String jsonString = "";
        
        System.out.println("City ID: "+ wikiID);
        try {
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create("https://wft-geo-db.p.rapidapi.com/v1/geo/cities/" + wikiID))
                    .header("X-RapidAPI-Key", "6faf077cdemshe52f17a9ecd51fdp16b35cjsn492cb29b5e1a")
                    .header("X-RapidAPI-Host", "wft-geo-db.p.rapidapi.com")
                    .method("GET", HttpRequest.BodyPublishers.noBody())
                    .build();
            HttpResponse<String> response;

            response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
            jsonString = response.body();


            } catch (InterruptedException ex) {
                Logger.getLogger(Cities.class.getName()).log(Level.SEVERE, null, ex);
        
        
        }
        System.out.println("Expected Json: " + jsonString);
        return jsonString;
    }
        
    public static List parseGeoDBJson(String jsonString) throws IOException{
        
        GsonBuilder builder = new GsonBuilder();
        Gson gson = builder.create();
        
        Cities city = gson.fromJson(jsonString, Cities.class);
        Datum[] datum = city.getData();
        System.out.println(datum);
        List<String> cityDetails = new ArrayList<>();
        
        // 2,3,5,7,8,9
        for(int i=0; i < datum.length; i++){
            
                String name = datum[i].getName();
                cityDetails.add(name);
 
                String country = datum[i].getCountry();
                cityDetails.add(country);
                
                String region = datum[i].getRegion();
                cityDetails.add(region);
                
                double latitude = datum[i].getLatitude();
                cityDetails.add(Double.toString(latitude));
                
                double longtitude = datum[i].getLongitude();
                cityDetails.add(Double.toString(longtitude));
                
                long population = datum[i].getPopulation();
                cityDetails.add(Long.toString(population));
        }
        
        System.out.println(cityDetails);
        return cityDetails;
    }
    
    public static String getCitySpecifiedName(List jsonAsArray) throws IOException{
        List<String> cityDetails = jsonAsArray;
        String name = "";
        for(int i=0; i < cityDetails.size(); i++){
            if(i == 0){
                name = cityDetails.get(i);
            }
        }
        return name;
    }
    
    public static String getCitySpecifiedCountry(List jsonAsArray) throws IOException{
        List<String> cityDetails = jsonAsArray;
        String country = "";
        for(int i=0; i < cityDetails.size(); i++){
            if(i == 1){
                country = cityDetails.get(i);
            }
        }
        return country;
    }
    
    public static String getCitySpecifiedRegion(List jsonAsArray) throws IOException{
        List<String> cityDetails = jsonAsArray;
        String region = "";
        for(int i=0; i < cityDetails.size(); i++){
            if(i == 2){
                region = cityDetails.get(i);
            }
        }
        return region;
    }
    
    public static String getCitySpecifiedLatitude(List jsonAsArray) throws IOException{
        List<String> cityDetails = jsonAsArray;
        String latitude = "";
        for(int i=0; i < cityDetails.size(); i++){
            if(i == 3){
                latitude = cityDetails.get(i);
            }
        }
        return latitude;
    }
        
    public static String getCitySpecifedLongitude(List jsonAsArray) throws IOException{
        List<String> cityDetails = jsonAsArray;
        String longitude = "";
        for(int i=0; i < cityDetails.size(); i++){
            if(i == 4){
                longitude = cityDetails.get(i);
            }
        }
        return longitude;
    }
    
    public static String getCitySpecifiedPopulation(List jsonAsArray) throws IOException{
        List<String> cityDetails = jsonAsArray;
        String population = "";
        for(int i=0; i < cityDetails.size(); i++){
            if(i == 5){
                population = cityDetails.get(i);
            }
        }
        return population;
    }
}
