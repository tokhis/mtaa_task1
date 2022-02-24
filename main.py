import sipfullproxy

import socket
import logging
import time
import sys


def main():
    print('subscribe to technoblade')
    logging.basicConfig(filename='communication.log', format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%H:%M:%S', level=logging.INFO)
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))

    hostname = socket.gethostname()
    logging.info(hostname)

    ipaddress = socket.gethostbyname(hostname)
    if ipaddress == '127.0.0.1':
        ipaddress = sys.argv[1]
    logging.info(ipaddress)

    server = sipfullproxy.socketserver.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
