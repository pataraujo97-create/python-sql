import psycopg2
from config import DB_CONFIG

def conectar(): # ABRE A CONEXÃO COM O BANCO DE DADOS
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn #RETORNA A CONEXÃO COM QUEM CHAMOU A FUNÇÃO
    except Exception as e: # SE DER ERRO NA CONEXÃO CAPTURA E MOSTRA NA TELA SEM TRAVAR O PROGRAMA
        print(f"Erro ao conectar: {e}")
        return None

def desconectar(conn): #RECEBE A CONEXÃO E FECHA
    if conn: # GARANTE QUE SÓ TENTA FECHAR SE EXISTIR A CONEXÃO
        conn.close()