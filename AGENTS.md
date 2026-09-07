# python-hello-world-app

Minimal Flask + Gunicorn app on Zerops that reads a greeting from PostgreSQL and returns it as JSON.

## Zerops service facts

- HTTP port: `8000`
- Siblings: `db` (PostgreSQL) — env: `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASS`, `DB_NAME`
- Runtime base: `python@3.12`

## Zerops dev

`setup: dev` idles on `zsc noop --silent`; the agent starts the dev server.

- Dev command: `python src/app.py` (Flask built-in server on `0.0.0.0:8000`; or `/var/www/vendor/bin/gunicorn --bind 0.0.0.0:8000 --workers 2 src.app:app` for the prod-like WSGI path)
- In-container rebuild without deploy: `pip install --target=./vendor -r requirements.txt`

**All platform operations (start/stop/status/logs of the dev server, deploy, env / scaling / storage / domains) go through the Zerops development workflow via `zcp` MCP tools. Don't shell out to `zcli`.**

## Notes

- Dependencies vendor into `./vendor`; `PYTHONPATH=/var/www/vendor` is set at runtime — no system-Python pollution, no `pip install` needed after SSH.
- Migration runs once per deploy via `python migrate.py` in `initCommands`, race-safe across multi-container deploys via `zsc execOnce`.
