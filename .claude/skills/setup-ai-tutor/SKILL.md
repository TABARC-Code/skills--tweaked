---
name: setup-ai-tutor
description: Sets up and starts the AI Tutor project locally (environment file, dependencies, database, migrations, and dev server). Use when standing up the AI Tutor for the first time on a new machine or after a fresh clone. This is sample-project specific; adapt it when you install the AI Layer into your own project. Dewey 371.33.
---

# Set Up the AI Tutor Locally

Run the following commands to set up and start the AI Tutor locally.

## Input

None required. Run from the repository root.

## Process

### 1. Create Environment File
```bash
[ -f .env ] && echo ".env already exists, leaving it untouched" || cp .env.example .env
```
Creates your local environment configuration from the example template.

### 2. Install Dependencies
```bash
uv sync
```
Installs all Python packages defined in pyproject.toml.

### 3. Start Database
```bash
# use `docker compose` if `docker-compose` is not found; if neither exists, stop and tell the user
docker-compose up -d db
```
Starts PostgreSQL in a Docker container.

### 4. Run Database Migrations
```bash
uv run alembic upgrade head
```
Applies all pending database migrations.

### 5. Start Development Server
```bash
uv run uvicorn app.main:app --reload --port 8123 > /tmp/ai-tutor.log 2>&1 &
```
Run it in the background and keep the log, so the validation step can run in the same shell. Before validating, poll `curl -sf http://localhost:8123/health` up to 15 times, 2 seconds apart. If it still fails, show `/tmp/ai-tutor.log` and stop.
Starts the FastAPI server with hot-reload on port 8123.

### 6. Validate Setup

Check that everything is working:

```bash
# Test API health
curl -s http://localhost:8123/health

# Test database connection
curl -s http://localhost:8123/health/db
```

Both should return `{"status":"healthy"}` responses.

## Output

A running local AI Tutor instance.

### Access Points

- Swagger UI: http://localhost:8123/docs
- Health Check: http://localhost:8123/health
- Database: localhost (Docker container)

## Cleanup

To stop services:
```bash
# Stop dev server: kill the background uvicorn process
# Stop database: docker-compose down
```

## Notes

- Port numbers and the exact `docker-compose` service name may differ — check `docker-compose.yml`,
  `.env.example`, and the project README for project-specific values before running.

<!-- relationships:start -->
## Relationships

Bidirectional contracts. Generated from network/edges.json, so edit there, not here.

No links declared yet. Add one in network/edges.json and rebuild.
<!-- relationships:end -->
