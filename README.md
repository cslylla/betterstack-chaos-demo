# Better Stack Chaos Demo 

## Monitoring & Incident Demo (Better Stack)

Tiny FastAPI service with:
- `GET /health` → always 200
- `GET /chaos` → intermittently 500 (simulates a flaky dependency)

Used to demonstrate Better Stack monitoring + incident lifecycle.