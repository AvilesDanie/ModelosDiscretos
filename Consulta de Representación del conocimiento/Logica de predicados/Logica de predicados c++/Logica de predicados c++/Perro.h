#pragma once
#include <iostream>
#include <string>
class Perro {
private:
    std::string nombre;
public:
    Perro(std::string);
    bool ladrar() const;
};

