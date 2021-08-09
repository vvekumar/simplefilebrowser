FROM python:3.7

WORKDIR /opt/app

COPY ../.. .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP simplefilebrowser.api.app:app

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]