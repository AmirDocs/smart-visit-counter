from app.services.visit_counter import record_visit

def test_record_visit():
    ip = "127.0.0.1"
    count1 = record_visit(ip)
    count2 = record_visit(ip)
    assert count1 == 1
    assert count2 == 2
