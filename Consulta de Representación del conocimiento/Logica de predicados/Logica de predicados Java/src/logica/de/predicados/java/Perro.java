/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package logica.de.predicados.java;

/**
 *
 * @author Daniel Aviles, DeltaTeam, DCCO-ESPE
 */
import java.util.ArrayList;
import java.util.List;

class Perro {
    private String nombre;
    
    public Perro(String nombre) {
        this.nombre = nombre;
    }
    
    public boolean ladrar() {
        System.out.println(nombre + " está ladrando.");
        return true;
    }
}



