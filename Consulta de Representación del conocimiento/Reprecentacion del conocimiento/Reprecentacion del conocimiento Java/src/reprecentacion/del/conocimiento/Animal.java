package reprecentacion.del.conocimiento;

/**
 *
 * @author Daniel Aviles, DeltaTeam, DCCO-ESPE
 */
public class Animal {
    private String especie;
    private int edad;
    private String nombre;
    
    public Animal(String especie, int edad, String nombre) {
        this.especie = especie;
        this.edad = edad;
        this.nombre = nombre;
    }
    
    public void mostrarInformacion() {
        System.out.println("Especie: " + especie);
        System.out.println("Edad: " + edad + " años");
        System.out.println("Nombre: " + nombre);
    }
}
