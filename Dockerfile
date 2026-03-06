FROM python:3.12

WORKDIR /app
COPY ./02_Parkinson_app_deployment/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./02_Parkinson_app_deployment/* .
COPY rf_model_parkinson .

CMD ["python", "app.py"]