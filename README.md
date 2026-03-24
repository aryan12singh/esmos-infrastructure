# ESMOS Infrastructure

**ESMOS Healthcare Training & Operations Platform**

Odoo 17 (ERP/Operations) + Moodle (Compliance Training) + Nginx (Reverse Proxy)

## Stack

| Service | Access | Description |
|---------|--------|-------------|
| Odoo | http://20.205.189.96 (port 80) | Meal planning & operations ERP |
| Moodle | http://20.205.189.96:8080 | Healthcare compliance training |

## CI/CD

Every push to `main` automatically deploys to the production VM via GitHub Actions.

## Local Development

```bash
git clone https://github.com/aryan12singh/esmos-infrastructure.git
cd esmos-infrastructure
docker-compose up -d
```

## Phase Roadmap

- **Phase 2 (current):** Docker + Nginx HTTP baseline + CI/CD pipeline
- **Phase 3:** HTTPS/SSL hardening via Let's Encrypt (RFC change)
