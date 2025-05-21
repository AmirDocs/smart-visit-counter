import time

timer_state = {"start_time": None}

def start_timer():
    timer_state["start_time"] = time.time()

def get_timer_status():
    if timer_state["start_time"] is None:
        return {"status": "Timer not started"}
    elapsed = time.time() - timer_state["start_time"]
    return {"status": "running", "elapsed_seconds": round(elapsed, 2)}
