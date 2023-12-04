FROM python:3.11-alpine

WORKDIR /code
COPY ./requirements.txt ./requirements.txt 

RUN pip install -r ./requirements.txt

COPY . .

ENTRYPOINT ["sh",  "-c", "cd alembic && alembic upgrade head && cd .. && uvicorn src.main:app --host 0.0.0.0 --port 80 && exec \"$@\"", "--"]