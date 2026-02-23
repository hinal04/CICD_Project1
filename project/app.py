from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")

server = HTTPServer(("localhost", 8000), Handler)
print("Server running on port 8000...")
server.serve_forever()