def add_cors_headers(handler):
    handler.send_header("access-control-allow-origin","*")
    handler.send_header("access-control-allow-methods","GET, POST, PUT, DELETE")
    handler.send_header("access-control-allow-headers","content-type")