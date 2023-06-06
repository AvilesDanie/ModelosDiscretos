#include "Perro.h"

Perro::Perro(std::string nombre) {
    this->nombre = nombre;
}

bool Perro::ladrar() const {
    std::cout << nombre << " esta ladrando." << std::endl;
    return true;
}