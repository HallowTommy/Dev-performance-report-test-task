from dev_performance.loader import load_from_files

def test_load_from_files(tmp_path):
    p = tmp_path / "t.csv"
    p.write_text("name,position,completed_tasks,performance,skills,team,experience_years\nA,Dev,1,4.5,,T,1\n")
    records = load_from_files([str(p)])
    assert len(records) == 1
    assert records[0].position == "Dev"
    assert abs(records[0].performance - 4.5) < 1e-6
