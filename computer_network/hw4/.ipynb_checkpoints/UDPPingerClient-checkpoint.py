# UDPPingerClient.py
import time
from socket import *

# 서버의 IP 주소와 포트 번호 설정
serverName = '127.0.0.1'
serverPort = 12000

# UDP 소켓 생성
clientSocket = socket(AF_INET, SOCK_DGRAM)

# 소켓의 타임아웃 설정 (1초)
clientSocket.settimeout(1)

# 10번의 Ping을 실행
for sequence_number in range(1, 11):
    # 현재 시간을 메시지에 포함하여 서버로 전송
    message = f'Ping {sequence_number} {time.time()}'
    start = time.time()  # 메시지를 보낸 시간 기록
    try:
        # 메시지를 서버로 전송
        clientSocket.sendto(message.encode(), (serverName, serverPort))

        # 서버로부터 응답 받기
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)

        # RTT 계산
        end = time.time()
        rtt = end - start

        # 결과 출력
        print(f'Received from server: {modifiedMessage.decode()}')
        print(f'RTT: {rtt} seconds\n')

    except timeout:
        # 요청 시간 초과 처리
        print('Request timed out\n')

# 소켓 닫기
clientSocket.close()
