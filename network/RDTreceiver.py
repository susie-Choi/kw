from socket import *
from sys import *

def send(data, recv):
    send_sock.sendto(data.encode('utf-8'), recv)

if __name__ == '__main__':

    send_address = '127.0.0.1'
    send_port = 15002
    a_send = (send_address, send_port)

    recv_address = '127.0.0.1'
    recv_port = 15001
    a_recv = (recv_address, recv_port)

    send_sock = socket(AF_INET, SOCK_DGRAM)
    recv_sock = socket(AF_INET, SOCK_DGRAM)

    recv_sock.bind(a_recv)

    exp_seq = 0

    while True:
        message = recv_sock.recvfrom(1024) #최대 수신 가능한 데이터크기 4096bytes
        
        data = message[0] #메세지 리스트의 data값 받아오기
        de_data = data.decode('euc-kr')
        seq = de_data[-1]
        
        if seq == str(exp_seq):
            print(" Right sequence ")
            send("ACK"+seq, a_send)
            stdout.write(de_data)
            exp_seq = 1 - exp_seq

        else:
            print(" Wrong sequence ")
            neg_seq = str(1 - exp_seq)
            send("ACK"+neg_seq, a_send)
            
    
