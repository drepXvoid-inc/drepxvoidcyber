import socket

target = "127.0.0.1"

print("Scanning localhost...")

for port in range(1, 200):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)
    
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port} terbuka")
    
    s.close()