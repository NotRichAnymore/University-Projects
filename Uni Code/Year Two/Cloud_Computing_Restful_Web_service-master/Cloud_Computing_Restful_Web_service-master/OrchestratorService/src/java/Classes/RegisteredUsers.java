/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Classes;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class RegisteredUsers {
    private List<String> userIDs;
    private List<String> usernames;
    
    public List<String> getUserIDs(){return userIDs;}
    public void setUserIDs(List<String> value){this.userIDs = value;}
    
    public List<String> getUsernames(){return usernames;}
    public void setUsernames(List<String> value){this.usernames = value;}
    
    public RegisteredUsers createRegisteredUsersObject(String userID, String username)throws IOException{
        RegisteredUsers registeredUser = new RegisteredUsers();
        String[] splitUserIDs = userID.split("");
        List<String> listOfUserIDs = new ArrayList<String>(Arrays.asList(splitUserIDs));
        registeredUser.setUserIDs(listOfUserIDs);
        
        String[] splitStringUsername = username.split("");
        List<String> listOfUsernames = new ArrayList<String>(Arrays.asList(splitStringUsername));
        registeredUser.setUsernames(listOfUsernames);
        
        return registeredUser;
    }
    
}
