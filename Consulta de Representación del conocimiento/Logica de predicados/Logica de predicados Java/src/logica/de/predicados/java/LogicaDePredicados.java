package logica.de.predicados.java;

import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author Daniel Aviles, DeltaTeam, DCCO-ESPE
 */
public class LogicaDePredicados {
    /*En este ejemplo de logica de predicados se
    tiene una clase perro con la funcion ladrar
    y con la funcion todosLosPerrosLadran se 
    busca verificar la premisa*/
    public static boolean todosLosPerrosLadran(List<Perro> perros) {
        for (Perro perro : perros) {
            if (!perro.ladrar()) {
                return false;
            }
        }
        return true;
    }
    
    public static void main(String[] args) {
        List<Perro> listaPerros = new ArrayList<>();
        listaPerros.add(new Perro("Max"));
        listaPerros.add(new Perro("Bella"));
        listaPerros.add(new Perro("Charlie"));
        
        if (todosLosPerrosLadran(listaPerros)) {
            System.out.println("Todos los perros ladran.");
        } else {
            System.out.println("No todos los perros ladran.");
        }
    }
    
}
