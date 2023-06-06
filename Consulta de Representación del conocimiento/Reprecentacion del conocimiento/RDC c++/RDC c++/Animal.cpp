#include "Animal.h"
Animal::Animal(std::string especie, int edad, std::string nombre) {
    this->especie = especie;
    this->edad = edad;
    this->nombre = nombre;
}

void Animal::mostrarInformacion() {
    std::cout << "Especie: " << especie << std::endl;
    std::cout << "Edad: " << edad << " años" << std::endl;
    std::cout << "Nombre: " << nombre << std::endl;
}