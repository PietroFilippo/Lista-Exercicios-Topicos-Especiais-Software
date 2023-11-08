"""
jogo da velha em um tabuleiro de tamanho variável NxN.
o tabuleiro é representado como uma lista de listas
onde cada elemento representa uma posição no tabuleiro.
`desenhar_tabuleiro` é responsável por exibir o estado atual do tabuleiro.
`verificar_vitoria` verifica se o jogador venceu o jogo, verificando todas as linhas, colunas e diagonais.
 jogar` inicia o jogo, para os jogadores inserir suas jogadas e verificando o resultado.

 -`tabuleiro`: lista de listas que representa o tabuleiro.
 -`atual_jogador`: variável que mostra qual jogador está jogando (começa com o jogador "X").
 -`jogadas`: variável que rastreia o número de jogadas feitas.
 -`tamanho_tabuleiro`: tamanho do tabuleiro, escolhido pelo usuário no início.
 - função `desenhar_tabuleiro`: desenha o tabuleiro na tela.
 - função `verificar_vitoria`: verifica se o atual jogador venceu o jogo.
 - função `jogar`: função principal que controla o loop do jogo, verifica jogadas válidas e o resultado do jogo.
"""

def desenhar_tabuleiro(tabuleiro):
    """desenha o tabuleiro na tela"""
    n = len(tabuleiro)
    for i in range(n):
        print(" | ".join(tabuleiro[i]))
        if i < n - 1:
            print("-" * (4 * n - 1))

def verificar_vitoria(tabuleiro, jogador):
    """verifica se o atual jogador ganhou o jogo"""
    n = len(tabuleiro)
    for i in range(n):
        if all([tabuleiro[i][j] == jogador for j in range(n)]) or all([tabuleiro[j][i] == jogador for j in range(n)]):
            return True
    if all([tabuleiro[i][i] == jogador for i in range(n)]) or all([tabuleiro[i][n - 1 - i] == jogador for i in range(n)]):
        return True

    return False

def jogar():
    """função principal do jogo para inicia-lo"""
    while True:
        try:
            tamanho_tabuleiro = int(input("Insira o tamanho do tabuleiro que deseja (NxN): "))
            if tamanho_tabuleiro > 1:
                break
            else:
                print("Insira um valor válido.")
        except ValueError:
            print("Insira um número maior que 1.")

    tabuleiro = [[" " for _ in range(tamanho_tabuleiro)] for _ in range(tamanho_tabuleiro)]
    atual_jogador = "X"
    jogadas = 0

    while True:
        desenhar_tabuleiro(tabuleiro)
        print(f"É a vez do jogador {atual_jogador}")
        try:
            linha = int(input(f"Insira o número da linha (1 a {tamanho_tabuleiro}): "))
            coluna = int(input(f"Insira o número da coluna (1 a {tamanho_tabuleiro}): "))

            if 1 <= linha <= tamanho_tabuleiro and 1 <= coluna <= tamanho_tabuleiro and tabuleiro[linha - 1][coluna - 1] == " ":
                tabuleiro[linha - 1][coluna - 1] = atual_jogador
                jogadas += 1

                if verificar_vitoria(tabuleiro, atual_jogador):
                    desenhar_tabuleiro(tabuleiro)
                    print(f"O jogador {atual_jogador} venceu.")
                    break

                if jogadas == tamanho_tabuleiro * tamanho_tabuleiro:
                    desenhar_tabuleiro(tabuleiro)
                    print("Empate.")
                    break

                atual_jogador = "O" if atual_jogador == "X" else "X"
            else:
                print("Jogada inválida. Tente novamente.")
        except ValueError:
            print("Insira um número válido.")

if __name__ == "__main__":
    jogar()
