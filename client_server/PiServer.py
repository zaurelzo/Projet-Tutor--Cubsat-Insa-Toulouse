import pickle
import socket
import sys
from time import sleep

UART = 0
SPI = 1
I2C = 2

class Server:

    def __init__(self, name, port):
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server_address = (name, port)

    def listen(self):
        print 'starting up on %s port %s' % self.server_address
        self.sock.bind(self.server_address)
        self.sock.listen(1)

        while True:
            print 'waiting for a connection'
            connection, client_address = self.sock.accept()
            try:
                print 'client connected:', client_address
                while True:
                    data = connection.recv(4096)
                    (packet, protocol, ip) = pickle.loads(data)
                    print 'received "%s %d %s"' % (packet, protocol, ip)
                    if data:
                        #connection.sendall(data)
                        pass
                    else:
                        break
            except socket.error:
                print >>sys.stderr, "Connection broke"
            except EOFError:
                pass #TODO this is not the most beautiful way to do it. Normaly the stream should be closed before pickle
            finally:
                connection.close()