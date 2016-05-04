import Client
import PiServer

client = Client.Client('localhost', 10003)

client.send_message("packet", PiServer.SPI, 'localhost')

client.close_socket()
