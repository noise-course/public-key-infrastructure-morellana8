from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

# Define address and port
server_address = ('localhost', 4443)  # HTTPS often uses 443, but you need root for that

# Create basic HTTP server
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

# Wrap the socket with SSL
httpd.socket = ssl.wrap_socket(
    httpd.socket,
    certfile='server.pem',
    server_side=True
)

print("Serving on https://localhost:4443")
httpd.serve_forever()
