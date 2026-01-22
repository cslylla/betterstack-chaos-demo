from dotenv import load_dotenv
import os
import random
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import time
from posthog import Posthog

load_dotenv()
app = FastAPI(title="Chaos Demo")

FAIL_RATE = float(os.getenv("FAIL_RATE", "0.3"))  # 30% default

POSTHOG_API_KEY = os.getenv("POSTHOG_API_KEY", "")
POSTHOG_HOST = os.getenv("POSTHOG_HOST", "https://app.posthog.com")

posthog = None
if POSTHOG_API_KEY:
    posthog = Posthog(project_api_key=POSTHOG_API_KEY, host=POSTHOG_HOST)

if posthog:
    posthog.capture(
        distinct_id="test",
        event="posthog_test_event"
    )

@app.get("/health")
async def health():
    if posthog:
        posthog.capture(
            distinct_id="chaos-demo-service",
            event="health_check_called",
        )
    return {"ok": True}

@app.get("/chaos", response_class=PlainTextResponse)
def chaos():
    start = time.time()

    # Intermittent failure (simulate flaky dependency)
    failed = random.random() < FAIL_RATE

    if posthog:
        posthog.capture(
            distinct_id="chaos-demo-service",
            event="chaos_endpoint_called",
            properties={
                "failed": failed,
                "fail_rate": FAIL_RATE,
                "latency_ms": int((time.time() - start) * 1000),
            },
        )

    if failed:
        return PlainTextResponse("Simulated failure", status_code=500)

    return PlainTextResponse("OK", status_code=200)