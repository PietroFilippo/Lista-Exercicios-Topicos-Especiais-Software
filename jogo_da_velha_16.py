"""
um jogo da velha com 16 quadrados mas com as mesmas regras.
o tabuleiro é representado como uma lista de listas onde cada lista
interna representa uma linha do tabuleiro, os elementos podem ser "X","O" ou " ".

- desenhar_tabuleiro(tabuleiro): desenha o tabuleiro, mostrando as posições dos jogadores.
- verificar_vitoria(tabuleiro, jogador): verifica se o atual jogador ganhou, formando uma linha, coluna ou diagonal.
    - tabuleiro: tabuleiro do jogo representado como uma lista de listas.
    - jogador: símbolo do jogador ("X" ou "O") que está sendo verificado.
    - retorno: valor booleano (True se o jogador venceu, False se não).
- jogar(): função para iniciar o jogo.
"""

def desenhar_tabuleiro(tabuleiro):
    """desenha o tabuleiro na tela"""
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 17)

def verificar_vitoria(tabuleiro, jogador):
    """verifica se o atual jogador ganhou o jogo"""
    for i in range(4):
        if all([tabuleiro[i][j] == jogador for j in range(4)]) or all([tabuleiro[j][i] == jogador for j in range(4)]):
            return True
    if all([tabuleiro[i][i] == jogador for i in range(4)]) or all([tabuleiro[i][3 - i] == jogador for i in range(4)]):
        return True

    return False

def jogar():
    """função principal do jogo para inicia-lo"""
    tabuleiro = [[" " for _ in range(4)] for _ in range(4)]
    atual_jogador = "X"
    jogadas = 0

    while True:
        desenhar_tabuleiro(tabuleiro)
        print(f"É a vez do jogador {atual_jogador}")
        linha = int(input("Insira o número da linha em que deseje jogar. (1 a 4): ")) - 1
        coluna = int(input("Insira o número da coluna em que deseje jogar. (1 a 4): ")) - 1

        if 0 <= linha < 4 and 0 <= coluna < 4 and tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = atual_jogador
            jogadas += 1

            if verificar_vitoria(tabuleiro, atual_jogador):
                desenhar_tabuleiro(tabuleiro)
                print(f"O jogador {atual_jogador} venceu.")
                break

            if jogadas == 16:
                desenhar_tabuleiro(tabuleiro)
                print("Empate.")
                break

            atual_jogador = "O" if atual_jogador == "X" else "X"
        else:
            print("Jogada inválida. Tente novamente.")

if __name__ == "__main__":
    jogar()
