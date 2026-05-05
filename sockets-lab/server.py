import socket

HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 65432      

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Allow immediate reuse of the port after the server stops.
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    print(f"[SERVER] Listening on {HOST}:{PORT}")
    
    try:
        while True:  # accept multiple clients one after another
            conn, addr = s.accept()
            with conn:
                print(f"[SERVER] Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        print(f"[SERVER] {addr} disconnected")
                        break
                    print(f"[SERVER] Received: {data.decode()}")
                    conn.sendall(data)  # echo back
    except KeyboardInterrupt:
        print("\n[SERVER] Shutting down (Ctrl+C).")