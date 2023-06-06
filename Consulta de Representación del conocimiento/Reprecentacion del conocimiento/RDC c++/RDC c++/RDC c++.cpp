#include <iostream>
#include <string>
#include "Animal.h"

/*En este ejemplo de la Representacion del conocimiento
 se usa una clase Animal para retener y posteriormente
 mostrar(usar) la informacion sobre un animal*/
int main() {
    Animal perro("Perro", 3, "Max");
    perro.mostrarInformacion();

    return 0;
}