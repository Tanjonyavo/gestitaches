from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dist" / "gestitaches.zip"


def build():
    frontend = ROOT / "frontend"
    assets = [
        file for file in frontend.iterdir()
        if file.suffix in (".html", ".css", ".js") and file.is_file()
    ]
    files = [ROOT / "backend" / "server.py", ROOT / "README.md", *assets]
    names = sorted(file.relative_to(ROOT).as_posix() for file in files)
    OUTPUT.parent.mkdir(exist_ok=True)

    with NamedTemporaryFile(dir=OUTPUT.parent, delete=False) as stream:
        temporary = Path(stream.name)
    try:
        with ZipFile(temporary, "w") as archive:
            for name in names:
                entry = ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
                entry.create_system = 3
                entry.external_attr = 0o100644 << 16
                content = (ROOT / name).read_text(encoding="utf-8")
                archive.writestr(entry, content.encode("utf-8"))
        temporary.replace(OUTPUT)
    finally:
        temporary.unlink(missing_ok=True)
    print(f"Artefact : {OUTPUT.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    build()
