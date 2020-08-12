FROM python:3.6

COPY . /opt/predict_square
WORKDIR /opt/predict_square

RUN pip install pipenv
RUN pipenv lock -r > /requirements.txt
RUN pip install -r /requirements.txt

EXPOSE 8000

ENTRYPOINT ["gunicorn", "--worker-tmp-dir", "/dev/shm"]
CMD ["--bind", "0.0.0.0:8000", "app:api"]
