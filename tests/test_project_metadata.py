import tomllib
from pathlib import Path
import unittest


class ProjectMetadataTests(unittest.TestCase):
    def test_package_identity_matches_tresorbana(self):
        pyproject = Path(__file__).resolve().parents[1] / "pyproject.toml"
        with pyproject.open("rb") as f:
            data = tomllib.load(f)

        self.assertEqual(data["project"]["name"], "tresor-calcutils-2026")
        self.assertEqual(data["project"]["authors"][0]["name"], "tresorbana")
        self.assertEqual(data["project"]["authors"][0]["email"], "tresorbana77@gmail.com")
        self.assertIn("tresor-calcutils-2026", data["project"]["urls"]["Homepage"])


if __name__ == "__main__":
    unittest.main()
