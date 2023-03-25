
package randomOrgClient;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.net.HttpURLConnection;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;

public class randomOrgClient {
  
    public static String getRandomUUIDS() throws IOException{
        /*
        System.out.println("Enter how many UUIDS to return in mutiples of 10 (e.g 1 = 10, 2 = 20): ");
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int userInput = Integer.parseInt(input.readLine());
        
        "+userInput+"
          */  
            
            
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
   
    
 
   
     
    
    
    
}
    