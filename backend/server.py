import json
import sqlite3
from contextlib import closing
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FRONTEND = ROOT / "frontend"
DATABASE = ROOT / "backend" / "tasks.sqlite3"


def initialize_database():
    with closing(sqlite3.connect(DATABASE)) as connection, connection:
        connection.execute(
            """CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                due_date TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0
            )"""
        )


class Handler(BaseHTTPRequestHandler):
    def send_content(self, body, content_type):
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/api/tasks":
            with closing(sqlite3.connect(DATABASE)) as connection:
                connection.row_factory = sqlite3.Row
                rows = connection.execute(
                    "SELECT title, description, due_date, completed "
                    "FROM tasks ORDER BY id"
                )
                body = json.dumps([dict(row) for row in rows]).encode("utf-8")
            self.send_content(body, "application/json; charset=utf-8")
            return
        if self.path == "/":
            body = (FRONTEND / "index.html").read_bytes()
            self.send_content(body, "text/html; charset=utf-8")
            return
        self.send_error(404)


if __name__ == "__main__":
    initialize_database()
    with HTTPServer(("127.0.0.1", 8000), Handler) as server:
        print("GestiTâches : http://127.0.0.1:8000", flush=True)
        server.serve_forever()
