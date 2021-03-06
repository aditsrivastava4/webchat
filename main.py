from jinja2 import Template
from os import curdir, sep
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import requests as rts
from urllib.parse import unquote, parse_qs
import threading
from socketserver import ThreadingMixIn
import storeMsg
import decrypt


class ThreadHTTPServer(ThreadingMixIn, HTTPServer):
    "This is an HTTPServer that supports thread-based concurrency."

class ChatHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/":
            self.path="/index.html"

        try:
            #Check the file extension required and
            #set the right mime type
            sendReply = False
            if self.path.endswith(".html"):
                mimetype='text/html; charset=utf-8'
                sendReply = True
            if self.path.endswith(".jpg"):
                mimetype='image/jpg; charset=utf-8'
                sendReply = True
            if self.path.endswith(".gif"):
                mimetype='image/gif; charset=utf-8'
                sendReply = True
            if self.path.endswith(".js"):
                mimetype='application/javascript; charset=utf-8'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype='text/css; charset=utf-8'
                sendReply = True

            if sendReply == True:
                #Open the static file requested and send it
                msgData = storeMsg.getData()
                if(msgData == ()):
                	msgData = 'Empty'


                f = open(curdir + sep + self.path) 
                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.end_headers()
                template = Template(f.read())
                self.wfile.write(template.render(data=msgData).encode())
                f.close()
            return


        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

    def do_POST(self):
        length = int(self.headers.get('Content-length', 0))
        body = self.rfile.read(length).decode()
        params = parse_qs(body)
        try:
            a_data = params['Textarea'][0]
            if decrypt.confirm(a_data):
                #if the passphrase is correct drop the table
                storeMsg.dropTable()
            else:
                storeMsg.inputData(a_data)
        except:
            pass

        try:
            #Check the file extension required and
            #set the right mime type
            self.send_response(302)
            self.path = "/"
            self.send_header('Location', self.path)
            self.end_headers()

        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type','text/html; charset=utf-8')
        self.end_headers()



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    server_address = ('', port)
    httpd = ThreadHTTPServer(server_address, ChatHandler)
    print('Server runing at http://localhost:{}/'.format(port))
    httpd.serve_forever()
