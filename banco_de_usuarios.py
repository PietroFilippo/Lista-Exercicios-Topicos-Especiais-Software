"""
programa para gerenciar registros de usuários. utiliza estruturas como listas e dicionários.
o código apresenta um menu com opções interativas, permitindo ao usuário escolher entre cadastrar
um novo usuário, imprimir todos os usuários ou imprimir com filtros.

- banco_usuarios (lista): armazena os registros de usuários como dicionários.
- cadastrar_usuario (função):
   - cadastrar um novo usuário.
   - pede por informações obrigatórias e opcionais campos extras.
   - armazena os dados em um dicionário e adiciona o dicionário à lista banco_usuarios.
- imprimir_usuarios (função):
   - imprimir os registros de usuários com várias opções de filtro.
   - imprimir todos os usuários, filtrar por nomes, filtrar por campos e valores.
- main (função principal):
   - função principal que inicia o programa.
   - solicita os nomes dos campos obrigatórios para o cadastro de usuários.
   - mostra um menu interativo para o usuário escolher entre as opções.
   - programa continua em execução até que o usuário escolha encerrá-lo.
"""

banco_usuarios = []

def cadastrar_usuario(campos_obrigatorios):
    """função para cadastrar um usuário"""
    usuario = {}
    for campo in campos_obrigatorios:
        valor = input(f"Insira o valor para '{campo.strip()}': ") 
        usuario[campo.strip()] = valor
    while True:
        campo_extra = input("Insira um campo extra (ou 'sair'): ")
        if campo_extra.lower() == 'sair':
            break
        valor_extra = input(f"Insira o valor para '{campo_extra.strip()}': ")  
        usuario[campo_extra.strip()] = valor_extra
    banco_usuarios.append(usuario)
    print("Usuário cadastrado.")

def imprimir_usuarios(*args, **kwargs):
    """função para cadastrar um usuário"""
    if not args and not kwargs:
        if not banco_usuarios:
            print("Não há cadastros para imprimir.")
        else:
            for usuario in banco_usuarios:
                print(usuario)
    elif args and not kwargs:
        encontrados = []
        for nome in args:
            for usuario in banco_usuarios:
                if usuario.get('nome') == nome.strip(): 
                    encontrados.append(usuario)
        if not encontrados:
            print("Não há cadastros com os valores inseridos.")
        else:
            for usuario in encontrados:
                print(usuario)
    elif not args and kwargs:
        encontrados = False
        for usuario in banco_usuarios:
            atende_condicoes = True
            for campo, valor in kwargs.items():
                if usuario.get(campo) != valor:
                    atende_condicoes = False
                    break
            if atende_condicoes:
                print(usuario)
                encontrados = True
        if not encontrados:
            print("Não há cadastros com os valores inseridos.")
    elif args and kwargs:
        encontrados = []
        for nome in args:
            for usuario in banco_usuarios:
                if usuario.get('nome') == nome.strip(): 
                    atende_condicoes = True
                    for campo, valor in kwargs.items():
                        if usuario.get(campo) != valor:
                            atende_condicoes = False
                            break
                    if atende_condicoes:
                        encontrados.append(usuario)
        if not encontrados:
            print("Não há cadastros que com os valores inseridos.")
        else:
            for usuario in encontrados:
                print(usuario)
                
def main():
    """função principal"""
    campos_obrigatorios = input("Insira os nomes dos campos obrigatórios (separados por vírgula): ").split(',')
    while True:
        print("\nMENU:")
        print("1 - Cadastrar usuário")
        print("2 - Imprimir usuários")
        print("0 - Encerrar")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            cadastrar_usuario(campos_obrigatorios)
        elif escolha == '2':
            print("1 - Imprimir todos")
            print("2 - Filtrar por nomes")
            print("3 - Filtrar por campos")
            print("4 - Filtrar por nomes e campos")
            subescolha = input("Escolha uma opção: ")
            if subescolha == '1':
                imprimir_usuarios()
            elif subescolha == '2':
                nomes = input("Insira os nomes para filtrar (separados por vírgula): ").split(',')
                imprimir_usuarios(*nomes)
            elif subescolha == '3':
                campos = input("Insira os campos para filtrar (separados por vírgula): ").split(',')
                kwargs = {}
                for campo in campos:
                    valor = input(f"Insira o valor para '{campo.strip()}': ")  
                    kwargs[campo.strip()] = valor.strip()  
                imprimir_usuarios(**kwargs)
            elif subescolha == '4':
                nomes = input("Insira os nomes para filtrar (separados por vírgula): ").split(',')
                campos = input("Insira os campos para filtrar (separados por vírgula): ").split(',')
                kwargs = {}
                for campo in campos:
                    valor = input(f"Insira o valor para '{campo.strip()}': ")  
                    kwargs[campo.strip()] = valor.strip()  
                imprimir_usuarios(*nomes, **kwargs)
            else:
                print("Opção inválida.")
        elif escolha == '0':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
