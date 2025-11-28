from dev_performance.reports import performance_report
from dev_performance.models import DeveloperRecord

def test_performance_report():
    recs = [
        DeveloperRecord("A","Dev",1,4.0,"","",1),
        DeveloperRecord("B","Dev",2,5.0,"","",2),
        DeveloperRecord("C","QA",1,3.5,"","",1),
    ]
    rows = performance_report(recs)
    assert rows[0]["position"] == "Dev"
    assert rows[0]["avg_performance"] == 4.5
