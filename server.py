from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from os import path

# Путь к HTML-файлу
file_path = "templates/index.html"


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Проверяем путь запроса
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            # Открываем и отправляем HTML-файл
            with open(file_path, "rb") as file:
                self.wfile.write(file.read())
        else:
            self.send_error(404, "File Not Found")


# Функция запуска сервера
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()


# Запускаем сервер на порту 8000
if __name__ == "__main__":
    run()
