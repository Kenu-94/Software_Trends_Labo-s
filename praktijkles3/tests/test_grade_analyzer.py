"""Tests voor de Student Grade Analyzer."""

import csv
import sys
import subprocess
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from grade_analyzer import GradeAnalyzer


def _maak_csv(rijen, tmp_path, naam="test.csv"):
    """Maak tijdelijk CSV-bestand (eerste rij = header)."""
    pad = tmp_path / naam
    with open(pad, "w", newline="") as f:
        csv.writer(f).writerows(rijen)
    return pad


def _draai_analyzer(csv_pad):
    """Roep grade_analyzer.py aan als script."""
    script = Path(__file__).resolve().parent.parent / "src" / "grade_analyzer.py"
    return subprocess.run([sys.executable, str(script), str(csv_pad)],
                          capture_output=True, text=True)


class TestGradeAnalyzer:
    """Tests voor de GradeAnalyzer-klasse."""

    def test_ac1_drie_studenten(self, tmp_path):
        """AC1: Normaal bestand met 3 studenten."""
        p = _maak_csv([["name", "score"], ["Alice", "14"],
                       ["Bob", "8"], ["Charlie", "17"]], tmp_path)
        r = GradeAnalyzer(p).analyseer()
        assert r["aantal"] == 3
        assert r["gemiddelde"] == 13.0
        assert r["geslaagd"] == ["Alice", "Charlie"]
        assert r["niet_geslaagd"] == ["Bob"]

    def test_ac2_grote_dataset(self):
        """AC2: Makkelijke dataset met 60 studenten."""
        p = (Path(__file__).resolve().parent.parent /
             "data" / "makkelijk" / "results_v3.csv")
        r = GradeAnalyzer(p).analyseer()
        assert r["aantal"] > 0
        assert isinstance(r["gemiddelde"], float)

    def test_ac3_leeg_bestand(self, tmp_path):
        """AC3: Leeg bestand geeft fout."""
        p = tmp_path / "leeg.csv"
        p.write_text("")
        proc = _draai_analyzer(p)
        assert proc.returncode != 0

    def test_ac4_alleen_header(self, tmp_path):
        """AC4: Enkel header, 0 studenten."""
        r = GradeAnalyzer(_maak_csv([["name", "score"]], tmp_path)).analyseer()
        assert r["aantal"] == 0
        assert r["gemiddelde"] is None

    def test_ac5_lege_score(self, tmp_path):
        """EC4: Lege score overgeslagen."""
        r = GradeAnalyzer(_maak_csv([["name", "score"],
                                     ["A", ""], ["B", "12"]], tmp_path)).analyseer()
        assert r["aantal"] == 1

    def test_ac5_absent(self, tmp_path):
        """EC5: Absent overgeslagen."""
        r = GradeAnalyzer(_maak_csv([["name", "score"],
                                     ["A", "absent"], ["B", "12"]], tmp_path)).analyseer()
        assert r["aantal"] == 1

    def test_ac5_na(self, tmp_path):
        """EC5: n/a overgeslagen."""
        r = GradeAnalyzer(_maak_csv([["name", "score"],
                                     ["A", "n/a"], ["B", "12"]], tmp_path)).analyseer()
        assert r["aantal"] == 1

    def test_ac6_score_nul(self, tmp_path):
        """AC6: Score 0 geldig, niet geslaagd."""
        r = GradeAnalyzer(_maak_csv([["name", "score"], ["A", "0"]],
                                    tmp_path)).analyseer()
        assert r["aantal"] == 1
        assert r["gemiddelde"] == 0.0
        assert r["niet_geslaagd"] == ["A"]

    def test_ac7_score_tien(self, tmp_path):
        """AC7: Score 10 geslaagd (grens)."""
        r = GradeAnalyzer(_maak_csv([["name", "score"], ["A", "10"]],
                                    tmp_path)).analyseer()
        assert r["geslaagd"] == ["A"]

    def test_ac8_score_twintig(self, tmp_path):
        """AC8: Score 20 geslaagd."""
        r = GradeAnalyzer(_maak_csv([["name", "score"], ["A", "20"]],
                                    tmp_path)).analyseer()
        assert r["geslaagd"] == ["A"]

    def test_ac9_bestand_niet_bestaat(self):
        """AC9: Niet-bestaand bestand."""
        proc = _draai_analyzer(Path("/nep/bestaat/niet.csv"))
        assert proc.returncode != 0

    def test_ac10_geen_argument(self):
        """AC10: Zonder argument."""
        script = (Path(__file__).resolve().parent.parent /
                  "src" / "grade_analyzer.py")
        proc = subprocess.run([sys.executable, str(script)],
                              capture_output=True, text=True)
        assert proc.returncode != 0

    def test_ongeldige_negatief(self, tmp_path):
        """EC6: Negatieve score overgeslagen."""
        r = GradeAnalyzer(_maak_csv([["name", "score"],
                                     ["A", "-5"], ["B", "12"]], tmp_path)).analyseer()
        assert r["aantal"] == 1

    def test_ongeldige_boven_20(self, tmp_path):
        """EC7: Score >20 overgeslagen."""
        r = GradeAnalyzer(_maak_csv([["name", "score"],
                                     ["A", "25"], ["B", "12"]], tmp_path)).analyseer()
        assert r["aantal"] == 1

    def test_gemiddelde_afronding(self, tmp_path):
        """Gemiddelde afgerond op 1 decimaal."""
        r = GradeAnalyzer(_maak_csv([["name", "score"],
                                     ["A", "10"], ["B", "13"], ["C", "17"]],
                                    tmp_path)).analyseer()
        assert r["gemiddelde"] == 13.3

    def test_cli_output_tekst(self, tmp_path):
        """CLI toont alle secties."""
        p = _maak_csv([["name", "score"], ["Alice", "14"],
                       ["Bob", "8"]], tmp_path)
        proc = _draai_analyzer(p)
        assert proc.returncode == 0
        assert "Aantal studenten: 2" in proc.stdout
        assert "Geslaagd:" in proc.stdout
        assert "Niet geslaagd:" in proc.stdout