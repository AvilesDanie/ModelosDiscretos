#include <iostream>
#include <string>
#include <vector>
#include "Perro.h"

/*En este ejemplo de logica de predicados se
    tiene una clase perro con la funcion ladrar
    y con la funcion todosLosPerrosLadran se
    busca verificar la premisa*/

bool todosLosPerrosLadran(const std::vector<Perro>& perros) {
    for (const auto& perro : perros) {
        if (!perro.ladrar()) {
            return false;
        }
    }
    return true;
}

int main() {
    std::vector<Perro> listaPerros;
    listaPerros.push_back(Perro("Max"));
    listaPerros.push_back(Perro("Bella"));
    listaPerros.push_back(Perro("Charlie"));

    if (todosLosPerrosLadran(listaPerros)) {
        std::cout << "Todos los perros ladran." << std::endl;
    }
    else {
        std::cout << "No todos los perros ladran." << std::endl;
    }

    return 0;
}
