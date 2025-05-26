from app.services import timer
import time

def test_start_timer_sets_time():
    timer.start_timer()
    assert timer.timer_state["start_time"] is not None

def test_get_timer_status_running():
    timer.start_timer()
    time.sleep(0.1)  # short wait to simulate time passing
    status = timer.get_timer_status()
    assert status["status"] == "running"
    assert status["elapsed_seconds"] >= 0.1

def test_get_timer_status_not_started():
    timer.timer_state["start_time"] = None  # manually reset
    status = timer.get_timer_status()
    assert status == {"status": "Timer not started"}
