
package TravelLength;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;



public class handleDatesTravelling {
    public static LocalDate getUserSpecifiedStartDate() throws IOException{
        System.out.println("Enter the start date for your trip(dd-mm-yyyy): ");
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String userInput = input.readLine();
        DateTimeFormatter format = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        LocalDate startDate = LocalDate.parse(userInput, format);
        return startDate;
    }
    
    public static LocalDate getUserSpecifiedEndDate() throws IOException{
        System.out.println("Enter the end date for your trip(dd-mm-yyyy): ");
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String userInput = input.readLine();
        DateTimeFormatter format = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        LocalDate endDate = LocalDate.parse(userInput, format);
        return endDate;
    }
    
    public static List<LocalDate> setDatesTravelling() throws IOException{
        LocalDate startDate = getUserSpecifiedStartDate();
        LocalDate endDate = getUserSpecifiedEndDate();
        
        List<LocalDate> datesTravelling = new ArrayList<>();
        while(!startDate.isAfter(endDate)){
            datesTravelling.add(startDate);
            startDate = startDate.plusDays(1);
        }
        						
        return datesTravelling;
    }
}
