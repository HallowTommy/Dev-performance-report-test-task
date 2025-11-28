from dev_performance.main import main

def test_cli_integration(tmp_path, capsys):
    p = tmp_path / "t.csv"
    p.write_text("name,position,completed_tasks,performance,skills,team,experience_years\nA,Dev,1,4.1,,,1\n")
    exit_code = main(["--files", str(p), "--report", "performance"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Dev" in captured.out
