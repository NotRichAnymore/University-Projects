/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Json_Weather;


import java.io.IOException;

public enum Direction {
    E, N, NE, SE;

    public String toValue() {
        switch (this) {
            case E: return "E";
            case N: return "N";
            case NE: return "NE";
            case SE: return "SE";
        }
        return null;
    }

    public static Direction forValue(String value) throws IOException {
        if (value.equals("E")) return E;
        if (value.equals("N")) return N;
        if (value.equals("NE")) return NE;
        if (value.equals("SE")) return SE;
        throw new IOException("Cannot deserialize Direction");
    }
}
