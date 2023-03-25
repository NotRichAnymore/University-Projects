
package randomOrgClient;
import java.io.*;
import java.util.*;
/*Manages the main flow/functionality of the program via method class from other files*/
public class main{
    public static void main(String[] args) throws IOException , Exception{
       /*boolean that continously runs the program unless specific command invoked*/      
       boolean running = true;
       
       
       
       randomOrgClient random = new randomOrgClient();
        /*
        String UUID = random.getRandomUUIDS();
        System.out.println("random UUID");
        System.out.println(UUID);
        */
       String UUIDS = random.getRandomUUIDS();
       System.out.println(UUIDS);
    }
}
