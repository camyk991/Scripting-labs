import socket

def scan_ports(ip_address, port_range):
    open_ports = []

    start_port, end_port = port_range.split('-')
    start_port = int(start_port)
    end_port = int(end_port)


    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  

        try:
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                print(f"Port {port} is open")
                open_ports.append(port)
            sock.close()
        except socket.error:
            print(f"Couldn't connect to port {port}")
            pass

    print(f"Scan completed. Open ports: {open_ports}")


if __name__ == "__main__":
    ip = input("Enter the IP address to scan: ")
    port_range = input("Enter the port range (e.g., 1-1000): ")
    scan_ports(ip, port_range)

