# Chaos Demo API (Better Stack + PostHog)

**Uptime + incidents via Better Stack; backend event analytics via PostHog.**

## Monitoring & Incident Demo (Better Stack)

This project demonstrates monitoring, alerting, and incident management using Better Stack through an intentional failure scenario.

A dedicated endpoint (`/chaos`) was designed to return intermittent 5xx responses. An uptime monitor detects these failures and automatically triggers an incident, which is communicated via a public status page.

The incident is acknowledged, updated, and resolved once the service is stabilized and monitoring confirms recovery. This mirrors a real-world incident lifecycle: detection → investigation → communication → resolution.

The status page also includes a completed scheduled maintenance window to demonstrate planned operational workflows.

Status page: https://status.lillacsanaky.dev/

## Analytics (PostHog)

The API emits explicit PostHog events to track endpoint usage, failure rate, and request latency. This complements uptime monitoring and incident alerts.

Environment variables:
- POSTHOG_API_KEY
- POSTHOG_HOST (EU: https://eu.i.posthog.com)

---

Tiny FastAPI service with:
- `GET /health` → always returns 200
- `GET /chaos` → intermittently returns 500 (simulates a flaky dependency)

Used to demonstrate Better Stack monitoring, alerting, and incident lifecycle handling.