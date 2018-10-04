# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 02:40:36 2018

@author: user
"""

#proxy 서버
from socket import *
import sys


#소켓 설정
tcpServerSocket = socket(AF_INET,SOCK_STREAM)
#주소,포트 연결, 응답시간
tcpServerSocket.bind(('localhost',8888))
tcpServerSocket.listen(10)

#데이터 받기
tcpClientSocket, addr = tcpServerSocket.accept()

#클라이언트로 메세지 받기/1024 비트? 버퍼
message = tcpClientSocket.recv(1024)
print(message)

#파일이름 파싱
filename = message.split()[1].decode().partition("/")[2]
fileExist = 'false' #파일 유무 불리언



try:
    print(filename)
    #프록시 역할 - 서버와 클라이언트 사이 중계(캐시역할)
    #파일 존재하면 열기 - 읽기모드
    f = open('C:\\Users\\user\\Downloads\\'+filename,'r')
    print('log1')
    outputdata = f.readlines()
    print('log2')
    fileExist = 'true'
    #cache hit, 파일 존재할 경우 응답
    #파일 읽어서 보내기
    tcpClientSocket.send('File is exist.'.encode())
    print('log3')
    for i in range(0,len(outputdata)):
        tcpClientSocket.send(outputdata[i].encode())
        
    print("complete")
    #파일 없을경우 예외처리
    #클라이언트 역할로 요청
except IOError:
    print('exception')
    
    if fileExist == 'false':
        #소켓만들기
        c = socket(AF_INET,SOCK_STREAM)
        #서버 호스트 - 임의로 지정했습니다.
        hostn = '121.198.1.151'
        try:
            #소켓연결,포트설정
            print('o')
            c.connect((hostn,80))
            print('k')
            #파일 만들고 가져오기
            fileobj = c.makefile('r',0)
            fileobj.write('GET '+'http://'+filename+" HTTP/1.0\r\n")
            #만든 파일 읽어오기
            print("fileobj is : " + fileobj)
            buff = fileobj.readlines()
            tmpFile = open('./ '+filename,'wb')
            #클라이언트한테 파일 보내기
            for line in buff:
                tmpFile.write(line)
                tcpClientSocket.send(line)
        except :#예외처리
            print('illegal request')
    else:
        #파일 없을때 에러메세지
        tcpClientSocket.send('No file'.encode())
    tcpClientSocket.close()
tcpServerSocket.close()
