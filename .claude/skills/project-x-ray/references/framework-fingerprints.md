# Framework Fingerprints

Identifying frameworks, runtimes, and deployment patterns from file structure and dependency
file content — without running the code, without a README, without context.

Used during PHASE 1 of Project X-Ray when framework identification is uncertain.

---

## Confidence of Identification

Always state the basis. The same framework name can be present but unused.

| Evidence quality | Confidence | Label |
|---|---|---|
| Named in dependency file + matching file structure | High | Observed |
| Named in dependency file only, structure ambiguous | Medium | Inferred |
| File structure only, no dependency file present | Low | Inferred |
| Naming pattern only (folder/file name suggests framework) | Seed | Inferred, Low |

A dependency listed but with no corresponding usage pattern in the file structure
should be flagged in Section 9 as a possible unused dependency.

---

## Python

| Signal | What it suggests | Confidence |
|---|---|---|
| `requirements.txt` or `pyproject.toml` | Python project | High |
| `setup.py` or `setup.cfg` | Python package or library | High |
| `manage.py` + `settings.py` | Django | High |
| `apps/` + `manage.py` | Django multi-app structure | High |
| `app.py` or `wsgi.py` + `flask` in requirements | Flask | High |
| `main.py` + `fastapi` in requirements | FastAPI | High |
| `asgi.py` present | ASGI-capable framework (Django 3+, FastAPI, Starlette) | Medium |
| `alembic/` + `alembic.ini` | SQLAlchemy with Alembic migrations | High |
| `migrations/` under a Django app folder | Django ORM migrations | High |
| `celery` in requirements + `tasks.py` | Celery task queue | Medium |
| `beat_schedule` in code or config | Celery Beat scheduler | Medium |
| `Pipfile` | Pipenv environment management | High |
| `poetry.lock` | Poetry dependency management | High |
| `.env` + `python-dotenv` in requirements | dotenv environment variable loading | High |
| `pytest` in requirements or `conftest.py` present | pytest test suite | High |
| `unittest` imports in test files | Standard library test suite | High |
| `pydantic` in requirements | Data validation; likely FastAPI or data pipeline | Medium |
| `sqlalchemy` in requirements | SQLAlchemy ORM | High |
| `tortoise-orm` or `databases` in requirements | Async ORM; likely FastAPI | Medium |

---

## JavaScript / Node / TypeScript

| Signal | What it suggests | Confidence |
|---|---|---|
| `package.json` | Node.js project | High |
| `tsconfig.json` | TypeScript project | High |
| `next.config.js` or `next.config.ts` | Next.js | High |
| `pages/` directory in root | Next.js pages router | High |
| `app/` directory + Next.js in deps | Next.js app router | High |
| `nuxt.config.js` or `nuxt.config.ts` | Nuxt.js | High |
| `vite.config.js` or `vite.config.ts` | Vite bundler | High |
| `src/App.jsx` or `src/App.tsx` + React in deps | React SPA | High |
| `angular.json` | Angular | High |
| `svelte.config.js` | SvelteKit | High |
| `astro.config.mjs` | Astro | High |
| `remix.config.js` | Remix | High |
| `express` in deps + `routes/` folder | Express web server or REST API | Medium |
| `fastify` in deps | Fastify HTTP framework | High |
| `hono` in deps | Hono edge-ready framework | High |
| `prisma/` + `schema.prisma` | Prisma ORM | High |
| `drizzle.config.ts` | Drizzle ORM | High |
| `knexfile.js` | Knex query builder | High |
| `bull` or `bullmq` in deps | Redis-backed job queue | Medium |
| `jest.config.js` or `jest` in deps | Jest test suite | High |
| `vitest.config.ts` | Vitest test suite | High |
| `.env.local` | Next.js / Vite local environment convention | Medium |
| `bun.lockb` | Bun runtime | High |
| `deno.json` or `deno.lock` | Deno runtime | High |

---

## PHP

| Signal | What it suggests | Confidence |
|---|---|---|
| `composer.json` | PHP project | High |
| `artisan` file + `app/` + `routes/web.php` | Laravel | High |
| `config/app.php` + Laravel in composer | Laravel confirmed | High |
| `symfony.lock` or `config/bundles.php` | Symfony | High |
| `wp-config.php` or `wp-content/` | WordPress | High |
| `index.php` only, no framework signals | Plain PHP or bespoke CMS | Medium |
| `phpunit.xml` or PHPUnit in composer | PHPUnit test suite | High |

---

## Ruby

| Signal | What it suggests | Confidence |
|---|---|---|
| `Gemfile` | Ruby project | High |
| `config/routes.rb` + `app/controllers/` | Ruby on Rails | High |
| `config.ru` | Rack application (could be Rails, Sinatra, or custom) | Medium |
| `Rakefile` | Rake build tasks | High |
| `spec/` + `rspec` in Gemfile | RSpec test suite | High |
| `test/` + `minitest` in Gemfile | Minitest test suite | High |

---

## Go

| Signal | What it suggests | Confidence |
|---|---|---|
| `go.mod` | Go module | High |
| `main.go` in `cmd/` | Standard Go CLI or service structure | High |
| `gin` in go.mod | Gin HTTP framework | High |
| `echo` in go.mod | Echo HTTP framework | High |
| `fiber` in go.mod | Fiber HTTP framework | High |
| `chi` in go.mod | Chi HTTP router | High |
| `gorm` in go.mod | GORM ORM | High |
| `sqlx` in go.mod | sqlx database toolkit | High |
| `ent` in go.mod | Facebook Ent ORM | High |

---

## Rust

| Signal | What it suggests | Confidence |
|---|---|---|
| `Cargo.toml` | Rust project | High |
| `actix-web` in Cargo.toml | Actix HTTP framework | High |
| `axum` in Cargo.toml | Axum HTTP framework | High |
| `rocket` in Cargo.toml | Rocket HTTP framework | High |
| `sqlx` or `diesel` in Cargo.toml | SQL database access | High |
| `tokio` in Cargo.toml | Async runtime | High |
| `serde` in Cargo.toml | Serialisation; likely web or data project | Medium |

---

## Java / JVM

| Signal | What it suggests | Confidence |
|---|---|---|
| `pom.xml` | Maven Java project | High |
| `build.gradle` or `build.gradle.kts` | Gradle project (Java or Kotlin) | High |
| `src/main/java/` | Standard Maven/Gradle Java layout | High |
| `spring-boot` in pom or gradle | Spring Boot | High |
| `@SpringBootApplication` in source | Spring Boot confirmed | High |
| `quarkus` in pom | Quarkus | High |
| `micronaut` in pom | Micronaut | High |

---

## Databases — Schema and Persistence Signals

| Signal | What it suggests | Confidence |
|---|---|---|
| `migrations/` folder with numbered files | Migration-managed schema | High |
| `.sql` files in migrations | Raw SQL schema management | High |
| `schema.prisma` | Prisma schema definition | High |
| `schema.rb` | Rails ActiveRecord schema snapshot | High |
| `models.py` + Django structure | Django ORM model definitions | High |
| `ormconfig.json` or `ormconfig.ts` | TypeORM | High |
| `*.entity.ts` files | TypeORM entities | High |
| `mongo` or `mongoose` in deps | MongoDB | High |
| `redis` in deps | Redis (could be cache, queue, session, or primary store) | Medium |
| `elasticsearch` or `opensearch` in deps | Search index | High |
| `supabase` in deps or `supabase/` folder | Supabase backend | High |
| `firebase` in deps | Firebase (Firestore, Auth, or Functions) | Medium |
| `sqlite3` in deps | SQLite database | High |
| `pg` or `psycopg2` in deps | PostgreSQL | High |
| `mysql2` or `mysqlclient` in deps | MySQL or MariaDB | High |

---

## Deployment and Infrastructure

| Signal | What it suggests | Confidence |
|---|---|---|
| `Dockerfile` | Containerised application | High |
| `docker-compose.yml` or `compose.yaml` | Multi-container setup | High |
| `.github/workflows/*.yml` | GitHub Actions CI/CD | High |
| `.gitlab-ci.yml` | GitLab CI | High |
| `Jenkinsfile` | Jenkins pipeline | High |
| `fly.toml` | Fly.io deployment | High |
| `vercel.json` | Vercel deployment | High |
| `netlify.toml` | Netlify deployment | High |
| `render.yaml` | Render.com deployment | High |
| `Procfile` | Heroku-style process management | High |
| `heroku.yml` | Heroku container deployment | High |
| `terraform/` | Infrastructure as code (IaC) | High |
| `ansible/` | Ansible provisioning | High |
| `k8s/` or `kubernetes/` | Kubernetes manifests | High |
| `helm/` | Helm chart | High |
| `.env.example` or `.env.sample` | Environment variable documentation | High |
| `railway.toml` | Railway.app deployment | High |
| `coolify/` or `coolify.yml` | Coolify self-hosted deployment | Medium |

---

## Automation — n8n, Home Assistant, Node-RED, IoT

| Signal | What it suggests | Confidence |
|---|---|---|
| `n8n-workflow.json` or `workflow.json` with n8n node structure | n8n automation export | High |
| `flows.json` + Node-RED shape (type: tab, type: http in) | Node-RED flows | High |
| `configuration.yaml` + `automations.yaml` + `scripts.yaml` | Home Assistant | High |
| `custom_components/` in Home Assistant structure | HA custom integration | High |
| `esphome/` or `.yaml` files with ESPHome device config | ESPHome firmware | High |
| `mqtt` in config or `paho-mqtt` in requirements | MQTT messaging | High |
| `zigbee2mqtt/` folder or config | Zigbee2MQTT bridge | High |
| `appdaemon/` folder | AppDaemon (HA automation Python) | High |

---

## Security Signals — Flag Immediately in Section 10

These warrant a Critical or High entry in the risk audit regardless of confidence level.
Note them during PHASE 1 — do not wait for Section 10.

| Signal | Risk | Severity |
|---|---|---|
| `.env` committed to the repo | Secrets likely in version control | Critical |
| Hardcoded connection strings in source | Credentials in code | Critical |
| `SECRET_KEY = "..."` or `API_KEY = "..."` as literal strings | Hardcoded secret | Critical |
| `DEBUG = True` in an apparent production config | Debug mode in production | High |
| `CORS: origins: "*"` or `allow_origins=["*"]` | Open CORS policy | High |
| `eval(` or `exec(` with user input | Code injection risk | Critical |
| SQL built by string concatenation with user input | SQL injection risk | Critical |
| Passwords stored or compared as plaintext | No password hashing | Critical |
| No authentication middleware visible on admin routes | Unprotected admin | High |
| Dependency file with versions from 2+ years ago, no lockfile | Dependency rot | Medium |

---

## Cross-reference

Framework identification feeds into:
- Section 8 (Technical Guide) — architecture pattern, known framework behaviours
- Section 7 (Execution Flow) — framework-standard startup sequences
- Section 9 (What Is Missing) — expected files not present for identified framework
- Section 10 (Risk Audit) — framework-specific known vulnerability patterns
