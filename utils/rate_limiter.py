from time import time
from fastapi import HTTPException

request_log = {}

def rate_limit(user):
    now = time()

    if user not in request_log:
        request_log[user] = []

    # Keep only last 60 sec requests
    request_log[user] = [t for t in request_log[user] if now - t < 60]

    if len(request_log[user]) >= 5:
        raise HTTPException(status_code=429, detail="Too many requests")

    request_log[user].append(now)