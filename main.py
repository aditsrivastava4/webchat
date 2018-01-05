from jinja2 import Template
from os import curdir, sep
from http.server import HTTPServer, BaseHTTPRequestHandler
import test

class HelloHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','application/html; charset=utf-8')
		self.end_headers()
		self.wfile.write('hello world'.encode())

if __name__ == '__main__':
	port = 8008
	server_address = ('0.0.0.0', port)  # Serve on all addresses, port 8000.
	httpd = HTTPServer(server_address, HelloHandler)
	print('Server runing at http://localhost:{}/'.format(port))
	httpd.serve_forever()
