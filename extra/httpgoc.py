import http.server as htpsrvr
import socketserver

def run_http_server():
    PORT = 8080
    handler = htpsrvr.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
      httpd.serve_forever()
    print(f"Serving HTTP at {PORT} \n")
