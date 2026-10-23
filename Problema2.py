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
ESPERA_SEGUNDOS = 2
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
        #Vacia la pila al terminar el juego (puede quedar con naipes si alguien gano antes)
        while not self.partida.isempty():
            self.partida.pop()
        assert self.partida.isempty(), "La partida debe quedar vacía al finalizar"
