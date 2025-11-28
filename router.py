from datetime import datetime
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse
from core.responses import send_404
class StudentRouter(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlparse(self.path).path
        

        # if path in ("/", "/index.html"):
        #     return serve_html(self) 

        # if path.startswith("/static/"):
        #     return serve_static(self)

        # if path == "/api/students":
        #     return get_all_students(self)

        # if path.startswith("/api/students/"):
        #     student_id = int(path.split("/")[-1])
        #     return get_student(self, student_id)
        

        return send_404(self)