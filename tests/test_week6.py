import runpy
from pathlib import Path

script = Path(__file__).resolve().parents[1] / "record_processor.py"
processor = runpy.run_path(str(script))
process_records = processor["process_records"]


def test_pending_total():
    total, flagged, high_value = process_records(processor["records"])
    assert len(processor["records"]) == 5
    assert total == 3939
    assert len(flagged) == 2
    assert len(high_value) == 1


def test_review_boundary():
    items = [
        {"amount": 1000, "status": "Pending"},
        {"amount": 1001, "status": "Pending"},
    ]
    _, flagged, _ = process_records(items)
    assert flagged == [items[1]]


def test_high_value_boundary():
    items = [
        {"amount": 2000, "status": "Pending"},
        {"amount": 2001, "status": "Pending"},
    ]
    _, flagged, high_value = process_records(items)
    assert high_value == [items[1]]
    assert len(flagged) == 2


def test_approved_excluded():
    items = [{"amount": 3500, "status": "Approved"}]
    assert process_records(items) == (0, [], [])


def test_summary_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    processor["main"]()
    summary = tmp_path / "data" / "week6_summary.txt"
    expected = "Pending total: $3,939.00\nNeeds review: 2\nHigh-value: 1\n"
    assert summary.read_text(encoding="utf-8") == expected
