import csv
from pathlib import Path
from typing import Iterable, List
from .models import DeveloperRecord


def load_from_files(paths: Iterable[str]) -> List[DeveloperRecord]:
    records: List[DeveloperRecord] = []
    for p in paths:
        path = Path(p)
        if not path.is_file():
            raise FileNotFoundError(f"File not found: {path}")
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # assume CSV is valid per spec; convert types
                records.append(
                    DeveloperRecord(
                        name=row["name"],
                        position=row["position"],
                        completed_tasks=int(row["completed_tasks"]),
                        performance=float(row["performance"]),
                        skills=row.get("skills", ""),
                        team=row.get("team", ""),
                        experience_years=int(row.get("experience_years", 0)),
                    )
                )
    return records
