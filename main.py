import sys
import io
sys.stdin  = io.TextIOWrapper(sys.stdin.buffer,  encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from clientes import adicionar_cliente, listar_clientes, remover_cliente #Importa as 3 funções do cliente.py

while True:  #Cria um Loop até o usuário escolher a opção para SAIR
    print("\n1. Adicionar cliente") #MENU de interação 
    print("2. Listar clientes")
    print("3. Remover cliente")
    print("0. Sair")
    op = input("Opcao: ").strip()

    if op == "1": #selecionando o ADICIONAR CLIENTE  e pede NOME e idade
        nome  = input("Nome: ").strip()
        idade = input("Idade: ").strip()
        adicionar_cliente(nome, int(idade))
    elif op == "2": #Chama a função de listar os clientes
        listar_clientes()
    elif op == "3": # Chama a função para remover o cliente, caso confirmado o ID remove o cliente do banco de dados
        id_str = input("ID do cliente: ").strip()
        if id_str.isdigit():
            remover_cliente(int(id_str))
    elif op == "0": #Encerra o Loop e finaliza o programa.
        print("Ate logo!")
        break