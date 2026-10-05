"""Student Grade Analyzer — command line tool die een CSV met studentresultaten analyseert.

Usage:
    python grade_analyzer.py <pad_naar_csv>
"""

import argparse
import csv
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional


class GradeAnalyzer:
    """Analyseert een CSV-bestand met studentresultaten.

    Args:
        bestandspad: Pad naar het CSV-bestand.
    """

    def __init__(self, bestandspad: Path) -> None:
        """Initialiseer met het pad naar het CSV-bestand."""
        self.bestandspad = Path(bestandspad)
        self._data: List[Dict[str, str]] = []

    def _laad_csv(self) -> List[Dict[str, str]]:
        """Lees het CSV-bestand in en geef een lijst van dictionaries terug.

        Returns:
            Lijst met rijen als dictionaries.

        Raises:
            FileNotFoundError: Als het bestand niet bestaat.
            ValueError: Als het bestand leeg is of enkel een header bevat.
        """
        if not self.bestandspad.exists():
            raise FileNotFoundError(f"Bestand niet gevonden: {self.bestandspad}")

        with open(self.bestandspad, newline="") as f:
            reader = csv.DictReader(f)
            rijen = list(reader)

        if not rijen or (len(rijen) == 1 and all(v == "" for v in rijen[0].values())):
            raise ValueError("CSV-bestand bevat geen geldige gegevens.")

        if not reader.fieldnames or "name" not in reader.fieldnames or "score" not in reader.fieldnames:
            raise ValueError("CSV-bestand moet 'name' en 'score' kolommen bevatten.")

        return rijen

    def _is_geldige_score(self, waarde: str) -> Optional[float]:
        """Controleer of een score geldig is (numeriek, 0–20).

        Args:
            waarde: De ruwe score-waarde uit de CSV.

        Returns:
            De score als float als geldig, anders None.
        """
        if waarde is None or waarde.strip() == "":
            return None
        try:
            score = float(waarde)
        except (ValueError, TypeError):
            return None
        if score < 0 or score > 20:
            return None
        return score

    def analyseer(self) -> Dict[str, Any]:
        """Analyseer de studentresultaten.

        Returns:
            Dictionary met:
            - 'aantal': aantal studenten met geldige score
            - 'gemiddelde': rekenkundig gemiddelde (None als 0 geldige scores)
            - 'geslaagd': lijst van geslaagde studenten (score ≥ 10)
            - 'niet_geslaagd': lijst van niet-geslaagde studenten (score < 10)
        """
        self._data = self._laad_csv()

        geldig: List[Dict[str, Any]] = []
        for rij in self._data:
            score = self._is_geldige_score(rij.get("score", ""))
            if score is not None:
                geldig.append({"naam": rij["name"], "score": score})

        if not geldig:
            return {
                "aantal": 0,
                "gemiddelde": None,
                "geslaagd": [],
                "niet_geslaagd": [],
            }

        scores = [g["score"] for g in geldig]
        gemiddelde = round(sum(scores) / len(scores), 1)

        geslaagd = [g["naam"] for g in geldig if g["score"] >= 10]
        niet_geslaagd = [g["naam"] for g in geldig if g["score"] < 10]

        return {
            "aantal": len(geldig),
            "gemiddelde": gemiddelde,
            "geslaagd": geslaagd,
            "niet_geslaagd": niet_geslaagd,
        }


def toon_resultaat(resultaat: Dict[str, Any]) -> None:
    """Toon het analyse-resultaat op stdout.

    Args:
        resultaat: Dictionary zoals teruggegeven door GradeAnalyzer.analyseer().
    """
    if resultaat["aantal"] == 0:
        print("Aantal studenten: 0")
        print("Geen geldige scores om te verwerken.")
        return

    print(f"Aantal studenten: {resultaat['aantal']}")
    print(f"Gemiddelde score: {resultaat['gemiddelde']}")
    print()
    print("Geslaagd:")
    for naam in resultaat["geslaagd"]:
        print(f"- {naam}")
    print()
    print("Niet geslaagd:")
    for naam in resultaat["niet_geslaagd"]:
        print(f"- {naam}")


def main() -> None:
    """Command line entry point."""
    parser = argparse.ArgumentParser(description="Student Grade Analyzer")
    parser.add_argument("bestand", help="Pad naar CSV-bestand met studentresultaten")
    args = parser.parse_args()

    try:
        analyzer = GradeAnalyzer(Path(args.bestand))
        resultaat = analyzer.analyseer()
        toon_resultaat(resultaat)
        sys.exit(0)
    except FileNotFoundError as e:
        print(f"Fout: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Fout: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()