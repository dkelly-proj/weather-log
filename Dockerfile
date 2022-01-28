FROM python:3.9.1
WORKDIR /weather-log
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "./weather_log.py"]
