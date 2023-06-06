#pragma once
#include <iostream>
#include <string>
class Animal {
private:
    std::string especie;
    int edad;
    std::string nombre;
public:
    Animal(std::string especie, int edad, std::string nombre);
    void mostrarInformacion();
};
