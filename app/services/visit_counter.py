from datetime import datetime
from collections import defaultdict

visits = defaultdict(int)

def record_visit(ip: str) -> int:
    visits[ip] += 1
    return visits[ip]
