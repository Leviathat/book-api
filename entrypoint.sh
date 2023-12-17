
#!/bin/bash

cd "alembic"

while ! alembic upgrade head; do
    echo "Migration failed, retrying..."
    sleep 1
done

cd ..

uvicorn src.main:app --host 0.0.0.0 --port 80