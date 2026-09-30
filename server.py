from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class CustomHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="/root/workspace/steve-birthday", **kwargs)

if __name__ == '__main__':
    PORT = 8080
    server = HTTPServer(('0.0.0.0', PORT), CustomHandler)
    print(f"🎂 Site d'anniversaire de Steve avec galerie lancé sur le port {PORT}")
    print(f"🌐 Ouvre: http://localhost:{PORT}")
    server.serve_forever()
