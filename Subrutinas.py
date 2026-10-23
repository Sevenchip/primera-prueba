import random
# means of char
# B = Bastos o pica
# C = Corazones
# D = Diamantes
# T = Treboles

baraja = [["1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B", "10B", "JB", "QB", "KB"],
          ["1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC"],
          ["1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"],
          ["1T", "2T", "3T", "4T", "5T", "6T", "7T", "8T", "9T", "10T", "JT", "QT", "KT"]]



def repartir_naipes(jugadores) -> None:
    """Reparte un naipe a la vez a cada jugador, de forma aleatoria y sin repetir naipes,
    hasta que la pila de cada jugador alcance su tope (10 naipes)."""
    # Se "aplana" la baraja (lista de listas) en una sola lista de naipes disponibles
    disponibles = [naipe for palo in baraja for naipe in palo]

    while not all(j.partida.isfull() for j in jugadores):
        for jugador in jugadores:
            if jugador.partida.isfull():
                continue
            if not disponibles:
                return  # ya no quedan naipes en la baraja
            naipe = random.choice(disponibles)
            disponibles.remove(naipe)   # garantiza que nadie más reciba este naipe
            jugador.recibir_naipe(naipe)

