Full Server - Quick Guide

Run
- node Node_JS_basic/full_server/server.js Node_JS_basic/full_server/database.csv

Endpoints
- GET / → Hello Holberton School!
- GET /students → Aggregated list by field (CS, SWE)
- GET /students/:major → CS or SWE only (returns "List: ...")

Notes
- CSV must include header with firstname and field columns.
- In tests, server won’t listen (NODE_ENV=test).
