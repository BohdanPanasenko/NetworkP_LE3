import socket

HOST = 'localhost'
PORT = 65432

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("[CLIENT] Connected to server.")
        while True:
            message = input("Enter message (or 'exit'): ")
            if message.lower() == 'exit':
                break
            s.sendall(message.encode())
            data = s.recv(1024)
            if not data:
                print("[CLIENT] Server closed the connection.")
                break
            print(f"[CLIENT] Received from server: {data.decode()}")
except ConnectionRefusedError:
    print("[CLIENT] Could not connect. Is the server running?")
except KeyboardInterrupt:
    print("\n[CLIENT] Aborted by user.")