
package webService;

import Classes.ListOfCitiesJson;
import Classes.ListOfWikiIDsJson;
import Classes.ProposeJson;
import Classes.RegisteredUsers;
import Classes.User;
import Classes.Location;
import com.google.gson.Gson;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URI;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.UriInfo;
import javax.ws.rs.Consumes;
import javax.ws.rs.Produces;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.PUT;
import javax.ws.rs.PathParam;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

/**
 * REST Web Service
 *
 * 
 */
@Path("webservice")
public class WebserviceResource {

    @Context
    private UriInfo context;

    /**
     * Creates a new instance of WebserviceResource
     */
    public WebserviceResource() {
    }

    
    @POST
    @Path("/users/accountdetails")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response storeAccountDetails(InputStream request) throws IOException{
        
        StringBuilder sb = new StringBuilder();
        try{
            BufferedReader input = new BufferedReader(new InputStreamReader(request));
            String line = "";
            while((line = input.readLine())!= null){
                sb.append(line);
            }
        }catch (IOException ioe){
            ioe.printStackTrace();
        }
        String jsonString = sb.toString();
        
        Gson gson = new Gson();
        User userDetails = gson.fromJson(jsonString, User.class);
        
        ///{userID}
        //@PathParam("userID") String userID,
        
        String userID = userDetails.getUserID();
        String username = userDetails.getUsername();
        String password = userDetails.getPassword();
        String name = userDetails.getName();
        String city = userDetails.getCity();
        String country = userDetails.getCountry();
        String ageGroup = userDetails.getAgeGroup();
        String interests = userDetails.getInterests();
        String travelReasons = userDetails.getTravelReasons();
        
        System.out.println("Account Details for :" + name);
        System.out.println("User ID: " + userID);
        System.out.println("Username:" + username);
        System.out.println("Password" + password);
        System.out.println("City: " + city);
        System.out.println("Country: " + country);
        System.out.println("Age Group: " + ageGroup);
        System.out.println("Interests: " + interests);
        System.out.println("Travel Reasons: " + travelReasons);
        
        String fileName = username+"_AccountDetails.json";
        try{
            User accountDetails = userDetails.createUserObject(userID, username, password, name, city, country, ageGroup, interests, travelReasons);
            
            
            FileWriter writer = new FileWriter(fileName);
            gson.toJson(accountDetails, writer);
            writer.close();
        } catch (FileNotFoundException fnf){
            fnf.printStackTrace();
        } catch (IOException e){
            e.printStackTrace();
        }
        String result = "Account Details uploaded at: " + context.getRequestUri() + "/" + fileName;
                        //+ userID + username + password + name + city + country + ageGroup + interests + travelReasons;
        
        return Response.status(200).entity(result).build();
    }
    
    
    @GET
    @Path("/users/accountdetails")
    @Produces(MediaType.APPLICATION_JSON)
    public String getUsersAccountDetails(@QueryParam("username") String username) throws IOException{
        FileReader reader = new FileReader(username+"_AccountDetails.json");
        Gson gson = new Gson();
        User user = gson.fromJson(reader, User.class);
        String userID = user.getUserID();
        String password = user.getPassword();
        String name = user.getName();
        String city = user.getCity();
        String country = user.getCountry();
        String ageGroup = user.getAgeGroup();
        String interests = user.getInterests();
        String travelReasons = user.getTravelReasons();
        User userDetails = user.createUserObject(userID, username, password, name, city, country, ageGroup, interests, travelReasons);
        String response = gson.toJson(userDetails);
        return response;
    }
    
    
    
    
    @POST
    @Path("/cities/listofcities")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response storeListOfCitiesFile(InputStream request) throws IOException{
        StringBuilder sb = new StringBuilder();
        try{
            BufferedReader input = new BufferedReader(new InputStreamReader(request));
            String line = "";
            while((line = input.readLine())!= null){
                sb.append(line);
            }
        }catch (IOException ioe){
            ioe.printStackTrace();
        }
        String jsonString = sb.toString();
        
        Gson gson = new Gson();
        ListOfCitiesJson fileContents = gson.fromJson(jsonString, ListOfCitiesJson.class);
        List<String> listOfCities = fileContents.getListOfCities();
        
        String fileName = "listOfCities.txt";
        try{
            ListOfCitiesJson LOCJ = fileContents.createListOfCitiesJson(fileName, listOfCities);           
            FileWriter writer = new FileWriter(fileName);
            gson.toJson(LOCJ, writer);
            writer.close();
        } catch (FileNotFoundException fnf){
            fnf.printStackTrace();
        } catch (IOException e){
            e.printStackTrace();
        }
        String result = "List of Cities uploaded: " + context.getRequestUri() + "/" + fileName;
                //+ city + area + country;       
        return Response.status(200).entity(result).build();
    }
    
    @GET
    @Path("/cities/listofcities")
    @Produces(MediaType.APPLICATION_JSON)
    public String getListOfCities(@QueryParam("filename") String fileName) throws IOException{
        FileReader reader = new FileReader(fileName);
        Gson gson = new Gson();
        ListOfCitiesJson obj = gson.fromJson(reader, ListOfCitiesJson.class);
        List<String> listOfCities = obj.getListOfCities();
        String response = gson.toJson(listOfCities);
        return response;
    }
    
    @GET
    @Path("/cities/WikiIDs")
    @Produces(MediaType.APPLICATION_JSON)
    public String getListOfWikiIDs(@QueryParam("filename") String fileName) throws IOException{
        FileReader reader = new FileReader(fileName);
        Gson gson = new Gson();
        ListOfWikiIDsJson obj = gson.fromJson(reader, ListOfWikiIDsJson.class);
        List<String> listOfWikiIDs = obj.getListOfWikiIDs();
        String response = gson.toJson(listOfWikiIDs);
        return response;
    }
    
    @POST
    @Path("/cities/WikiIDs")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response storeListOfWikiIDsFile(InputStream request) throws IOException{
        StringBuilder sb = new StringBuilder();
        try{
            BufferedReader input = new BufferedReader(new InputStreamReader(request));
            String line = "";
            while((line = input.readLine())!= null){
                sb.append(line);
            }
        }catch (IOException ioe){
            ioe.printStackTrace();
        }
        String jsonString = sb.toString();
        
        Gson gson = new Gson();
        ListOfWikiIDsJson fileContents = gson.fromJson(jsonString, ListOfWikiIDsJson.class);
        List<String> listOfWikiIDs = fileContents.getListOfWikiIDs();
        
        String fileName = "listofwikiids.txt";
        try{
            ListOfWikiIDsJson LOCJ = fileContents.createListOfWikiIDsJson(fileName, listOfWikiIDs);           
            FileWriter writer = new FileWriter(fileName);
            gson.toJson(LOCJ, writer);
            writer.close();
        } catch (FileNotFoundException fnf){
            fnf.printStackTrace();
        } catch (IOException e){
            e.printStackTrace();
        }
        String result = "List of Cities uploaded: " + context.getRequestUri() + "/" + fileName;
                //+ city + area + country;       
        return Response.status(200).entity(result).build();
    }
    
    @POST
    @Path("/weatherforecast/location")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response storeCurrentTripLocation(InputStream request) throws IOException{
        StringBuilder sb = new StringBuilder();
        try{
            BufferedReader input = new BufferedReader(new InputStreamReader(request));
            String line = "";
            while((line = input.readLine())!= null){
                sb.append(line);
            }
        }catch (IOException ioe){
            ioe.printStackTrace();
        }
        String jsonString = sb.toString();
        
        Gson gson = new Gson();
        Location tripLocation  = gson.fromJson(jsonString, Location.class);
        
        String username = tripLocation.getUsername();
        String city = tripLocation.getCity();
        String country = tripLocation.getCountry();
        
        System.out.println("Trip Location" + username);
        System.out.println("City: " + city);
        System.out.println("Country: " + country);
        
        String fileName = username+"_NewTripLocation.json";
        try{
            Location tripPlace = tripLocation.createNewLocationObject(username, city,  country);
            
            FileWriter writer = new FileWriter(fileName);
            gson.toJson(tripPlace, writer);
            writer.close();
        } catch (FileNotFoundException fnf){
            fnf.printStackTrace();
        } catch (IOException e){
            e.printStackTrace();
        }
        String result = "New trip location details uploaded: " + context.getRequestUri() + "/" + fileName;
                //+ city + area + country;       
        return Response.status(200).entity(result).build();
    }
    
    
    @GET
    @Path("/weatherforecast/location")
    @Produces(MediaType.APPLICATION_JSON)
    public String createWeatherForecast(@QueryParam("username") String username)throws IOException{
        FileReader reader = new FileReader(username+"_NewTripLocation.json");
        Gson gson = new Gson();
        handleCities hC = new handleCities();
        handleWeatherForecast hWF = new handleWeatherForecast();
        Location place = gson.fromJson(reader,Location.class);
        String city = place.getCity();
        String country = place.getCountry();
        String weatherForecast = "";
        
        String wikiID = "";
        boolean validCity = hC.checkCityIsValid(city);
        String condition = Boolean.toString(validCity);
        
        return condition;     
    }
    
    @GET
    @Path("/randomOrg/uuid")
    @Produces(MediaType.APPLICATION_JSON)
    public String createUserID() throws IOException{
        handleRandomUUIDs hRU = new handleRandomUUIDs();
        String UUID = "";
        
        try{
       
            String randomOrgResponse = hRU.getRandomUUIDS();
            UUID = hRU.parseRandomOrgJson(randomOrgResponse);
        
        
        }catch(IOException ioe){
            ioe.printStackTrace();
        }
        return UUID;
    }    
    
    @POST
    @Path("/trips/newtrip")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response storeNewTripRequest(InputStream request){
         StringBuilder sb = new StringBuilder();
        try{
            BufferedReader input = new BufferedReader(new InputStreamReader(request));
            String line = "";
            while((line = input.readLine())!= null){
                sb.append(line);
            }
        }catch (IOException ioe){
            ioe.printStackTrace();
        }
        String jsonString = sb.toString();
        
        Gson gson = new Gson();
        ProposeJson newTripDetails = gson.fromJson(jsonString, ProposeJson.class);
        
        String userID = newTripDetails.getUserID();
        String tripID = newTripDetails.getTripID();
        String city = newTripDetails.getCity();
        String country = newTripDetails.getCountry();
        String tripDates = newTripDetails.getTripDates();
        String weather = newTripDetails.getWeather();
        
        System.out.println("New Trip for: " + userID);
        System.out.println("User ID: " + userID);
        System.out.println("Location: " + city +", " + country);
        System.out.println("Trip Dates: " + tripDates);
        System.out.println("Weather: " + weather);
        try{
            ProposeJson newTrip = newTripDetails.createProposeJsonObject(userID, tripID, city, country, tripDates, weather);
            
            FileWriter writer = new FileWriter(tripID+"_NewTrip.json");
            gson.toJson(newTrip, writer);
            writer.close();
        } catch (FileNotFoundException fnf){
            fnf.printStackTrace();
        } catch (IOException e){
            e.printStackTrace();
        }
        String result = "New Trip Details: " + userID + tripID + city + country + weather;
        
        return Response.status(200).entity(result).build();
        
    }
    
    
    
    
    
    
    
    
    
    //public static setExpressInterestInTripJson(){
        
    //}
    
    //public static setCheckInterestInTripJson(){
        
    //}
}
        
      
    
    
   

