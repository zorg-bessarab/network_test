import asyncio
from telnetlib import Telnet
import socket
from datetime import datetime

host = "172.19.11.140"
ports = [22, 25, 111, 162, 199, 5000, 5432, 7805, 9381, 15433]
ports.extend(range(20000,23001))


def test_with_socket(qp):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.01)
        sock.connect((host, qp))
        result = f'Port {qp} is ok'
    except socket.error as exc:
        result = f'Port {qp} {exc}'
    finally:
        sock.close()
        return result


# def test_with_telnet(ports_range):
#     for qp in ports_range:
#         try:
#             connection = Telnet(host, qp, 0.01)
#             print(f'Port {qp} is ok')
#         except socket.error as exc:
#             print(f'Port {qp} {exc}')
#         finally:
#             connection.close()


def main():
    start = datetime.now()
    with open('result.txt', "w") as r:
        for qp in ports:
            result = test_with_socket(qp)
            r.write(f'{result}\n')
        end = datetime.now()
        r.write(f'Completed in: {end - start} \n')
        r.close()


if __name__ == "__main__":
    main()
