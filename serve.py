import http.server
import os

PORT = 3000
DIR = os.path.dirname(os.path.abspath(__file__))

os.chdir(DIR)

handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(("", PORT), handler)
print(f"Serving {DIR} on port {PORT}")
httpd.serve_forever()
