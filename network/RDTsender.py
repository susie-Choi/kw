from socket import *
from sys import *

def usage():
    print ("Usage: python RDTsender.py file.txt")
    exit()

if __name__ == "__main__":


    send_address = '127.0.0.1'
    send_port = 15000
    a_send = (send_address, send_port)

    recv_address = '127.0.0.1'
    recv_port = 15003
    a_recv = (recv_address, recv_port)

    if len(argv) != 2:
        usage()
    filename = argv[1] #python RDTsender.py file.txt입력

    with open(filename) as f:
        data = f.readlines()

    send_sock = socket(AF_INET, SOCK_DGRAM)
    recv_sock = socket(AF_INET, SOCK_DGRAM)

    recv_sock.bind(a_recv)

    trans_delay = 0.008
    prop_delay = 0.012
    sum_time = trans_delay + prop_delay
    
    recv_sock.settimeout(3+sum_time)

    seq = 0

    return_true = True
    
    while return_true:
        for elem in data:
            send_sock.sendto((elem[:-1]+'.'+str(seq)).encode('utf-8'), a_send)
            try:
                message = recv_sock.recvfrom(1024)
            except timeout:
                print ("Timeout")
            else:
                print (message[0])
                ack_seq = message[0]
                if ack_seq == str(seq):
                    return_true = False
            seq = 1 - seq
            
        
