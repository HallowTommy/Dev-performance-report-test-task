from collections import defaultdict
from typing import List, Dict, Any
from .models import DeveloperRecord

def performance_report(records: List[DeveloperRecord]) -> List[Dict[str, Any]]:
    sums: dict[str, float] = defaultdict(float)
    counts: dict[str, int] = defaultdict(int)

    for r in records:
        sums[r.position] += r.performance
        counts[r.position] += 1

    rows: List[Dict[str, Any]] = []
    for pos, total in sums.items():
        avg = total / counts[pos]
        rows.append({"position": pos, "avg_performance": round(avg, 2)})

    # sort by avg_performance descending
    rows.sort(key=lambda x: x["avg_performance"], reverse=True)
    return rows

REPORTS = {
    "performance": performance_report,
}
