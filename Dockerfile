FROM python:3.9

WORKDIR /swdp-001-be

COPY ./requirements.txt /swdp-001-be/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /swdp-001-be/requirements.txt

COPY ./src /swdp-001-be/src

RUN python /swdp-001-be/src/data/create_db.py

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]