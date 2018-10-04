from socket import *
import base64
import ssl

content = '15146312 박강민'
endmsg = "\r\n.\r\n" #점으로 끝을 인식
userID = 'wjdrmf314@gmail.com'
password = 'qkrrkdals314'
recipient = '<wjdrmf314@gmail.com>\r\n'
sender = '<wjdrmf314@gmail.com>'
#메일소켓 설정
mailSocket = socket(AF_INET, SOCK_STREAM)
#구글에서 제공하는 smtp 주소
mailSocket.connect(('smtp.gmail.com',587))#three-way handshaking
recv = mailSocket.recv(1024).decode()
print(recv)


#HELO 커맨드
mailSocket.send('HELO Alice\r\n'.encode())
recv1 = mailSocket.recv(1024).decode()
print(recv1)
#TLS연결 ( 포트 587 )
mailSocket.send('STARTTLS\r\n'.encode())
recv2 = mailSocket.recv(1024).decode()
print(recv2)
#SSL소켓 설정하기
sslmailSocket = ssl.SSLSocket(mailSocket)

print("Sending AUTH LOGIN command") #로그인 커맨드 
authCommand = 'AUTH LOGIN\r\n'
sslmailSocket.write(authCommand.encode())
recvAUTH = sslmailSocket.read(1024).decode()
print(recvAUTH)

UserID = base64.b64encode(userID.encode()) + "\r\n".encode() #사용자 ID 인코딩후 전송
sslmailSocket.write(UserID)
recvUserID = sslmailSocket.read(1024).decode()
print(recvUserID)

PSword = base64.b64encode(password.encode()) + '\r\n'.encode()  #사용자 PW 인코딩 후 전송
sslmailSocket.write(PSword)
recvPSword = sslmailSocket.read(1024).decode()
print(recvPSword)

sslmailSocket.send("MAIL FROM:".encode() + sender.encode() + "\r\n".encode())#MAIL FROM 명령어
recv1 = sslmailSocket.recv(1024).decode()
print(recv1)

sslmailSocket.send("RCPT TO:".encode() + recipient.encode()) #RCPT TO 명령어
recv1 = sslmailSocket.recv(1024).decode()
print(recv1)

sslmailSocket.send("DATA\r\n".encode()) #DATA 명령어
recv1 = sslmailSocket.recv(1024).decode()


sslmailSocket.send(content.encode()) #작성한 메세지 보내기


sslmailSocket.send(endmsg.encode()) #점으로 끝맺음
recv1 = sslmailSocket.recv(1024).decode()


QUIT = 'QUIT\r\n'.encode() #서버 접속종료
sslmailSocket.send(QUIT)
recv1 = sslmailSocket.recv(1024).decode()
print('compelte')