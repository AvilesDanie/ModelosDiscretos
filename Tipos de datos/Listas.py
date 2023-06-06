lista = ["nombre", 4, True, [4, 5, "a"], 10.2]
print(type(lista))

lista1 = []
lista1.append("Colombia")
lista1.append("Peru")
lista1.append("Brazil")
print(lista1)

lista2 = lista1.copy()
print(lista2)

lista2.clear()
print(lista2)

lista2 = lista1.copy()
print(lista2.count("Brazil"))
lista2.append("Brazil")
print(lista2.count("Brazil"))


print(len(lista2))
print(lista2[1])
print(lista2[3])
print(lista2[0])
lista2[3] = "Mexico"
print(lista2)

#Eliminar elemento de una lista

lista2.pop()
print(lista2)

lista2.remove("Peru")
print(lista2)

lista2.append("Brazil")
lista2.append("Brazil")
lista2.append("Brazil")
lista2.append("Brazil")
lista2.remove("Brazil")

print(lista2)

lista2[2] = None
print(lista2)

lista3 = [10,9,8,7,6,5,4,3,2,1,0]
lista3.reverse()
print(lista3)

lista4 = ["u","e","a","i","o"]
lista4.sort()
print(lista4)




