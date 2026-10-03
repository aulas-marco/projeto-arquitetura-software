"""O tempo de aula e so de apresentacao conceitual, e o exercicio e atividade fora da sala."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MODULES = sorted(p for p in DOCS.glob("modulo-*") if p.is_dir())
MARKER = "fora do horário de aula"


class ExercisesOutsideClassTest(unittest.TestCase):
    def test_schedule_gives_class_time_only_to_concepts(self):
        text = (DOCS / "cronograma.md").read_text(encoding="utf-8")
        self.assertNotIn("quinze de exercício", text)
        self.assertIn("blocos de apresentação conceitual somam 130 minutos", text)
        self.assertIn(MARKER, text)

    def test_home_page_states_the_rule(self):
        self.assertIn(MARKER, (DOCS / "index.md").read_text(encoding="utf-8"))

    def test_module_indexes_state_the_rule(self):
        for module in MODULES:
            with self.subTest(module=module.name):
                self.assertIn(MARKER, (module / "index.md").read_text(encoding="utf-8"))

    def test_time_grids_have_no_exercise_minutes(self):
        for module in MODULES:
            text = (module / "index.md").read_text(encoding="utf-8")
            with self.subTest(module=module.name):
                self.assertNotIn("Exercício (min)", text)
                if "## Grade de tempo" not in text:
                    continue
                if "| Horário | Atividade |" in text:
                    # Grade com Kahoot, adotada a partir da Aula 3: 130 minutos de blocos.
                    rows = re.findall(r"^\| [\dh–]+ \| Bloco [1-4],.*\| (\d+) \|\s*$", text, re.MULTILINE)
                    self.assertEqual(4, len(rows))
                    self.assertEqual(130, sum(int(r) for r in rows))
                    self.assertEqual(3, len(re.findall(r"^\| [\dh–]+ \| Kahoot", text, re.MULTILINE)))
                else:
                    # Grade das Aulas 1 e 2, ministradas antes da mudança.
                    rows = re.findall(r"^\| [1-4] \|.*\| (\d+) \|\s*$", text, re.MULTILINE)
                    self.assertEqual(["40", "40", "40", "40"], rows)

    def test_exercise_sections_do_not_repeat_the_rule(self):
        """A regra fica no indice de cada aula, e o enunciado vai direto ao caso."""
        for page, section in exercise_sections():
            with self.subTest(page=page.name):
                self.assertNotIn(MARKER, section)
                self.assertNotIn("Este exercício é realizado", section)

    def test_exercises_are_split_into_self_contained_items(self):
        for page, section in exercise_sections():
            items = re.findall(r"(?m)^### Item \d+: \S", section)
            with self.subTest(page=page.name):
                self.assertGreaterEqual(len(items), 2)

    def test_exercises_bring_a_visual_artifact(self):
        for page, section in exercise_sections():
            visuals = section.count("```mermaid") + section.count("{ .module-diagram }")
            with self.subTest(page=page.name):
                self.assertGreaterEqual(visuals, 1)


def exercise_sections():
    for page in sorted(DOCS.glob("modulo-*/bloco-*.md")):
        text = page.read_text(encoding="utf-8")
        match = re.search(r"^## Exercício \d+\s*$", text, re.MULTILINE)
        if match is None:
            continue
        rest = text[match.end():]
        yield page, rest[: re.search(r"^## ", rest, re.MULTILINE).start()]

if __name__ == "__main__":
    unittest.main()
