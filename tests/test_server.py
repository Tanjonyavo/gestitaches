import json
import sqlite3
import unittest
from contextlib import closing
from http.client import HTTPResponse
from io import BytesIO
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from backend import server


class InMemorySocket:
    def __init__(self, incoming):
        self.incoming = incoming
        self.outgoing = bytearray()

    def makefile(self, *_args):
        return BytesIO(self.incoming)

    def sendall(self, data):
        self.outgoing.extend(data)


class ServerTests(unittest.TestCase):
    def setUp(self):
        scratch = TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.database = Path(scratch.name) / "tasks.sqlite3"
        database_patch = patch.object(server, "DATABASE", self.database)
        database_patch.start()
        self.addCleanup(database_patch.stop)
        server.initialize_database()

    def get(self, path):
        request = f"GET {path} HTTP/1.0\r\n\r\n".encode("ascii")
        transport = InMemorySocket(request)
        with patch.object(server.Handler, "log_message"):
            server.Handler(transport, ("127.0.0.1", 12345), None)
        with closing(HTTPResponse(InMemorySocket(transport.outgoing))) as response:
            response.begin()
            return response.status, response.read()

    def test_home_serves_the_frontend(self):
        status, body = self.get("/")
        self.assertEqual(status, 200)
        self.assertIn(b"<title>GestiT", body)

    def test_empty_database_returns_an_empty_list(self):
        status, body = self.get("/api/tasks")
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(body), [])

    def test_list_returns_a_saved_task(self):
        with closing(sqlite3.connect(self.database)) as database, database:
            database.execute(
                "INSERT INTO tasks (title, description, due_date) VALUES (?, ?, ?)",
                ("Relire le TD", "Vérifier les critères", "2026-11-18"),
            )
        status, body = self.get("/api/tasks")
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(body), [{
            "title": "Relire le TD",
            "description": "Vérifier les critères",
            "due_date": "2026-11-18",
            "completed": 0,
        }])
