
package webService;


import Json_Weather.Datasery;
import Json_Weather.PrecType;
import Json_Weather.Weather;
import Json_Weather.Wind10M;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;



public class handleWeatherForecast {
    
        
    
    
        public static String getWeather(String lon, String lat) throws IOException{
        Map<String, String> parameters = new HashMap<>();
        
        
        parameters.put("lon", lon);
        parameters.put("lat", lat);
        parameters.put("lang", "en");
        parameters.put("unit", "metric");
        parameters.put("output", "json");

        StringBuilder mapAsString = new StringBuilder("{");
        for (String key : parameters.keySet()) {
            mapAsString.append(key + "=" + parameters.get(key) + ", ");
        }
        mapAsString.delete(mapAsString.length()-2, mapAsString.length()).append("}");
        System.out.println( mapAsString.toString());
        String convertedParamsToString = mapAsString.toString();
       
        URL url = new URL("http://www.7timer.info/bin/astro.php?" + convertedParamsToString);
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestMethod("GET");
        con.connect();
        InputStream input = con.getInputStream();
        BufferedReader Reader = new BufferedReader(new InputStreamReader(input));
            
        String line = Reader.readLine();
        StringBuilder result = new StringBuilder();
        while(line != null){
            result.append(line);
        }
        String output = result.toString();
       
        
        return output;
    }
    
    public static List parseWeatherJson(String lon, String lat) throws IOException{
        GsonBuilder builder = new GsonBuilder();
        Gson gson = builder.create();
        String jsonString = getWeather(lon, lat);
        
        Weather weather = gson.fromJson(jsonString, Weather.class);
        Datasery[] forecast = weather.getDataseries();
        
        List<String> weatherForecast = new ArrayList<>();
        
        for(int i=0; i< forecast.length; i++){
            long time = forecast[i].getTimepoint();
            weatherForecast.add(Long.toString(time));
            
            long cloudAmount = forecast[i].getCloudcover();
            weatherForecast.add(Long.toString(cloudAmount));
            
            long airTransparency = forecast[i].getTransparency();
            weatherForecast.add(Long.toString(airTransparency));
            
            long humidity = forecast[i].getRh2M();
            weatherForecast.add(Long.toString(humidity));
            
            long temperature = forecast[i].getTemp2M();
            weatherForecast.add(Long.toString(temperature));
            
            PrecType rainAmount = forecast[i].getPrecType();
            weatherForecast.add(rainAmount.toString());
            
            Wind10M windAmount = forecast[i].getWind10M();
            weatherForecast.add(windAmount.toString());
            
        }
        return weatherForecast;
    }
    
    public static String getTime(List jsonAsArray) throws IOException{
        List<String> weatherForecast = jsonAsArray;
        String time = "";
        for(int i=0; i < weatherForecast.size(); i++){
            if(i == 0){
                time = weatherForecast.get(i);
            }
        }
        return time;    
    }
    
    public static String getCloudAmount(List jsonAsArray) throws IOException{
        List<String> weatherForecast = jsonAsArray;
        String cloudAmount = "";
        for(int i=0; i < weatherForecast.size(); i++){
            if(i == 1){
                cloudAmount = weatherForecast.get(i);
            }
        }
        return cloudAmount; 
    }
    public static String getAirTransparency(List jsonAsArray) throws IOException{
        List<String> weatherForecast = jsonAsArray;
        String airTransparency = "";
        for(int i=0; i < weatherForecast.size(); i++){
            if(i == 3){
                airTransparency = weatherForecast.get(i);
            }
        }
        return airTransparency; 
        
    }
    public static String getHumidity(List jsonAsArray)throws IOException{
        List<String> weatherForecast = jsonAsArray;
        String airTransparency = "";
        for(int i=0; i < weatherForecast.size(); i++){
            if(i == 3){
                airTransparency = weatherForecast.get(i);
            }
        }
        return airTransparency; 
        
    }
    public static String getTemperature(List jsonAsArray)throws IOException{
        List<String> weatherForecast = jsonAsArray;
        String temperature = "";
        for(int i=0; i < weatherForecast.size(); i++){
            if(i == 7){
                temperature = weatherForecast.get(i);
            }
        }
        return temperature;
    }
    public static String getRainAmount(List jsonAsArray)throws IOException{
        List<String> weatherForecast = jsonAsArray;
        String rainAmount = "";
        for(int i=0; i < weatherForecast.size(); i++){
            if(i == 8){
                rainAmount = weatherForecast.get(i);
            }
        }
        return rainAmount;
    
    }
    public static String getWindAmount(List jsonAsArray)throws IOException{
        List<String> weatherForecast = jsonAsArray;
        String windAmount = "";
        for(int i=0; i < weatherForecast.size(); i++){
            if(i == 6){
                windAmount = weatherForecast.get(i);
            }
        }
        return windAmount;
    }
    
    public static String setWeatherForecast(List jsonAsArray) throws IOException{
        String time = getTime(jsonAsArray);
        String cloudAmount = getCloudAmount(jsonAsArray);
        String airTransparency = getAirTransparency(jsonAsArray);
        String humidity = getHumidity(jsonAsArray);
        String temperature = getTemperature(jsonAsArray);
        String rainAmount = getRainAmount(jsonAsArray);
        String windAmount = getWindAmount(jsonAsArray);
        
        String weatherForecast = "At " + time + " ," +
                                 "it's " + temperature +"degrees celcius"+ " ," +
                                 "currently" + rainAmount + " ," +
                                 "the wind is" + windAmount + " ," +
                                 "the humidity is" + humidity + " ," +
                                 "the level of visibility is" + airTransparency + " ," +
                                 "the sky is currently" + cloudAmount;
        return weatherForecast;                
    }
}
