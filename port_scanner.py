import socket

target = input("Masukkan IP target: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print(f"\nScanning {target} dari port {start_port} sampai {end_port}...\n")

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port}")

    s.close()

print("\nScan selesai.")
