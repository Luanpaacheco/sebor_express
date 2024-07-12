import os
restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False
                },{'nome': 'pizzaria', 'categoria': 'pizza', 'ativo': True},
                {'nome': 'canina', 'categoria': 'italiana', 'ativo': False }]

def exibir_nome_do_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░

    """)
    
    
def finaliza_app():
    os.system("cls")
    print("finalizando o app\n")
    

def opcao_invalida():
    print("opcao invalida\n")
    input("digite uma tecla e volte ao menu principal:")
    os.system("cls")
    voltar_menu_pricipal()

def exibir_opcoes():   
   
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restuarante")
    print("4. Sair\n")


def cadastrar_nome_restaurantes(texto):
    exibir_subtitulo(texto)
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_do_restaurante)
    print(f"o restaurante {nome_do_restaurante} foi cadastrada\n")
    voltar_menu_pricipal()
     


def listar_restaurantes(texto):
    os.system("cls")
    exibir_subtitulo(texto)
    print("Lista de restaurantes\n")
    for restaurante in restaurantes:
        nome_restaurante=restaurante["nome"]
        categoria_restaurante=restaurante["categoria"]
        print(f"-{nome_restaurante} | {categoria_restaurante}") 
    voltar_menu_pricipal()
    

def escolher_opcao():
    try: 
        opcao_escolhida = int(input("Escolha uma opção: "))
        
        match opcao_escolhida:
            case 1:
                cadastrar_nome_restaurantes("""
█▀▀ ▄▀█ █▀▄ ▄▀█ █▀ ▀█▀ █▀█ ▄▀█   █▄░█ █▀█ █░█ █▀█ █▀   █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀ █▀
█▄▄ █▀█ █▄▀ █▀█ ▄█ ░█░ █▀▄ █▀█   █░▀█ █▄█ ▀▄▀ █▄█ ▄█   █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄ ▄█
""")
            case 2:
                listar_restaurantes("""
█░░ █ █▀ ▀█▀ ▄▀█   █▀▄ █▀▀   █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀ █▀
█▄▄ █ ▄█ ░█░ █▀█   █▄▀ ██▄   █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄ ▄█""")
            case 3:
                exibir_subtitulo("""
▄▀█ ▀█▀ █ █░█ ▄▀█ █▀▀ ▄▀█ █▀█   █▀▄ █▀▀   █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀ █▀
█▀█ ░█░ █ ▀▄▀ █▀█ █▄▄ █▀█ █▄█   █▄▀ ██▄   █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄ ▄█""")
            case 4:
                print('Finalizar app')
            case _:
                opcao_invalida()
    except:
        opcao_invalida()    
    
    
    
    
def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


def exibir_subtitulo(texto):
    os.system("cls")
    print(texto,"\n")

def voltar_menu_pricipal():
    input("\nDigite uma tecla para voltar ao menu: ")
    main()
    
if __name__=="__main__":
    main()
    
    

# print(f"Voce escolheu {opcao_escolhida}!")
