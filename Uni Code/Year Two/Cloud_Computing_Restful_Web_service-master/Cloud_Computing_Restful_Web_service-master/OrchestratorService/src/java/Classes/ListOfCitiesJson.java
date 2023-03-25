/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Classes;

import java.util.List;



public class ListOfCitiesJson {
    private String filename;
    private List<String> listOfCities;
    
    public String getFileName(){return filename;}
    public void setFileName(String value){this.filename = value;}
    
    public List<String> getListOfCities(){return listOfCities;}
    public void setListOfCities(List<String> value){this.listOfCities = value;}
    
    public ListOfCitiesJson createListOfCitiesJson(String fileName, List<String> listOfCities){
        ListOfCitiesJson CJ = new ListOfCitiesJson();
        CJ.setFileName(fileName);
        CJ.setListOfCities(listOfCities);
        return CJ;
    }
    
}
