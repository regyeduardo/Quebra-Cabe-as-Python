import readline
import os
import sys
from random import sample
from pynput.keyboard import Key, Listener

matriz = []
linha = coluna = 0
movimentos = 0


def clear():
    if sys.platform == "linux":
        os.system("clear")
    elif sys.platform == "win32" or "cygwin":
        os.system("cls")


def get_pointer():
    global linha, coluna, matriz
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            if matriz[x][y] == "*":
                linha = x
                coluna = y


def gera_matriz():
    valores = [valor for valor in range(1, 16)]
    valores.append("*")
    for i in range(4):
        # try:
        q = sample(valores, 4)
        for x in q:
            valores.remove(x)
        # except ValueError:
        #     q = sample(valores, 3)
        #     q.append("*")
        matriz.append(q)
    get_pointer()


def imprime_matriz():
    print(f"{' '*4}PUZZLE{' '*5}")
    print("-" * 20)
    for lista in matriz:
        linha = "  "
        for n_lista in lista:
            try:
                if n_lista < 10:
                    linha += f"0{str(n_lista)}  "
                else:
                    linha += f"{str(n_lista)}  "
            except TypeError:
                linha += f" {n_lista}  "
        print(f"|{linha}|")
    print("-" * 20)
    print("Pressione 'ESC' para sair")
    print(f"Movimentos {movimentos}")


def on_press(key):
    global linha, coluna, movimentos
    aux = ""
    if key == Key.up:
        if linha - 1 < 0:
            clear()
            print("Movimento Invalido\n")
        else:
            aux = matriz[linha - 1][coluna]
            matriz[linha - 1][coluna] = matriz[linha][coluna]
            matriz[linha][coluna] = aux
            linha -= 1
            movimentos += 1
            clear()
    elif key == Key.right:
        if coluna + 1 > 3:
            clear()
            print("Movimento Invalido\n")
        else:
            aux = matriz[linha][coluna + 1]
            matriz[linha][coluna + 1] = matriz[linha][coluna]
            matriz[linha][coluna] = aux
            coluna += 1
            movimentos += 1
            clear()
    elif key == Key.down:
        if linha + 1 > 3:
            clear()
            print("Movimento Invalido\n")
        else:
            aux = matriz[linha + 1][coluna]
            matriz[linha + 1][coluna] = matriz[linha][coluna]
            matriz[linha][coluna] = aux
            linha += 1
            movimentos += 1
            clear()
    elif key == Key.left:
        if coluna - 1 < 0:
            clear()
            print("Movimento Invalido\n")
        else:
            aux = matriz[linha][coluna - 1]
            matriz[linha][coluna - 1] = matriz[linha][coluna]
            matriz[linha][coluna] = aux
            coluna -= 1
            movimentos += 1
            clear()
    imprime_matriz()


def on_release(key):
    # print("{0} release".format(key))
    if key == Key.esc:
        # Stop listener
        print("Saindo...")
        return False
    elif verifica_jogo():
        print("Voce me derrotou...!")
        return False


def verifica_jogo():
    if (
        matriz[0] == [1, 2, 3, 4]
        and matriz[1] == [5, 6, 7, 8]
        and matriz[2] == [9, 10, 11, 12]
        and matriz[3] == [13, 14, 15, "*"]
    ):
        return True


if __name__ == "__main__":
    clear()
    gera_matriz()
    imprime_matriz()
    # Collect events until released
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
# gera_matriz()
# get_pointer()
