FROM python:3.8-slim

EXPOSE 5001

WORKDIR /app

RUN python -m pip install Flask prometheus-flask-exporter

COPY flask_app.py ./app.py

ENTRYPOINT ["python"]

CMD ["-m", "flask", "run", "--host", "0.0.0.0", "--port", "5001"]