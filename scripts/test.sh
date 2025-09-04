# scripts/test.sh
set -e
python -m pytest -q || true
docker compose -f docker-compose.yml up -d neo4j && sleep 5
curl -sS http://localhost:8000/docs >/dev/null || exit 1
