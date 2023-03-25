/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Classes;

import java.util.List;


public class ListOfWikiIDsJson {
    private String filename;
    private List<String> listofWikiIDs;
    
    public String getFileName(){return filename;}
    public void setFileName(String value){this.filename = value;}
    
    public List<String> getListOfWikiIDs(){return listofWikiIDs;}
    public void setListOfWikiIDs(List<String> value){this.listofWikiIDs = value;}
    
    public ListOfWikiIDsJson createListOfWikiIDsJson(String fileName, List<String> listofWikiIDs){
        ListOfWikiIDsJson WIJ = new ListOfWikiIDsJson();
        WIJ.setFileName(fileName);
        WIJ.setListOfWikiIDs(listofWikiIDs);
        return WIJ;
    }
}
