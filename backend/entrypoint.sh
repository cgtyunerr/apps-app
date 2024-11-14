#!/bin/bash
# entrypoint.sh

# Wait until psql is ready.
until alembic upgrade head ; do
  echo "PostgreSQL is not ready, waiting..."
  sleep 2
done
echo "Migrations done.!"

# migrate db


# initialize app.
echo "Starting Uvicorn server..."
exec uvicorn src.main:app --host 0.0.0.0 --port 8000