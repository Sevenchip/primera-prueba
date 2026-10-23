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
