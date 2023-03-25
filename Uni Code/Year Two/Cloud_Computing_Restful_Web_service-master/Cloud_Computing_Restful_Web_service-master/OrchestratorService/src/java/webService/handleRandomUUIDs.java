
package webService;

import Json_RandomOrg.Random;
import Json_RandomOrg.Result;
import Json_RandomOrg.UUID;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;


public class handleRandomUUIDs {
    public static String getRandomUUIDS() throws IOException{
         
        String request = "{\n" +
        "   \"jsonrpc\": \"2.0\",\n" +
        "   \"method\": \"generateUUIDs\",\n" +
        "   \"params\": {\n" +
        "       \"apiKey\": \"00000000-0000-0000-0000-000000000000\",\n" +
        "       \"n\": 10\n" +
        "   },\n" +
        "   \"id\": 15998\n" +
        "}";
                
                
                
        URL url = new URL("https://api.random.org/json-rpc/4/invoke");
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestProperty("Accept", "application/json");
        con.setRequestProperty("Content-Type", "application/json");

        
        con.setDoOutput(true);
        con.setRequestMethod("POST");
        
        OutputStream os = con.getOutputStream();
        OutputStreamWriter osw = new OutputStreamWriter(os, "UTF-8");    
        osw.write(request);
        osw.flush();
        osw.close();
        os.close();
        
        con.connect();
        
        BufferedReader response = new BufferedReader(new InputStreamReader(con.getInputStream()));
        String line = response.readLine();
       
        return line;
    }
    
    
    
    
    
    public static String parseRandomOrgJson(String UUIDS) throws IOException{
        GsonBuilder builder = new GsonBuilder();
        Gson gson = builder.create();
        String jsonString = UUIDS;
        UUID uuid = gson.fromJson(jsonString, UUID.class);
        
        Result result = uuid.getResult();
        Random random = result.getRandom();
        java.util.UUID[] randomNums = random.getData();
        
        String elements = "";
        for(int i = 0; i < randomNums.length; i++){
            elements = randomNums[i].toString();
        }
        
        return elements;
    }
    
    
    
        
    
}   

