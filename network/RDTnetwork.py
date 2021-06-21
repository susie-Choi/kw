from socket import *
from sys import *
import random
import time

#Network

def usage():
    print ("Usage: python RDTnetwork.py")
    exit()


def RTT1(): #실험시간t1 : uniform random amount of time between 8 and 12ms.

    delay = random.random() * 0.002
    sign = random.randint(0, 1)
    if (sign == 1):
        delay = -delay
    delay += 0.01
    time.sleep(delay)

def RTT2(): #실험시간t2 : uniform random amount of time between 80 and 120ms.

    delay = random.random() * 0.02
    sign = random.randint(0, 1)
    if (sign == 1):
        delay = -delay
    delay += 0.1
    time.sleep(delay)


def corrupt(pkt): # bit 오류 발생
    index = random.randint(0, len(pkt)-1)
    print(pkt[:index])
    print(pkt[index+1:])
    pkt = pkt[:index] + pkt[index+1:]
    return pkt


def intercept(pkt, outSock, addr):
    rand = random.randint(0,10**6)
    """전송 오류율 조정, p_e : 0.1, 0.01, 0.001
    전송 오류율 = 손실(1/2) + bit오류(1/2)으로 설정
    현재 0.1로 조정.
    """
    if rand >= 1 and rand <= 5:
        print ("Dropped") # 손실 발생
        return
    elif rand >= 6 and rand <= 10:
        pkt = corrupt(pkt)
        print ("Corrupted to:", pkt) #bit 오류 발생

    outSock.sendto(pkt, addr)
        

if len(argv) != 1:
    usage()

fromSenderAddr = ('localhost', 15000)
toReceiverAddr = ('localhost', 15001)
fromReceiverAddr = ('localhost', 15002)
toSenderAddr = ('localhost', 15003)

fromSenderSock = socket(AF_INET, SOCK_DGRAM)
fromSenderSock.bind(fromSenderAddr)
fromSenderSock.setblocking(0)
fromReceiverSock = socket(AF_INET, SOCK_DGRAM)
fromReceiverSock.bind(fromReceiverAddr)
fromReceiverSock.setblocking(0)

outSock = socket(AF_INET, SOCK_DGRAM)

print("")
print("-----------------RDT 3.0 protocol with UDP-----------------")
print("|                                                         |")
print("--------------------Waiting for signal---------------------")

time_end = time.time() + 10 #t_m / 10초동안 실현될때, 실험시간 조정 필요
while True: 
    if time.time() > time_end:
        break

    RTT1()

    try:
        pkt = fromSenderSock.recv(1024)
        print ("Received packet from RDTsender:", pkt)
        intercept(pkt, outSock, toReceiverAddr)
    except error:
        pass
    try:
        pkt = fromReceiverSock.recv(1024)
        print ("Received packet from RDTreceiver:", pkt)
        intercept(pkt, outSock, toSenderAddr)
    except error:
        pass
