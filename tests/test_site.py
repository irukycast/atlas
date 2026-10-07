"""Offline checks for the actual GitHub Pages tree, including /atlas/ links."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = "https://irukycast.github.io/atlas/"


class Links(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.links, self.ids = [], set()
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        for key in ("href", "src"):
            if key in attrs:
                self.links.append(attrs[key])


class SiteTests(unittest.TestCase):
    def test_data_deletion_exists_and_identifies_operator(self):
        source = (ROOT / "data-deletion.html").read_text(encoding="utf-8")
        self.assertIn("<h1>Eliminación de datos</h1>", source)
        self.assertIn("Juan Manuel Castro", source)
        for term in ("obligaciones legales", "seguridad", "prevención de fraude", "cuenta o conversación"):
            self.assertIn(term, source)

    def test_contact_matches_current_landing(self):
        email = re.search(r'CONTACT_EMAIL = "([^"]+)"', (ROOT / "script.js").read_text(encoding="utf-8"))[1]
        for name in ("index.html", "privacy.html", "terms.html", "data-deletion.html"):
            source = (ROOT / name).read_text(encoding="utf-8")
            self.assertEqual(set(re.findall(r'mailto:([^"?]+)', source)), {email})

    def test_visible_footer_links(self):
        for name in ("index.html", "privacy.html", "terms.html"):
            footer = (ROOT / name).read_text(encoding="utf-8").split("<footer", 1)[1]
            self.assertIn('<a href="data-deletion.html">Eliminación de datos</a>', footer)

    def test_all_internal_assets_pages_and_fragments_exist_under_atlas(self):
        for page in ROOT.glob("*.html"):
            for link in Links(page.read_text(encoding="utf-8")).links:
                url = urlsplit(urljoin(PUBLIC + page.name, link))
                if url.scheme in ("mailto", "data") or url.hostname != "irukycast.github.io":
                    continue
                self.assertTrue(url.path.startswith("/atlas/"), (page, link))
                target = ROOT / unquote(url.path.removeprefix("/atlas/"))
                self.assertTrue(target.is_file(), (page, link))
                if url.fragment:
                    self.assertIn(url.fragment, Links(target.read_text(encoding="utf-8")).ids)

    def test_no_placeholders_and_shared_legal_styles(self):
        for page in ROOT.glob("*.html"):
            source = page.read_text(encoding="utf-8")
            for forbidden in ("REEMPLAZAR_EMAIL", "localhost", "facebook.com", "lorem ipsum"):
                self.assertNotIn(forbidden.lower(), source.lower())
        source = (ROOT / "data-deletion.html").read_text(encoding="utf-8")
        self.assertIn('href="styles.css"', source)
        self.assertIn('class="container legal-content"', source)


if __name__ == "__main__":
    unittest.main()
