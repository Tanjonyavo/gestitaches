import json
import sqlite3
from contextlib import closing
from datetime import date
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs


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
                    "SELECT title, description, due_date, completed FROM tasks ORDER BY id"
                )
                body = json.dumps([dict(row) for row in rows]).encode("utf-8")
            self.send_content(body, "application/json; charset=utf-8")
            return
        if self.path == "/":
            self.send_content((FRONTEND / "index.html").read_bytes(), "text/html; charset=utf-8")
            return
        self.send_error(404)

    def do_POST(self):
        if self.path != "/api/tasks":
            self.send_error(404)
            return
        if self.headers.get_content_type() != "application/x-www-form-urlencoded":
            self.send_error(415)
            return
        try:
            size = int(self.headers.get("Content-Length", "0"))
            if not 0 < size <= 65536:
                self.send_error(400, "Taille de formulaire invalide.")
                return
            fields = parse_qs(
                self.rfile.read(size).decode("utf-8"), keep_blank_values=True,
                errors="strict", max_num_fields=3,
            )
        except ValueError:
            self.send_error(400, "Formulaire invalide.")
            return

        title = fields.get("title", [""])[0].strip()
        description = fields.get("description", [""])[0].strip()
        due_date = fields.get("due_date", [""])[0]
        if not title:
            self.send_error(400, "Le titre est obligatoire.")
            return
        if len(title) > 120 or len(description) > 4000:
            self.send_error(400, "Le titre ou la description est trop long.")
            return
        if due_date:
            try:
                if date.fromisoformat(due_date).isoformat() != due_date:
                    raise ValueError
            except ValueError:
                self.send_error(400, "La date doit être valide (AAAA-MM-JJ).")
                return
        with closing(sqlite3.connect(DATABASE)) as connection, connection:
            connection.execute(
                "INSERT INTO tasks (title, description, due_date) VALUES (?, ?, ?)",
                (title, description, due_date),
            )
        self.send_response(303)
        self.send_header("Location", "/")
        self.end_headers()


if __name__ == "__main__":
    initialize_database()
    with HTTPServer(("127.0.0.1", 8000), Handler) as server:
        print("GestiTâches : http://127.0.0.1:8000", flush=True)
        server.serve_forever()
