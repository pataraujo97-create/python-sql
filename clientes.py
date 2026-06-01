from database import conectar, desconectar #Importa as funções conectar e desconectar do database

def adicionar_cliente(nome, idade): #adiciona o cliente
    conn = conectar() #conecta com o banco de dados
    if not conn: #retorna se falhar
        return
    try:
        cur = conn.cursor() #cria um cursor que executa os comandos do SQL dentro do Python
        cur.execute(
            "INSERT INTO clientes (nome, idade) VALUES (%s, %s) RETURNING id;",
            (nome, idade) #executa os comentos do SQL dentro do Python
        )
        novo_id = cur.fetchone()[0] #pega o id gerado e confirma que o cliente foi cadastrado
        conn.commit()
        print(f"Cliente cadastrado! ID: {novo_id}")
    except Exception as e: # Se algo der errado dezfaz tudo com o rollback para não salvar dados pela metade
        conn.rollback()
        print(f"Erro: {e}")
    finally: #sempre executa com ou sem erro e fecha a conexão
        cur.close()
        desconectar(conn)

def listar_clientes(): #Lista os clientes
    conn = conectar()   
    if not conn: # Abre a conexão e para se Falhar
        return
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, nome, idade FROM clientes ORDER BY id;") #Executa o Select e guarda os resultados na lista chamada Clientes
        clientes = cur.fetchall()
        if not clientes:
            print("Nenhum cliente cadastrado.") # Se a lista retornar vazia informa e para
            return
        print("\nID | Nome | Idade") #Percorre a lista e informa o ID/Nome/Idade
        print("-" * 30)
        for c in clientes:
            print(f"{c[0]} | {c[1]} | {c[2]}")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        cur.close()
        desconectar(conn)

def remover_cliente(cliente_id): # Função para Remover os clientes
    conn = conectar()
    if not conn:
        return
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM clientes WHERE id = %s;", (cliente_id,)) # Executa o DELETE filtrando pelo ID e confirma com o commit
        conn.commit() 
        print(f"Cliente {cliente_id} removido!") 
    except Exception as e:
        conn.rollback()
        print(f"Erro: {e}")
    finally:
        cur.close()
        desconectar(conn)
        #invincia cabrincia