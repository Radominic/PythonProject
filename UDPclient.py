# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 01:52:19 2018

@author: user
"""

#UDP pinger 클라이언트
import time
from socket import*
#서버 이름,포트 입력
serverName = 'localhost'
serverPort = 8000
#소켓 설정
clientSocket = socket(AF_INET,SOCK_DGRAM)
clientSocket.settimeout(1)
for i in range(10):
    message = "ping " + str(i) + " " + time.asctime()
    try:
        time1 = time.time()
        #서버로 메세지 인코딩해서 보내기
        clientSocket.sendto(message.encode(),(serverName, serverPort))
        #응답 메세지,주소 받기
        responseMessage,serverAddress = clientSocket.recvfrom(1024)
        #응답 서버 주소 띄우기
        print("Reply from" + serverAddress[0] + " : " +responseMessage.decode())
        print("RTT: "+str(time.time()-time1))
    except:
        print('Request timed out')
clientSocket.close()
