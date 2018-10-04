# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 01:34:29 2018

@author: user
"""

#UDP pinger 서버
import random
from socket import *
#소켓 만들기
serverSocket = socket(AF_INET,SOCK_DGRAM)
#ip,포트 부여하기
serverSocket.bind(('localhost',8000))
while True:
    #임의의 수 생성하기
    rand = random.randint(0,10)
    #클라이언트한테 메세지랑 주소 받기
    message, address = serverSocket.recvfrom(1024)
    #메세지 대문자로 변환
    message = message.upper()
    #임의 수가 4보다 작으면 패킷손실로 설정
    if rand < 4:
        continue
    #4보다 크면 응답
    serverSocket.sendto(message,address)