"""
jogo simulando term.oo.
o programa lê uma lista de palavras da lista_palavras.txt e seleciona uma palavra aleatória, removendo seus acentos.
há um limite de 6 tentativas para adivinhar a palavra, com feedback das tentativas mostrando as cores preto, amarelo e verde.

- são usadas listas para armazenar as palavras do arquivo e as tentativas do jogador.
- são usados dicionários para mapear caracteres com acentos para seus equivalentes sem acentos.
- são usadas strings para representar a palavra oculta escolhida aleatóriamente, as tentativas do jogador e o teclado.
- `remover_acentos(palavra)`: remove acentos.
- `escolher_palavra()`: escolhe aleatoriamente uma palavra.
- `verificar_palavra(palavra_oculta, tentativa)`: verifica uma tentativa do jogador e fornece o feedback.
- `desenhar_teclado(letras_utilizadas)`: desenha o teclado.
- `atualizar_teclado(palavra_oculta, letras_corretas, letras_utilizadas)`: atualiza o teclado.
- `main()`: inicia o jogo.
"""
import random

def remover_acentos(palavra):
    """
        palavra (str): palavra da qual se deseja remover os acentos.
        str: a palavra sem acentos.
    """
    acentos = {
        'á': 'a', 'à': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a',
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
        'ó': 'o', 'ò': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o',
        'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
        'ç': 'c'
    }
    
    sem_acentos = ''.join(acentos.get(char, char) for char in palavra)
    return sem_acentos

def escolher_palavra():
    """
        tupla: tupla com a palavra oculta e o tamanho da palavra.
    """
    with open("lista_palavras.txt", "r", encoding="utf-8") as arquivo:
        palavras = arquivo.readlines()
    
    palavras = [remover_acentos(palavra.strip()) for palavra in palavras]

    palavra_oculta = random.choice(palavras)
    tamanho_palavra = len(palavra_oculta)
    return palavra_oculta, tamanho_palavra

def verificar_palavra(palavra_oculta, tentativa):
    """
        palavra_oculta (str): palavra que o usuário está tentando adivinhar.
        tentativa (str): tentativa do usuário.
        tupla: tupla com o feedback e as letras corretas.
    """
    feedback = []
    letras_corretas = [] 
    for i in range(len(palavra_oculta)):
        if tentativa[i] == palavra_oculta[i]:
            feedback.append((tentativa[i].upper(), "\033[32m"))  
            letras_corretas.append(tentativa[i])
        elif tentativa[i] in palavra_oculta:
            feedback.append((tentativa[i].upper(), "\033[33m")) 
        else:
            feedback.append((tentativa[i].upper(), "\033[37m"))  
    return feedback, letras_corretas

def desenhar_teclado(letras_utilizadas):
    """
        letras_utilizadas (list): lista das letras já tentadas pelo usuário.
        str: teclado desenhado.
    """
    layout_teclado = [
        "QWERTYUIOP",
        "ASDFGHJKL",
        "ZXCVBNM"
    ]

    teclado = ""
    for linha in layout_teclado:
        for letra in linha:
            cor = "\033[0m"
            teclado += f"{cor}{letra} "
        teclado += "\n"
    return teclado

def atualizar_teclado(palavra_oculta, letras_corretas, letras_utilizadas):
    """
        palavra_oculta (str): palavra que o usuário está tentando adivinhar.
        letras_corretas (list): lista das letras corretas adivinhadas pelo usuário.
        letras_utilizadas (list): lista das letras já tentadas pelo usuário.
        str: teclado atualizado.
    """
    layout_teclado = [
        "QWERTYUIOP",
        "ASDFGHJKL",
        "ZXCVBNM"
    ]

    novo_teclado = ""

    for linha in layout_teclado:
        for letra in linha:
            if letra.lower() in letras_utilizadas:
                if letra.lower() in [l.lower() for l in letras_corretas]:
                    novo_teclado += f"\033[32m{letra} \033[0m"
                elif letra.lower() in [l.lower() for l in palavra_oculta] and letra.lower() not in [l.lower() for l in letras_corretas]:
                    novo_teclado += f"\033[33m{letra} \033[0m"
                else:
                    novo_teclado += f"\033[30m{letra} \033[0m"  
            else:
                novo_teclado += f"{letra} "
        novo_teclado += "\n"

    return novo_teclado

def main():
    """
        inicia o jogo
    """
    tentativas_maximas = 6
    palavra_oculta, tamanho_palavra = escolher_palavra()
    tentativas = 0
    letras_utilizadas = []
    letras_corretas = []
    letras_corretas_adivinhadas = [] 

    teclado = desenhar_teclado(letras_utilizadas)

    tentativas_restantes = tentativas_maximas  

    print()
    print(f"Adivinhe a palavra de {tamanho_palavra} letras (Palavras não possuem acentos.)")
    
    tentativas_restantes_str = f"Você tem {tentativas_restantes} tentativas"  
    
    print(tentativas_restantes_str)
    print()
    print(teclado)  
    print()

    tentativas_impressas = []

    while tentativas < tentativas_maximas:
        tentativa = input(f"Tentativa {tentativas + 1}: ").lower()

        if len(tentativa) != tamanho_palavra or not tentativa.isalpha():
            print(f"Insira uma palavra de {tamanho_palavra} letras válida.")
            continue

        feedback, letras_acertadas = verificar_palavra(palavra_oculta, tentativa)
        letras_utilizadas.extend(tentativa)  
        letras_corretas.extend(letras_acertadas)  #
        letras_corretas_adivinhadas.extend(letras_acertadas)  

        tentativas_impressas.append((tentativa, feedback)) 

        print("\033[H\033[J")

        print(f"Adivinhe a palavra de {tamanho_palavra} letras.")
        
        tentativas_restantes -= 1  
        tentativas_restantes_str = f"Você tem {tentativas_restantes} tentativas"  
        
        print(tentativas_restantes_str)
        print()

        teclado = atualizar_teclado(palavra_oculta, letras_corretas, letras_utilizadas)

        print(teclado)

        for t, f in tentativas_impressas:
            feedback_str = " ".join([f"{cor}{letra}\033[0m" for letra, cor in f])
            print(f"{feedback_str}")

        tentativas += 1

        if set(letras_corretas_adivinhadas) == set(palavra_oculta):
            print(f"Você adivinhou a palavra correta: {palavra_oculta}")
            break
    else:
        print(f"A palavra correta era: {palavra_oculta}")

if __name__ == "__main__":
    main()