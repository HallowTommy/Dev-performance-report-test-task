from typing import List, Dict
from tabulate import tabulate

def render_table(rows: List[Dict], headers):
    table = [[i + 1] + [row[h] for h in headers] for i, row in enumerate(rows)]
    print(tabulate(table, headers=["#"] + headers, tablefmt="github"))
