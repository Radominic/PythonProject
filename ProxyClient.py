# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 03:33:56 2018

@author: user
"""

#Proxy 클라이언트
import socket
#소켓 만들기
tcpClientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#서버 연결
tcpClientSocket.connect(('localhost',8888))

test = """
POST /Text.txt HTTP/1.1
Host: w3schools.com
name1=value1&name2=value2
"""
#테스트 메세지 보내기
tcpClientSocket.sendall(test.encode())
tcpClientSocket.settimeout(10)

while 1:				
    #1024버퍼로 메세지, 주소 받아오기
	message, address = tcpClientSocket.recvfrom(1024)
    #받아온 메세지 출력, 공백만날때 종료
	print(message.decode(),end='')
	if not message:
		break
	

tcpClientSocket.close()