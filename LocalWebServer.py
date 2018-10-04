# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 10:22:07 2018

@author: user
"""
import http.server

class Handler(http.server.BaseHTTPRequestHandler):
    """HTTP 요청을 처리하는 클래스"""
    def do_GET(self):
        """요청 메시지의 메서드가 GET 일 때 호출되어, 응답 메시지를 전송한다."""
        # 응답 메시지의 상태 코드를 전송한다
        self.send_response(200)

        # 응답 메시지의 헤더를 전송한다
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        
        # 응답 메시지의 본문을 전송한다
        self.wfile.write(bytes('안녕하세요!\n', 'utf-8'))
        self.wfile.write(bytes('클라이언트가 요청한 경로: ', 'utf-8'))
        self.wfile.write(bytes(self.path, 'utf-8'))

# 요청받을 주소 (요청을 감시할 주소)
address = ('localhost', 8000)

# 요청 대기하기
listener = http.server.HTTPServer(address, Handler)
print(f'http://{address[0]}:{address[1]} 주소에서 요청 대기중...')
listener.serve_forever()