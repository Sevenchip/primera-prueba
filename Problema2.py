"""=================================================================================================
Institute....: Universidad Técnica Nacional
Campus.......: Pacífico
Career.......: Tecnologías de Información
Course.......: ITI-321 - Programación II
Period.......: 1-2026
Documents....: Exam_01 - Problema2
Goals........: en busca de la reina de corazones jiji (cls_Stack por composicion en cada jugador)
Professor....: Jorge Ruiz (york)
Student......: Luis Carlos García Sáenz
================================================================================================="""
from time import sleep

from cls_Stack import cls_Stack
import Subrutinas

REINA_CORAZONES = "QC"
ESPERA_SEGUNDOS = 1
ANCHO_COLUMNA = 12


class Jugador:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        #cada jugador lleva su propia partida osea pila de naipes
        self.partida = cls_Stack()
        self.obtenidos: list[str] = []   # naipes que ha ido sacando durante el juego
        #la pila debe estar vacia antes de ser utilizada
        if not self.partida.isempty():
            raise RuntimeError("La partida debe estar vacia al iniciar")

    def recibir_naipe(self, naipe: str) -> None:
        if not self.partida.isfull():
            self.partida.push(naipe)

    def tiene_naipes(self) -> bool:
        return not self.partida.isempty()

    def jugar_turno(self) -> str:
        naipe = self.partida.pop()
        self.obtenidos.append(naipe)
        return naipe

    def limpiar_partida(self) -> None:
        #vacia la pila al terminar el juego (puede quedar con naipes si alguien gano antes)
        while not self.partida.isempty():
            self.partida.pop()
        assert self.partida.isempty(), "La partida debe quedar vacía al finalizar"

def imprimir_encabezado(jugadores: list[Jugador]) -> None:
    #imprime los nombres de los jugadores uno en cada columna
    print("".join(j.nombre.ljust(ANCHO_COLUMNA) for j in jugadores))
    print("".join(("-" * len(j.nombre)).ljust(ANCHO_COLUMNA) for j in jugadores))


def imprimir_naipe(naipe: str) -> None:
    #imprime el naipe de un jugador en su columna (esta vacio si ya no tiene naipes)."""
    print(naipe.ljust(ANCHO_COLUMNA), end="", flush=True)


def jugar(jugadores: list[Jugador]) -> None:
    #arranca el juego por turnos hasta que salga la Reina de corazones o se acaben los naipes... deberia
    imprimir_encabezado(jugadores)

    while any(j.tiene_naipes() for j in jugadores):
        for jugador in jugadores:
            naipe = jugador.jugar_turno() if jugador.tiene_naipes() else ""
            imprimir_naipe(naipe)

            if naipe == REINA_CORAZONES:
                print()
                return

            sleep(ESPERA_SEGUNDOS)   # espera q entre un jugador y el siguiente
        print()                      # fin de la fila


def calcular_ganador(jugadores: list[Jugador]) -> Jugador | None:
    #el ganador es quien le salio la reina de corazones, si nadie la obtuvo, None
    return next((j for j in jugadores if REINA_CORAZONES in j.obtenidos), None)


def obtener_corazones(ganador: Jugador) -> list[str]:
    #los naipes de corazones acumulados por el ganador
    return [n for n in ganador.obtenidos if n.endswith("C")]
    #f n.endswith("C"): es el filtro osea solo pasan los naipes cuyo texto termina en "C", que es la letra de corazones
    # Alternativa con lambda + filter:
    # return list(filter(lambda n: n.endswith("C"), ganador.obtenidos))


def imprimir_corazones(ganador: Jugador, corazones: list[str]) -> None:
    print(f"Corazones acumulados por {ganador.nombre}: {corazones}")

def main() -> None:
    print()
    print("Buscando a la Reina de Corazones")
    print("================================")

    nombres = ["Merlina", "Pericles", "Tío Lucas", "Homero"]
    jugadores = [Jugador(nombre) for nombre in nombres]

    Subrutinas.repartir_naipes(jugadores)
    jugar(jugadores)

    ganador = calcular_ganador(jugadores)
    print()
    if ganador is None:
        print("Nadie obtuvo la Reina de Corazones: los jugadores se quedaron sin naipes.")
    else:
        print(f"¡{ganador.nombre} obtuvo la Reina de Corazones!")
        imprimir_corazones(ganador, obtener_corazones(ganador))

    # Restricción: las pilas deben quedar vacías al finalizar
    for jugador in jugadores:
        jugador.limpiar_partida()


if __name__ == "__main__":
    main()
