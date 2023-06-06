package reprecentacion.del.conocimiento;

/**
 *
 * @author Daniel Aviles, DeltaTeam, DCCO-ESPE
 */
public class ReprecentacionDelConocimiento {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        /*En este ejemplo de la Representacion del conocimiento
        se usa una clase Animal para retener y posteriormente 
        mostrar(usar) la informacion sobre un animal*/
        Animal perro = new Animal("Perro", 3, "Max");
        perro.mostrarInformacion();
    }
    
}
