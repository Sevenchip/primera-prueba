"""=================================================================================================
Institute....: Universidad Técnica Nacional
Campus.......: Pacífico
Career.......: Tecnologías de Información
Course.......: ITI-321 - Programación III
Period.......: 3-2026
Documents....: Exam_01 - 01_Stack
Goals........: problema1 evalua la webada esa matematica
Professor....: Jorge Ruiz (york)
Student......: Luis Carlos Garcia Saenz
================================================================================================="""

from cls_Stack import cls_Stack

#RELACION DE CIERRE/ APERTURA
PARES = {")": "(", "]": "[", "}": "{"}
APERTURAS = set(PARES.values())

def vaciar(pila: cls_Stack) -> None:
    """Deja la pila vacía (se usa cuando el análisis termina antes de tiempo)."""
    while not pila.isempty():
        pila.pop()


def analizar_expresion(expresion: str) -> tuple[bool, str]:
    #Devuelve (esta_bien, mensaje) indicando si los agrupadores están balanceados
    pila = cls_Stack()

     # Restricción: la pila debe estar vacía antes de ser utilizada
    if not pila.isempty():
        return False,"error interno, no esta vacia al iniciar bro"

    resultado = (True, "La expresion está bien escrita")

    for posicion, caracter in enumerate(expresion, start=1):
        if caracter in APERTURAS:
            if pila.isfull():
                resultado = (False, f"No se puede evaluar pq hay más de 10 agrupadores abiertos "
                                    f"a la vez (posición {posicion}).")
                break
            pila.push((caracter, posicion))

        elif caracter in PARES:
            if pila.isempty():
                resultado = (False, f"mal escrita: '{caracter}' en la posición {posicion} "
                                    f"cerro un agrupador que nisiquiera abrio")
                break
            apertura, pos_apertura = pila.pop()
            if apertura != PARES[caracter]:
                resultado = (False, f"Mal escrita: '{apertura}' (posición {pos_apertura}) "
                                    f"se cierra con '{caracter}' (posición {posicion}).")
                break
    else:
        # Se recorrió toda la expresión: no deben quedar agrupadores sin cerrar
        if not pila.isempty():
            apertura, pos_apertura = pila.peek()
            resultado = (False, f"mal escrita: '{apertura}' en la posición {pos_apertura} "
                                f"nunca se cerro")

    # Restricción: la pila debe estar vacía al finalizar su uso
    vaciar(pila)
    assert pila.isempty(), "La pila debe quedar vacía al finalizar"
    return resultado

#este main es solo para que corra aqui
def main() -> None:
    print()
    print("Evaluación de las expresiones matematicas")
    print("=====================================")
    print("Digite una expresión (si pulsa enter vacio se sale jeje)")

    while True:
        expresion = input("\nExpresión: ").strip()
        if expresion == "":
            break
        esta_bien, mensaje = analizar_expresion(expresion)
        print(("Si, " if esta_bien else "no, ") + mensaje)

    print("\nFin del programa.")


if __name__ == "__main__":
    main()

