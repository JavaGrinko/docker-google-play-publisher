FROM python:3.7-slim

RUN pip install --no-cache-dir google-api-python-client oauth2client pyOpenSSL

COPY script.py /script.py

CMD ["python", "script.py"]
