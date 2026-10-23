"""=================================================================================================
Institute....: Universidad Técnica Nacional
Campus.......: Pacífico
Career.......: Tecnologías de Información
Course.......: ITI-321 - Programación III
Period.......: 3-2026
Documents....: Exam_01 - 01_Stack
Goals........: Using stack class
Professor....: Jorge Ruiz (york)
Student......:
================================================================================================="""
from cls_Stack import cls_Stack


print()
print("Stack implementation")
print("=================================")

# Create stack instance
pilita = cls_Stack()

# Load data chunk into stack while this not full
for letra in "Cuquita":
    if not pilita.isfull():
        pilita.push(letra)
    else:
        break

while not pilita.isempty():
    print(pilita.pop())

import Problema1
import Problema2


def mostrar_menu() -> None:
    print()
    print("================================")
    print("1.Evaluación de expresiones matematicas")
    print("2.Buscando a la reina de corazones(Juego)")
    print("0.Salir")


def main() -> None:
    acciones = {"1": Problema1.main, "2": Problema2.main}

    while True:
        mostrar_menu()
        opcion = input("\nElija una opción: ").strip()

        if opcion == "0":
            print("\nFin del programa.")
            break
        elif opcion in acciones:
            acciones[opcion]()
        else:
            print("\nOpción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()



