"""Pytest-tests voor de Student Grade Analyzer, per acceptatiecriterium."""

import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
GRADE_ANALYZER = REPO_ROOT / "src" / "grade_analyzer.py"

VOORBEELD = (
    "Aantal studenten: 3\n"
    "Gemiddelde score: 13.0\n"
    "\n"
    "Geslaagd:\n"
    "- Alice\n"
    "- Charlie\n"
    "\n"
    "Niet geslaagd:\n"
    "- Bob\n"
)


def schrijf_csv(tmp_path: Path, inhoud: str) -> Path:
    """Schrijf een CSV-bestand en geef het pad terug."""
    pad = tmp_path / "results.csv"
    pad.write_text(inhoud, encoding="utf-8")
    return pad


def voer_uit(csv_pad: Path) -> subprocess.CompletedProcess[str]:
    """Voer de tool uit en geef het resultaat terug."""
    if not GRADE_ANALYZER.is_file():
        pytest.fail(
            "src/grade_analyzer.py ontbreekt nog, fase 3 moet de module implementeren"
        )
    return subprocess.run(
        [sys.executable, str(GRADE_ANALYZER), str(csv_pad)],
        capture_output=True,
        text=True,
        check=False,
    )


def lijst_na_kop(output: str, kop: str) -> list[str]:
    """Geef de namen na de gegeven kop tot de witregel terug."""
    regels = output.splitlines()
    namen = []
    for regel in regels[regels.index(kop) + 1 :]:
        if not regel:
            break
        namen.append(regel.removeprefix("- "))
    return namen


def test_ac1_volledige_output_exact(tmp_path: Path) -> None:
    """AC-1: de volledige output is exact gelijk aan het voorbeeld."""
    pad = schrijf_csv(tmp_path, "name,score\nAlice,14\nBob,8\nCharlie,17\n")
    result = voer_uit(pad)
    assert result.stdout == VOORBEELD


def test_ac2_aantal_studenten(tmp_path: Path) -> None:
    """AC-2: de tool toont het aantal studenten."""
    pad = schrijf_csv(tmp_path, "name,score\nAlice,14\nBob,8\nCharlie,17\n")
    result = voer_uit(pad)
    assert "Aantal studenten: 3" in result.stdout


def test_ac3_gemiddelde_score(tmp_path: Path) -> None:
    """AC-3: de tool toont het gemiddelde 13.0."""
    pad = schrijf_csv(tmp_path, "name,score\nAlice,14\nBob,8\nCharlie,17\n")
    result = voer_uit(pad)
    assert "Gemiddelde score: 13.0" in result.stdout


def test_ac4_afronding_halve_waarde(tmp_path: Path) -> None:
    """AC-4: een gemiddelde van 3.25 wordt getoond als 3.3."""
    pad = schrijf_csv(tmp_path, "name,score\nA,3\nB,3\nC,3\nD,4\n")
    result = voer_uit(pad)
    assert "Gemiddelde score: 3.3" in result.stdout


def test_ac5_lijst_geslaagd(tmp_path: Path) -> None:
    """AC-5: de lijst geslaagden klopt en volgt de CSV-volgorde."""
    pad = schrijf_csv(tmp_path, "name,score\nAlice,14\nBob,8\nCharlie,17\n")
    result = voer_uit(pad)
    assert lijst_na_kop(result.stdout, "Geslaagd:") == ["Alice", "Charlie"]


def test_ac6_lijst_niet_geslaagd(tmp_path: Path) -> None:
    """AC-6: de lijst niet geslaagden klopt en volgt de CSV-volgorde."""
    pad = schrijf_csv(tmp_path, "name,score\nAlice,14\nBob,8\nCharlie,17\n")
    result = voer_uit(pad)
    assert lijst_na_kop(result.stdout, "Niet geslaagd:") == ["Bob"]


def test_ac7_score_10_is_geslaagd(tmp_path: Path) -> None:
    """AC-7: een score van 10 staat in de lijst geslaagden."""
    pad = schrijf_csv(tmp_path, "name,score\nBob,10\n")
    result = voer_uit(pad)
    assert lijst_na_kop(result.stdout, "Geslaagd:") == ["Bob"]


def test_ac8_score_0_is_niet_geslaagd_zonder_foutmelding(tmp_path: Path) -> None:
    """AC-8: een score van 0 staat in niet geslaagden, zonder foutmelding."""
    pad = schrijf_csv(tmp_path, "name,score\nErik,0\n")
    result = voer_uit(pad)
    assert lijst_na_kop(result.stdout, "Niet geslaagd:") == ["Erik"]
    assert result.stderr == ""


def test_ac9_score_20_is_geslaagd(tmp_path: Path) -> None:
    """AC-9: de maximumscore 20 staat in de lijst geslaagden."""
    pad = schrijf_csv(tmp_path, "name,score\nFatima,20\n")
    result = voer_uit(pad)
    assert lijst_na_kop(result.stdout, "Geslaagd:") == ["Fatima"]


def test_ac10_score_boven_maximum_fout(tmp_path: Path) -> None:
    """AC-10: een score boven 20 geeft een foutmelding en exit code ongelijk aan 0."""
    pad = schrijf_csv(tmp_path, "name,score\nWout,21\n")
    result = voer_uit(pad)
    assert result.returncode != 0
    assert "Wout" in result.stderr
    assert "21" in result.stderr


@pytest.mark.parametrize("waarde", ["abc", "-3"])
def test_ac11_ongeldige_score_fout(tmp_path: Path, waarde: str) -> None:
    """AC-11: een ongeldige score geeft een foutmelding met rij en waarde."""
    pad = schrijf_csv(tmp_path, f"name,score\nWout,{waarde}\n")
    result = voer_uit(pad)
    assert result.returncode != 0
    assert "Wout" in result.stderr
    assert waarde in result.stderr


def test_ac11_leeg_veld_fout(tmp_path: Path) -> None:
    """AC-11: een leeg scoreveld geeft een foutmelding en exit code ongelijk aan 0."""
    pad = schrijf_csv(tmp_path, "name,score\nWout,\n")
    result = voer_uit(pad)
    assert result.returncode != 0
    assert result.stderr != ""


def test_ac12_lege_csv_fout(tmp_path: Path) -> None:
    """AC-12: een CSV met alleen een kopregel geeft een foutmelding."""
    pad = schrijf_csv(tmp_path, "name,score\n")
    result = voer_uit(pad)
    assert result.returncode != 0
    assert result.stderr != ""


def test_ac13_ontbrekende_kolom_fout(tmp_path: Path) -> None:
    """AC-13: een bestand zonder scorekolom geeft een foutmelding."""
    pad = schrijf_csv(tmp_path, "name\nAlice\n")
    result = voer_uit(pad)
    assert result.returncode != 0
    assert result.stderr != ""


def test_ac14_onbestaand_bestand_fout(tmp_path: Path) -> None:
    """AC-14: een onbestaand bestand geeft een foutmelding."""
    pad = tmp_path / "bestaat_niet.csv"
    result = voer_uit(pad)
    assert result.returncode != 0
    assert result.stderr != ""