"""Build the offline edition and its WordPress page from named public works."""
from html import escape
from pathlib import Path

root = Path(__file__).resolve().parents[1]
site = root / "site"
site.mkdir(exist_ok=True)
template = (root / "web/index.template.html").read_text()
for marker, path in (("seed", "publications/book-of-questions/seed-001.md"),
                     ("score", "works/art/a-score-for-two-margins.md")):
    title, *paras = (root / path).read_text().strip().split("\n\n")
    content = [f"<h3>{escape(title.removeprefix('# '))}</h3>"]
    for para in paras:
        if para.startswith("*") and para.endswith("*"):
            content.append(f"<small>{escape(para[1:-1])}</small>")
        else:
            content.append(f"<p>{escape(para)}</p>")
    template = template.replace(f"<!-- {marker} -->", "\n".join(content))
fronds = [f'<i class="frond-{i}"></i>' for i in range(24)]
template = template.replace("<!-- fronds -->", "".join(fronds))
css = (root / "web/garden.css").read_text() + "\n".join(
    f".frond-{i}{{--turn:{i * 12}deg}}" for i in range(24))
(site / "index.html").write_text(template)
(site / "garden.css").write_text(css)
theme = root / "wordpress/garden-leaf"
(theme / "garden.css").write_text(css)
edition = template.split("<!-- edition -->")[1].split("<!-- end edition -->")[0].strip()
(root / "wordpress/front-page.blocks.html").write_text(
    "<!-- wp:html -->\n" + edition + "\n<!-- /wp:html -->\n")
