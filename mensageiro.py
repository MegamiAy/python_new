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
def receber_msg():
    # configura a sockert para conversar com a camada de transporte
    # para receber as mensagens
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(1)
    print("Aguardando conexão para receber mensagens")

    # aceita a conexão quando o outro computador esiver pronto
    conn, addr = server_socket.accept()
    print(f"Conectado com {addr}")

    # recebe mensagens 
    while True:
        mensagem = conn.recv(1024).decode()
        if mensagem.lower() == 'fui-me':
            print("O outro usuário encerrou a conexão.")
            break
        # adiciona a mensagem recebida na fila
        mensagens_recebidas.put(f"=={mensagem}")
    conn.close()
    server_socket.close()

# função para enviar mensagens
def enviar_msg():
    # cria um socket para enviar mensagens
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #tenta conectar com o outro computador
    while True:
        try:
            client_socket.connect((ip_destino, port))
            printf("Conectado. Pronto para enviar mensagens.")
            break
        except ConnectionRefusedError:
            print("O outro usuáio não está pronto. Tentando em 3 segundos")
            time.sleep(3)
            
    # loop para envio de mensagens
    while True:
        mensagem = input(': ')
        client_socket.send(mensagem.enconde())
        if mensagem.lower() == 'fui-me'
            break
        
    client_socket.close()

# função para exibir as msg da fila
def exibir_msg():
    while True:
        while not mensagens_recebidas.empty()
            # imprime cada mensagem da fila
            print(mensagens_recebidas.get())
        # aguarda o intevalo de tempo para verificar a fila novamente
        time.sleep(0.1)

# executa as funções de receber, enviar e exibir as mensagens
# ao mesmo tempo
threading.Thread(target=receber_msg, deamon=True).start()
threading.Thread(target=enviar_msg).start()
threading.Thread(target=exibir_msg, deamon=True).start()
