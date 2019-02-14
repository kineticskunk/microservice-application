FROM python:latest
ADD . /test
WORKDIR /test
EXPOSE 5000
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip flask_sqlalchemy
# ENTRYPOINT ["python", "wsgi.py"]
