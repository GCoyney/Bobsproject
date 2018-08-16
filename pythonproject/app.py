#!/usr/bin/python
import SimpleHTTPServer
import SocketServer

PORT = 9000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()

f=("log.txt", "a+")
for i in range(5):
	f.write("Appended" % (i+1))
f.close()
