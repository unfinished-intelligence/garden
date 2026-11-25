"""Build the private preview using only the explicitly listed inputs."""
from html import escape
from pathlib import Path
from shutil import copyfile

root = Path(__file__).resolve().parents[1]
seed = root / "publications/book-of-questions/seed-001.md"
heading, *paragraphs = seed.read_text(encoding="utf-8").strip().split("\n\n")
if not heading.startswith("# ") or not paragraphs:
    raise ValueError("The seed requires a heading and one or more paragraphs.")
article = "\n".join([f"<h3>{escape(heading[2:])}</h3>",
                     *(f"<p>{escape(p)}</p>" for p in paragraphs)])
template = (root / "web/index.template.html").read_text(encoding="utf-8")
if template.count("<!-- seed -->") != 1:
    raise ValueError("Expected one seed insertion point.")
site = root / "site"
site.mkdir(exist_ok=True)
(site / "index.html").write_text(template.replace("<!-- seed -->", article), encoding="utf-8")
copyfile(root / "web/garden.css", site / "garden.css")
