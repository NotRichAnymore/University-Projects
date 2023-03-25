/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Json_Weather;


import java.io.IOException;

public enum PrecType {
    NONE;
    
    @Override
    public String toString(){
    return this.toValue();
    }
    
    public String toValue() {
        switch (this) {
            case NONE: return "none";
        }
        return null;
    }

    public static PrecType forValue(String value) throws IOException {
        if (value.equals("none")) return NONE;
        throw new IOException("Cannot deserialize PrecType");
    }
}
