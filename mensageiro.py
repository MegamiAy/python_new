# no python a identação define se algo está dento ou fora de um bloco
# importação das bibliotecas 
import socket       # permite comunicação com a camada de transporte
import threading    # permite executar várias funções em paralelo
import time         # permite acessar o relógio do computador
import queue        # permite trabalhar com fluxo de mensagens

# pergunta ao usuário qual o IP da máquina para se comunicar
ip_destino = input("IP para conversar: ")

# define a porta que será usada para comunicação
port = 12345

# cria uma fila para controlar as mensagens recebidas
mensgens_recebidas = queue.Queue()

# função para receber as mensagens e coloca-lás na fila
def receber_msgs():
    # configura a sockert para conversar com a camada de transporte
    # para receber as mensagens
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(1)
    print("Aguardando conexão para receber mensagens")

    # aceita a conexão quando o outro computador esiver pronto
    conn, addr, server = server_socket.accept()
    print(f"Conectado com {addr}")
    
