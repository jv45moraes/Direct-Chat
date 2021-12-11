import socket   #importação do conjunto de comandos da biblioteca responsavel pela conexao
import threading  #importação da biblioteca threading para realizacao de trabalhos com multiplexacao de execucao

# declaracao das variaveis responsaveis por portar as informacoes referentes a porta a ser utilizada e o endereco IPV6 do usuario.
host = "::"
porta= 567

# adicionando variavel responsavel pela criptografia das mensagens enviadas e recebidas
cod = "ascii"

# Definindo conexao ipv6(AF_INET6) e UDP (SOCK_DGRAM)
conexao= socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
#iniciando conexão
conexao.bind((host,porta))

#listando clientes e seus apelidos para definir receptor das mensagens
cli = []
nick = []

#metodo para realizar envio das mensagens
def ms(nick,m,cliente):
    if(nick in nick):#verifica se o respectivo usuario esta conectado no momento
        usuario = cli[nick.index(nick)]# pega o respectivo nickname da lista de clientes 
        nome = nick[cli.index(cli)]
        msg = f"{nome} ]===> {m}" # passa no envio o nick das informaçoes referentes a quem enviou e quem recebeu a mensagem
        conexao.sendto(msg.encode(cod),usuario) #estabelece a conexao para envio da mensagem

    else:# caso o cliente destino esteja desconectado, ele retorna essa informaçao
        msg = f"{nick} esta off"
        conexao.sendto(msg.encode(cod),cliente)# cria a conexao para envio da mensagem

#define a forma como a mensagem deve ser enviada, onde o nickname vem antes , ai vem | e depois a mensagem
def geral(msg,cliente):
    if("|" in msg): #verifica se a mensagem foi enviada no formato correto, estando o nickname antes da | e mensagem depois
        msg = msg.split("|") # estabelece a separação de string usando -> |
        ms(msg[0],msg[1],cliente)

    else: #Retorna informacao de erro, caso ele ocorra
        print("erro 01")
    
# laço de repetição para receber todas as mensagens
while True:
    msg, cliente = conexao.recvfrom(1024) # estabelece a conexão e o tamanho da mensagem
    if(cliente in cli): #verifica se o usuario é valido
        geral(str(msg.decode(cod)),cliente) #decodifica a mensagem e passa ao cliente
    else: #se não estiver entre os usuarios, vai enviar o nickname
        nick = msg.decode(cod)
        nick.append(nick)
        cli.append(cliente)