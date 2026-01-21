import os
import random
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI(title="Chaos Demo")

FAIL_RATE = float(os.getenv("FAIL_RATE", "0.3"))  # 30% default

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/chaos", response_class=PlainTextResponse)
def chaos():
    # Intermittent failure (simulate flaky dependency)
    if random.random() < FAIL_RATE:
        return PlainTextResponse("Simulated failure", status_code=500)
    return PlainTextResponse("OK", status_code=200)