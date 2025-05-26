# tests functions

from app.services.timer import calculate_duration  
from app.services.visit_counter import increment_counter 

def test_calculate_duration():
    start_time = "2023-01-01T10:00:00"
    end_time = "2023-01-01T11:00:00"
    duration = calculate_duration(start_time, end_time)
    assert duration == 3600  # 1 hour in seconds

def test_increment_counter():
    counter = 0
    new_counter = increment_counter(counter)
    assert new_counter == 1
